#!/usr/bin/env python3
"""Validate generated Markdown requirement documents.

The default profile checks deterministic document structure. The full profile
also checks stable-ID definitions, progressive ASCII confirmation coverage,
interaction-to-ASCII coverage, and the requirement-to-ASCII trace chain.
It cannot determine whether the underlying product decisions are correct.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote


ALLOWED_ID_PREFIXES = {
    "AC",
    "AUD",
    "BG",
    "CHG",
    "CFLT",
    "CON",
    "CST",
    "DEC",
    "DRIFT",
    "FLOW",
    "FUNC",
    "IA",
    "INT",
    "JS",
    "NAV",
    "NFR",
    "OBJ",
    "PAGE",
    "Q",
    "REQ",
    "ROLE",
    "SCN",
    "SPEC",
    "SRC",
    "STATE",
    "STMT",
    "SUB",
    "SYS",
    "TASK",
    "UI",
    "US",
    "UXH",
}

DEFINITION_HEADERS: dict[str, set[str] | None] = {
    "ID": None,
    "AC ID": {"AC"},
    "验收标准 ID": {"AC"},
    "AUD ID": {"AUD"},
    "文档受众 ID": {"AUD"},
    "BG ID": {"BG"},
    "背景 ID": {"BG"},
    "CHANGE ID": {"CHG"},
    "CHG ID": {"CHG"},
    "变更 ID": {"CHG"},
    "CFLT ID": {"CFLT"},
    "冲突 ID": {"CFLT"},
    "CON ID": {"CON"},
    "概念 ID": {"CON"},
    "CST ID": {"CST"},
    "约束 ID": {"CST"},
    "DEC ID": {"DEC"},
    "决策 ID": {"DEC"},
    "确认决策 ID": {"DEC"},
    "DRIFT ID": {"DRIFT"},
    "漂移 ID": {"DRIFT"},
    "ELEMENT ID": {"UI"},
    "元素 ID": {"UI"},
    "FLOW/STEP ID": {"FLOW"},
    "流程/步骤 ID": {"FLOW"},
    "FUNC ID": {"FUNC"},
    "功能 ID": {"FUNC"},
    "IA ID": {"IA"},
    "信息架构 ID": {"IA"},
    "INT ID": {"INT"},
    "交互 ID": {"INT"},
    "NAV ID": {"NAV"},
    "导航 ID": {"NAV"},
    "NFR ID": {"NFR"},
    "非功能需求 ID": {"NFR"},
    "NFR/SPEC ID": {"NFR", "SPEC"},
    "非功能/规格 ID": {"NFR", "SPEC"},
    "OBJ ID": {"OBJ"},
    "目标 ID": {"OBJ"},
    "PAGE/FUNC ID": {"PAGE", "FUNC"},
    "页面/功能 ID": {"PAGE", "FUNC"},
    "Q ID": {"Q"},
    "问题 ID": {"Q"},
    "REQ ID": {"REQ"},
    "需求 ID": {"REQ"},
    "ROLE ID": {"ROLE"},
    "角色 ID": {"ROLE"},
    "RULE ID": {"SPEC"},
    "规则 ID": {"SPEC"},
    "SCN ID": {"SCN"},
    "场景 ID": {"SCN"},
    "SPEC ID": {"SPEC"},
    "规格 ID": {"SPEC"},
    "SRC ID": {"SRC"},
    "来源 ID": {"SRC"},
    "STATE ID": {"STATE"},
    "状态 ID": {"STATE"},
    "STMT ID": {"STMT"},
    "陈述 ID": {"STMT"},
    "SUB ID": {"SUB"},
    "子功能 ID": {"SUB"},
    "SYS ID": {"SYS"},
    "系统契约 ID": {"SYS"},
    "TASK ID": {"TASK"},
    "任务 ID": {"TASK"},
    "UI ID": {"UI"},
    "界面 ID": {"UI"},
    "US/JS ID": {"US", "JS"},
    "用户故事/任务故事 ID": {"US", "JS"},
    "用户/任务故事 ID": {"US", "JS"},
    "UXH ID": {"UXH"},
    "UX 假设 ID": {"UXH"},
}

FULL_PROFILE_REQUIREMENTS = (
    ({"BG"}, "background/problem statement"),
    ({"OBJ"}, "objective"),
    ({"ROLE"}, "target role"),
    ({"SCN"}, "target scenario"),
    ({"CON"}, "concept definition"),
    ({"REQ"}, "requirement register"),
    ({"TASK"}, "user-task backbone"),
    ({"FLOW"}, "task/decision flow"),
    ({"INT"}, "interaction behavior"),
    ({"US", "JS"}, "user or job story"),
    ({"IA"}, "information architecture"),
    ({"PAGE", "FUNC"}, "page or feature map"),
    ({"UI"}, "ASCII UI/screen definition"),
    ({"SPEC"}, "behavior specification"),
    ({"AC"}, "acceptance criterion"),
)

LINK_RE = re.compile(r"\[[^\]]*]\(([^)]+)\)")
ID_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,9})-[A-Z0-9][A-Z0-9-]*\b")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+]\([^)]+\)")
REVIEW_HANDOFF_HEADING_RE = re.compile(
    r"^#{1,6}\s+(?=.*(?:review|评审|审核|审查))(?=.*(?:delivery|handoff|交付)).+$",
    re.IGNORECASE,
)
DELIVERED_STRUCTURE_HEADING_RE = re.compile(
    r"^#{1,6}\s+(?=.*(?:file|document|artifact|文件|文档|交付物))"
    r"(?=.*(?:structure|tree|结构|目录)).+$",
    re.IGNORECASE,
)
LOCALIZED_PLACEHOLDER_RE = re.compile(
    r"\[(?:"
    r"Feature Name|Page or core feature name|Subfeature name|Focused interaction|"
    r"Primary area|Page/object|Task step|Decision [A-Z]|Next step|Recovery or exit|Page title|"
    r"Requirement name|Story name|User outcome|Activity(?: [A-Z])?|role|meaningful task|"
    r"situation|motivation/action|expected outcome|Summarize [^]]+|Describe [^]]+|"
    r"功能名称|页面名称|子功能名称|交互名称|主要区域|页面或对象|任务步骤|决策[^]]*|下一步|恢复或退出|页面标题|"
    r"需求名称|故事名称|用户结果|活动|角色|有意义的任务|场景|动机/行动|预期结果|概述[^]]*|描述[^]]*"
    r")\]"
    r"|待填写|待补充|请填写|替换为实际(?:页面|功能|内容)"
)
FIXED_PLACEHOLDERS = {
    "Replace with real page": "unresolved example-page instruction",
    "Draft / Provisional / Confirmed": "unresolved status choice",
    "Planned / N/A": "unresolved delivery-plan status choice",
}

BASELINE_STATUS_LABELS = {
    "BASELINE STATUS",
    "BASELINE VERSION/STATUS",
    "基线状态",
    "基线版本/状态",
}
STATUS_HEADERS = {"STATUS", "状态"}
DELIVERY_ITEM_HEADERS = {"FILE", "DELIVERABLE", "文件", "交付物"}
FINAL_DELIVERY_STATUSES = {
    "COMPLETE",
    "COMPLETED",
    "N/A",
    "NOT APPLICABLE",
    "OMITTED",
    "完成",
    "已完成",
    "不适用",
    "已省略",
}
ASCII_QUEUE_SCOPE_HEADERS = {"CONFIRMATION SCOPE", "确认范围"}
FINAL_ASCII_QUEUE_STATUSES = {
    "CONFIRMED",
    "CONFIRMED AND WRITTEN",
    "SUPERSEDED",
    "N/A",
    "NOT APPLICABLE",
    "OMITTED",
    "已确认",
    "已确认并写入",
    "已取代",
    "不适用",
    "已省略",
}


@dataclass(frozen=True)
class Site:
    file: Path
    line: int


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    file: Path
    line: int
    message: str


@dataclass
class Analysis:
    findings: list[Finding] = field(default_factory=list)
    definitions: dict[str, set[Site]] = field(default_factory=lambda: defaultdict(set))
    occurrences: dict[str, set[Site]] = field(default_factory=lambda: defaultdict(set))
    edges: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    ascii_flow_sites: set[Site] = field(default_factory=set)
    baseline_statuses: list[tuple[str, Site]] = field(default_factory=list)
    review_handoff_sites: set[Site] = field(default_factory=set)
    delivered_structure_sites: set[Site] = field(default_factory=set)
    ascii_confirmation_statuses: dict[str, list[tuple[str, Site]]] = field(
        default_factory=lambda: defaultdict(list)
    )
    ascii_queue_statuses: list[tuple[str, Site]] = field(default_factory=list)

    def merge(self, other: "Analysis") -> None:
        self.findings.extend(other.findings)
        for stable_id, sites in other.definitions.items():
            self.definitions[stable_id].update(sites)
        for stable_id, sites in other.occurrences.items():
            self.occurrences[stable_id].update(sites)
        for stable_id, neighbors in other.edges.items():
            self.edges[stable_id].update(neighbors)
        self.ascii_flow_sites.update(other.ascii_flow_sites)
        self.baseline_statuses.extend(other.baseline_statuses)
        self.review_handoff_sites.update(other.review_handoff_sites)
        self.delivered_structure_sites.update(other.delivered_structure_sites)
        for stable_id, statuses in other.ascii_confirmation_statuses.items():
            self.ascii_confirmation_statuses[stable_id].extend(statuses)
        self.ascii_queue_statuses.extend(other.ascii_queue_statuses)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a single Markdown requirement file or a multi-file document set."
    )
    parser.add_argument("target", type=Path, help="Markdown file or document directory")
    parser.add_argument(
        "--final",
        action="store_true",
        help="Treat unresolved templates, stale delivery statuses, missing backlinks, and ID integrity issues as errors.",
    )
    parser.add_argument(
        "--profile",
        choices=("structural", "full"),
        default="structural",
        help="Use 'full' for confirmed-baseline and requirement-to-ASCII trace-chain coverage.",
    )
    return parser.parse_args()


def markdown_files(target: Path) -> list[Path]:
    if target.is_file():
        if target.suffix.lower() != ".md":
            raise ValueError(f"target file is not Markdown: {target}")
        return [target]
    if target.is_dir():
        files = []
        for path in target.rglob("*.md"):
            if not any(part.startswith(".") for part in path.relative_to(target).parts):
                files.append(path)
        return sorted(files)
    raise ValueError(f"target does not exist: {target}")


def severity(final: bool) -> str:
    return "error" if final else "warning"


def prefix_of(stable_id: str) -> str:
    return stable_id.split("-", 1)[0]


def extract_ids(text: str) -> list[str]:
    return [match.group(0) for match in ID_RE.finditer(text)]


def normalize_header(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("`", "").strip()).upper()


def is_confirmed_baseline_status(value: str) -> bool:
    normalized = normalize_header(value)
    if (
        "NOT CONFIRMED" in normalized
        or "UNCONFIRMED" in normalized
        or "AWAITING" in normalized
        or "PENDING" in normalized
        or "待确认" in normalized
        or "未确认" in normalized
    ):
        return False
    return (
        bool(re.search(r"\bCONFIRMED\b", normalized))
        or "已确认" in normalized
        or "有条件确认" in normalized
    )


def is_confirmed_ascii_status(value: str) -> bool:
    return normalize_header(value) in {
        "CONFIRMED",
        "CONFIRMED AND WRITTEN",
        "已确认",
        "已确认并写入",
    }


def split_table_cells(line: str) -> list[str]:
    stripped = line.strip()
    content = stripped[1:-1] if stripped.startswith("|") and stripped.endswith("|") else stripped
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for character in content:
        if character == "\\" and not escaped:
            escaped = True
            current.append(character)
            continue
        if character == "|" and not escaped:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        escaped = False
    cells.append("".join(current).strip())
    return cells


def is_separator_row(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    if " '" in target:
        target = target.split(" '", 1)[0]
    return unquote(target.split("#", 1)[0])


def local_link_destination(source: Path, raw_target: str) -> Path | None:
    target = normalize_link_target(raw_target)
    if not target or target.startswith(("#", "/")):
        return None
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target):
        return None
    return (source.parent / target).resolve()


def add_row_edges(analysis: Analysis, ids: list[str]) -> None:
    unique_ids = sorted(set(ids))
    for index, stable_id in enumerate(unique_ids):
        for neighbor in unique_ids[index + 1 :]:
            analysis.edges[stable_id].add(neighbor)
            analysis.edges[neighbor].add(stable_id)


def inspect_file(path: Path, final: bool) -> Analysis:
    analysis = Analysis()
    lines = path.read_text(encoding="utf-8").splitlines()
    in_fence = False
    fence_marker = ""
    fence_is_ascii = False
    fence_has_flow = False
    fence_start_line = 0
    table_headers: list[str] | None = None
    table_cell_count: int | None = None
    definition_columns: dict[int, set[str] | None] = {}
    status_column: int | None = None
    delivery_table = False
    ascii_queue_table = False

    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()

        fence_match = re.match(r"^(```+|~~~+)", stripped)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_language = stripped[len(fence_match.group(1)) :].strip().lower()
                fence_is_ascii = fence_language in {"", "text", "txt"}
                fence_has_flow = False
                fence_start_line = line_number
            elif marker == fence_marker:
                if fence_is_ascii and fence_has_flow:
                    analysis.ascii_flow_sites.add(Site(path, fence_start_line))
                in_fence = False
                fence_marker = ""
                fence_is_ascii = False
                fence_has_flow = False
                fence_start_line = 0
            table_headers = None
            table_cell_count = None
            definition_columns = {}
            status_column = None
            delivery_table = False
            ascii_queue_table = False
            continue

        if in_fence:
            if fence_is_ascii and (
                re.search(r"(?:--?>|<--?|→|←|↓|↑)", line)
                or stripped in {"|", "v", "V"}
            ):
                fence_has_flow = True
            if LOCALIZED_PLACEHOLDER_RE.search(line):
                analysis.findings.append(
                    Finding(
                        severity(final),
                        "PLACEHOLDER",
                        path,
                        line_number,
                        "unresolved localized or template placeholder in code fence",
                    )
                )
            for placeholder, message in FIXED_PLACEHOLDERS.items():
                if placeholder in line:
                    analysis.findings.append(
                        Finding(severity(final), "PLACEHOLDER", path, line_number, message)
                    )
            continue

        site = Site(path, line_number)
        if REVIEW_HANDOFF_HEADING_RE.match(stripped):
            analysis.review_handoff_sites.add(site)
        if DELIVERED_STRUCTURE_HEADING_RE.match(stripped):
            analysis.delivered_structure_sites.add(site)
        line_ids = extract_ids(line)
        for stable_id in line_ids:
            analysis.occurrences[stable_id].add(site)
            if prefix_of(stable_id) not in ALLOWED_ID_PREFIXES:
                analysis.findings.append(
                    Finding(
                        "warning",
                        "UNKNOWN_ID_PREFIX",
                        path,
                        line_number,
                        f"unknown stable-ID prefix '{prefix_of(stable_id)}'",
                    )
                )

        placeholder_candidate = MARKDOWN_LINK_RE.sub("", line)
        if LOCALIZED_PLACEHOLDER_RE.search(placeholder_candidate):
            analysis.findings.append(
                Finding(
                    severity(final),
                    "PLACEHOLDER",
                    path,
                    line_number,
                    "unresolved localized or template placeholder",
                )
            )
        for placeholder, message in FIXED_PLACEHOLDERS.items():
            if placeholder in line:
                analysis.findings.append(
                    Finding(severity(final), "PLACEHOLDER", path, line_number, message)
                )

        is_table_row = stripped.startswith("|") and stripped.endswith("|")
        if is_table_row:
            cells = split_table_cells(stripped)
            if table_cell_count is not None and len(cells) != table_cell_count:
                analysis.findings.append(
                    Finding(
                        "error",
                        "TABLE_COLUMNS",
                        path,
                        line_number,
                        f"table row has {len(cells)} cells; expected {table_cell_count}",
                    )
                )

            if table_headers is None:
                table_headers = cells
                table_cell_count = len(cells)
                definition_columns = {}
                for index, header in enumerate(table_headers):
                    normalized = normalize_header(header)
                    if normalized in DEFINITION_HEADERS:
                        definition_columns[index] = DEFINITION_HEADERS[normalized]
                normalized_headers = {normalize_header(header) for header in table_headers}
                status_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in STATUS_HEADERS
                    ),
                    None,
                )
                delivery_table = bool(
                    DELIVERY_ITEM_HEADERS & normalized_headers
                    and STATUS_HEADERS & normalized_headers
                )
                ascii_queue_table = bool(
                    ASCII_QUEUE_SCOPE_HEADERS & normalized_headers
                    and STATUS_HEADERS & normalized_headers
                )
            elif not is_separator_row(cells):
                add_row_edges(analysis, line_ids)
                for column, allowed_prefixes in definition_columns.items():
                    if column >= len(cells):
                        continue
                    for stable_id in extract_ids(cells[column]):
                        if allowed_prefixes is None or prefix_of(stable_id) in allowed_prefixes:
                            analysis.definitions[stable_id].add(site)

                if ascii_queue_table and status_column is not None:
                    queue_status = cells[status_column].strip() if status_column < len(cells) else ""
                    analysis.ascii_queue_statuses.append((queue_status, site))

                for stable_id in line_ids:
                    if stable_id.startswith("DEC-ASCII-"):
                        confirmation_status = (
                            cells[status_column].strip()
                            if status_column is not None and status_column < len(cells)
                            else ""
                        )
                        analysis.ascii_confirmation_statuses[stable_id].append(
                            (confirmation_status, site)
                        )

                if len(cells) >= 2 and normalize_header(cells[0]) in BASELINE_STATUS_LABELS:
                    baseline_value = cells[1].strip()
                    analysis.baseline_statuses.append((baseline_value, site))
                    if not is_confirmed_baseline_status(baseline_value):
                        analysis.findings.append(
                            Finding(
                                severity(final),
                                "UNCONFIRMED_BASELINE",
                                path,
                                line_number,
                                f"baseline status is not confirmed: "
                                f"{baseline_value or '(empty)'}",
                            )
                        )

                if (
                    path.name == "index.md"
                    and delivery_table
                    and status_column is not None
                    and status_column < len(cells)
                ):
                    delivery_status = normalize_header(cells[status_column])
                    if delivery_status not in FINAL_DELIVERY_STATUSES:
                        analysis.findings.append(
                            Finding(
                                severity(final),
                                "STALE_STATUS",
                                path,
                                line_number,
                                f"delivery item has non-final status: "
                                f"{cells[status_column].strip() or '(empty)'}",
                            )
                        )
        else:
            table_headers = None
            table_cell_count = None
            definition_columns = {}
            status_column = None
            delivery_table = False
            ascii_queue_table = False

        for match in LINK_RE.finditer(line):
            destination = local_link_destination(path, match.group(1))
            if destination is not None and not destination.exists():
                analysis.findings.append(
                    Finding(
                        "error",
                        "BROKEN_LINK",
                        path,
                        line_number,
                        f"relative link target does not exist: {match.group(1)}",
                    )
                )

    if in_fence:
        analysis.findings.append(
            Finding("error", "UNCLOSED_FENCE", path, len(lines), "Markdown code fence is not closed")
        )

    return analysis


def inspect_document_set(target: Path, files: list[Path], final: bool) -> list[Finding]:
    findings: list[Finding] = []
    if not target.is_dir():
        return findings

    index = (target / "index.md").resolve()
    if not index.exists():
        return findings

    index_destinations = {
        destination
        for raw_target in LINK_RE.findall(index.read_text(encoding="utf-8"))
        if (destination := local_link_destination(index, raw_target)) is not None
        and destination.suffix.lower() == ".md"
    }

    for path in files:
        resolved = path.resolve()
        if resolved == index:
            continue

        link_destinations = {
            destination
            for raw_target in LINK_RE.findall(path.read_text(encoding="utf-8"))
            if (destination := local_link_destination(path, raw_target)) is not None
        }
        if index not in link_destinations:
            findings.append(
                Finding(
                    severity(final),
                    "MISSING_INDEX_LINK",
                    path,
                    1,
                    "file does not contain a relative link back to index.md",
                )
            )
        if resolved not in index_destinations:
            findings.append(
                Finding(
                    severity(final),
                    "UNLISTED_FILE",
                    path,
                    1,
                    "Markdown file is not listed in index.md",
                )
            )
        if path.parent == target and not re.fullmatch(
            r"(?:index|[a-z0-9]+(?:-[a-z0-9]+)*)\.md", path.name
        ):
            findings.append(
                Finding(
                    severity(final),
                    "FILENAME",
                    path,
                    1,
                    "top-level filename should use lowercase hyphen-case",
                )
            )

    return findings


def reachable_prefix(
    start: str,
    target_prefixes: set[str],
    edges: dict[str, set[str]],
    max_depth: int = 4,
) -> bool:
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        current, depth = queue.popleft()
        if current != start and prefix_of(current) in target_prefixes:
            return True
        if depth >= max_depth:
            continue
        for neighbor in edges.get(current, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, depth + 1))
    return False


def semantic_findings(analysis: Analysis, final: bool, profile: str) -> list[Finding]:
    if profile != "full":
        return []

    findings: list[Finding] = []
    strict_severity = severity(final)

    for stable_id, sites in analysis.definitions.items():
        if len(sites) > 1:
            first = sorted(sites, key=lambda site: (str(site.file), site.line))[0]
            locations = ", ".join(
                f"{site.file.name}:{site.line}"
                for site in sorted(sites, key=lambda site: (str(site.file), site.line))
            )
            findings.append(
                Finding(
                    strict_severity,
                    "DUPLICATE_ID",
                    first.file,
                    first.line,
                    f"{stable_id} has multiple canonical definitions: {locations}",
                )
            )

    for stable_id, sites in analysis.occurrences.items():
        if prefix_of(stable_id) in ALLOWED_ID_PREFIXES and stable_id not in analysis.definitions:
            first = sorted(sites, key=lambda site: (str(site.file), site.line))[0]
            findings.append(
                Finding(
                    strict_severity,
                    "DANGLING_ID",
                    first.file,
                    first.line,
                    f"{stable_id} is referenced but has no canonical definition",
                )
            )

    present_prefixes = {prefix_of(stable_id) for stable_id in analysis.definitions}
    fallback_file = next(
        (next(iter(sites)).file for sites in analysis.occurrences.values() if sites),
        Path("."),
    )
    for accepted_prefixes, label in FULL_PROFILE_REQUIREMENTS:
        if not (accepted_prefixes & present_prefixes):
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_ARTIFACT",
                    fallback_file,
                    1,
                    f"full profile has no canonical {label} definition",
                )
            )
    if "FUNC" not in present_prefixes:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_FUNCTION_DECOMPOSITION",
                fallback_file,
                1,
                "full profile requires story-derived FUNC definitions",
            )
        )
    if not analysis.review_handoff_sites:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_REVIEW_HANDOFF",
                fallback_file,
                1,
                "full profile requires a persisted Review and delivery summary section",
            )
        )
    if not analysis.delivered_structure_sites:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_DELIVERED_STRUCTURE",
                fallback_file,
                1,
                "full profile requires the actual delivered file or document structure",
            )
        )
    if not analysis.ascii_queue_statuses:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_ASCII_CONFIRMATION_QUEUE",
                fallback_file,
                1,
                "full profile requires a populated ASCII UX confirmation queue",
            )
        )
    else:
        for queue_status, site in analysis.ascii_queue_statuses:
            if normalize_header(queue_status) not in FINAL_ASCII_QUEUE_STATUSES:
                findings.append(
                    Finding(
                        strict_severity,
                        "UNRESOLVED_ASCII_CONFIRMATION",
                        site.file,
                        site.line,
                        f"ASCII confirmation unit has non-final status: "
                        f"{queue_status or '(empty)'}",
                    )
                )

    confirmed_ascii_decisions = {
        stable_id
        for stable_id, statuses in analysis.ascii_confirmation_statuses.items()
        if any(is_confirmed_ascii_status(status) for status, _site in statuses)
    }

    baseline_ids = sorted(
        stable_id
        for stable_id in analysis.definitions
        if stable_id.startswith("DEC-BASELINE-")
    )
    if not baseline_ids:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_BASELINE_CONFIRMATION",
                fallback_file,
                1,
                "full profile has no canonical DEC-BASELINE confirmation record",
            )
        )
    else:
        for stable_id in baseline_ids:
            first = sorted(
                analysis.definitions[stable_id],
                key=lambda site: (str(site.file), site.line),
            )[0]
            if not reachable_prefix(
                stable_id, {"REQ", "TASK", "US", "JS"}, analysis.edges
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_BASELINE_CONFIRMATION",
                        first.file,
                        first.line,
                        f"{stable_id} does not identify confirmed REQ/TASK/US/JS coverage",
                    )
                )

    if not analysis.baseline_statuses:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_CONFIRMED_BASELINE_STATUS",
                fallback_file,
                1,
                "full profile has no explicit baseline status field",
            )
        )

    if "FLOW" in present_prefixes and not analysis.ascii_flow_sites:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_ASCII_FLOW",
                fallback_file,
                1,
                "full profile defines FLOW IDs but has no ASCII flow in a text fence",
            )
        )

    for stable_id, sites in analysis.definitions.items():
        stable_prefix = prefix_of(stable_id)
        first = sorted(sites, key=lambda site: (str(site.file), site.line))[0]
        if stable_prefix in {"US", "JS"}:
            if not reachable_prefix(
                stable_id, {"REQ", "SCN", "TASK", "FLOW"}, analysis.edges
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_STORY_UPSTREAM",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to REQ/SCN/TASK/FLOW",
                    )
                )
            if not reachable_prefix(
                stable_id, {"UI", "SPEC", "SYS", "AC"}, analysis.edges
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_STORY_DOWNSTREAM",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to UI/SPEC/SYS/AC",
                    )
                )
            if not reachable_prefix(stable_id, {"FUNC"}, analysis.edges):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_STORY_FUNCTION",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to a story-derived FUNC capability",
                    )
                )
        elif stable_prefix == "FUNC":
            if not reachable_prefix(stable_id, {"US", "JS"}, analysis.edges):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_FUNCTION_STORY",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to a confirmed user/job story",
                    )
                )
            if not reachable_prefix(
                stable_id, {"PAGE", "SUB", "UI", "INT"}, analysis.edges
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_FUNCTION_SURFACE",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to a user-facing PAGE/SUB/UI/INT surface",
                    )
                )
        elif stable_prefix == "INT":
            if not reachable_prefix(stable_id, {"UI", "STATE"}, analysis.edges):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_INTERACTION_UI",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to an ASCII UI/STATE frame",
                    )
                )
        elif stable_prefix == "CHG":
            if not reachable_prefix(
                stable_id,
                {"REQ", "TASK", "US", "JS", "UI", "STATE", "SPEC", "AC"},
                analysis.edges,
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_CHANGE",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to an affected requirement, story, UI, state, specification, or acceptance criterion",
                    )
                )
        elif stable_prefix == "UI":
            if not reachable_prefix(stable_id, {"US", "JS"}, analysis.edges):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_UI_STORY",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to a user/job story",
                    )
                )
            if not reachable_prefix(stable_id, {"SPEC", "SYS", "AC"}, analysis.edges):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_UI_BEHAVIOR",
                        first.file,
                        first.line,
                        f"{stable_id} does not trace to SPEC/SYS/AC",
                    )
                )
            if not (analysis.edges.get(stable_id, set()) & confirmed_ascii_decisions):
                findings.append(
                    Finding(
                        strict_severity,
                        "MISSING_ASCII_CONFIRMATION",
                        first.file,
                        first.line,
                        f"{stable_id} is not directly covered by a confirmed DEC-ASCII record",
                    )
                )
        elif stable_prefix == "AC" and not reachable_prefix(
            stable_id, {"REQ", "US", "JS", "UI", "SPEC", "SYS"}, analysis.edges
        ):
            findings.append(
                Finding(
                    strict_severity,
                    "ORPHAN_AC",
                    first.file,
                    first.line,
                    f"{stable_id} does not trace to requirement, story, UI, or specification behavior",
                )
            )

    return findings


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    target = args.target.resolve()

    try:
        files = markdown_files(target)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if not files:
        print(f"ERROR: no Markdown files found under {target}", file=sys.stderr)
        return 2

    analysis = Analysis()
    for path in files:
        try:
            analysis.merge(inspect_file(path, args.final))
        except (OSError, UnicodeError) as error:
            analysis.findings.append(Finding("error", "READ_ERROR", path, 1, str(error)))

    analysis.findings.extend(inspect_document_set(target, files, args.final))
    analysis.findings.extend(
        semantic_findings(analysis, args.final, args.profile)
    )

    root = target if target.is_dir() else target.parent
    for finding in sorted(
        analysis.findings,
        key=lambda item: (item.severity != "error", str(item.file), item.line, item.code),
    ):
        print(
            f"{finding.severity.upper()} {finding.code} "
            f"{display_path(finding.file, root)}:{finding.line} {finding.message}"
        )

    errors = sum(finding.severity == "error" for finding in analysis.findings)
    warnings = sum(finding.severity == "warning" for finding in analysis.findings)
    print(
        f"Checked {len(files)} Markdown file(s), "
        f"{len(analysis.definitions)} canonical ID(s): "
        f"{errors} error(s), {warnings} warning(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
