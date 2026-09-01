#!/usr/bin/env python3
"""Validate generated Markdown requirement documents.

The default profile checks deterministic document structure. Stage profiles
check the contracts owned by baseline, happy-path, interaction, or delivery
work. The full profile checks the complete trace chain across all stages.
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
    "UXGAP",
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
    "FLOW ID": {"FLOW"},
    "流程 ID": {"FLOW"},
    "HAPPY PATH ID": {"FLOW"},
    "成功路径 ID": {"FLOW"},
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
    "UXGAP ID": {"UXGAP"},
    "UX GAP ID": {"UXGAP"},
    "UX 鸿沟 ID": {"UXGAP"},
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

STAGE_PROFILE_REQUIREMENTS = {
    "baseline": (
        ({"BG"}, "background/problem statement"),
        ({"OBJ"}, "objective"),
        ({"ROLE"}, "target role"),
        ({"SCN"}, "target scenario"),
        ({"CON"}, "concept definition"),
        ({"REQ"}, "requirement register"),
        ({"TASK"}, "user-task backbone"),
        ({"US", "JS"}, "user or job story"),
    ),
    "happy-path": (
        ({"FLOW"}, "happy path"),
    ),
    "interaction": (
        ({"FUNC"}, "functional decomposition"),
        ({"IA"}, "information architecture"),
        ({"INT"}, "interaction behavior"),
        ({"UI"}, "ASCII UI/screen definition"),
    ),
    "model-fit": (
        ({"ROLE"}, "target role"),
        ({"SCN"}, "target scenario"),
        ({"FLOW", "INT", "UI", "STATE"}, "reviewed interaction scope"),
    ),
    "delivery": (
        ({"SPEC"}, "behavior specification"),
        ({"AC"}, "acceptance criterion"),
    ),
}

COMMON_STAGE_CODES = {
    "DUPLICATE_ID",
    "DANGLING_ID",
    "ORPHAN_CHANGE",
}

STAGE_PROFILE_CODES = {
    "baseline": {
        "MISSING_BASELINE_CONFIRMATION",
        "ORPHAN_BASELINE_CONFIRMATION",
        "MISSING_CONFIRMED_BASELINE_STATUS",
        "ORPHAN_STORY_UPSTREAM",
    },
    "happy-path": {
        "MISSING_HAPPY_PATH_WAIVER_RATIONALE",
        "MISSING_HAPPY_PATH",
        "MISSING_HAPPY_PATH_BASIS",
        "MISSING_HAPPY_PATH_ADVERSARIAL_REVIEW",
        "ORPHAN_HAPPY_PATH_UPSTREAM",
        "ORPHAN_HAPPY_PATH_STORY",
        "MISSING_HAPPY_PATH_CONFIRMATION",
        "UNCONFIRMED_HAPPY_PATH",
    },
    "interaction": {
        "MISSING_FUNCTION_DECOMPOSITION",
        "MISSING_ASCII_CONFIRMATION_QUEUE",
        "UNRESOLVED_ASCII_CONFIRMATION",
        "MISSING_ASCII_FLOW",
        "ORPHAN_STORY_FUNCTION",
        "ORPHAN_FUNCTION_STORY",
        "ORPHAN_FUNCTION_SURFACE",
        "ORPHAN_INTERACTION_UI",
        "ORPHAN_UI_STORY",
        "MISSING_ASCII_CONFIRMATION",
    },
    "model-fit": {
        "MISSING_MODEL_FIT_COVERAGE",
        "MISSING_FLOW_MODEL_FIT_REVIEW",
        "MISSING_REPRESENTATION_MODEL_FIT_REVIEW",
        "INCOMPLETE_MODEL_FIT_COVERAGE",
        "ORPHAN_MODEL_FIT_COVERAGE",
        "MISSING_MODEL_FIT_RATIONALE",
        "INCOMPLETE_UXGAP_RECORD",
        "ORPHAN_UXGAP_CONTEXT",
        "OPEN_CRITICAL_UXGAP",
        "CONFIRMED_ASCII_WITH_OPEN_CRITICAL_UXGAP",
    },
    "delivery": {
        "MISSING_DELIVERY_PROFILE",
        "CONFLICTING_DELIVERY_PROFILE",
        "INVALID_DELIVERY_PROFILE",
        "DELIVERY_PROFILE_MISMATCH",
        "MISSING_SPLIT_RATIONALE",
        "MISSING_REVIEW_HANDOFF",
        "MISSING_DELIVERED_STRUCTURE",
        "ORPHAN_STORY_DOWNSTREAM",
        "ORPHAN_UI_BEHAVIOR",
        "ORPHAN_AC",
    },
}

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
    r"Happy path name|DEC-HAPPY reference|related baseline IDs|FLOW references|FLOW-HP reference|"
    r"SCN/REQ/TASK/US/JS references|Trigger and normal context|Required understanding or input|"
    r"Required understanding/input|Consequential user action|Consequential action|Required system work|"
    r"User verifies the intended result|User verifies outcome|Trigger|"
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
    "Confirmed / Blocked / Not applicable": "unresolved happy-path coverage status",
}

BASELINE_STATUS_LABELS = {
    "BASELINE STATUS",
    "BASELINE VERSION/STATUS",
    "基线状态",
    "基线版本/状态",
}
DELIVERY_PROFILE_LABELS = {"DELIVERY PROFILE", "交付模式", "交付配置"}
SPLIT_RATIONALE_LABELS = {"SPLIT RATIONALE", "拆分理由", "拆分原因"}
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
DELIVERY_PROFILE_FILE_RANGES = {
    "COMPACT": (1, 1),
    "紧凑": (1, 1),
    "单文件": (1, 1),
    "BALANCED": (2, 3),
    "平衡": (2, 3),
    "MODULAR": (4, None),
    "模块化": (4, None),
}
ASCII_QUEUE_SCOPE_HEADERS = {"CONFIRMATION SCOPE", "确认范围"}
HAPPY_PATH_COVERAGE_HEADERS = {"HAPPY PATH COVERAGE", "成功路径覆盖"}
RATIONALE_HEADERS = {"RATIONALE", "理由"}
HAPPY_PATH_BASIS_HEADERS = {
    "FUNDAMENTAL USER OUTCOME",
    "根本用户结果",
}
HAPPY_PATH_COMPLETION_HEADERS = {
    "OBSERVABLE COMPLETION EVIDENCE",
    "可观察完成证据",
    "可验证完成证据",
}
ADVERSARIAL_CHALLENGE_HEADERS = {"CHALLENGE", "审查问题", "挑战"}
ADVERSARIAL_IMPACT_HEADERS = {"PATH IMPACT", "路径影响"}
CONFIRMED_HAPPY_PATH_STATUSES = {
    "CONFIRMED",
    "CONFIRMED WITH CONDITIONS",
    "已确认",
    "有条件确认",
}
HAPPY_PATH_WAIVER_STATUSES = {
    "BLOCKED",
    "NOT APPLICABLE",
    "N/A",
    "阻塞",
    "不适用",
}
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
MODEL_FIT_COVERAGE_HEADERS = {
    "MODEL-FIT REVIEW COVERAGE",
    "MODEL FIT REVIEW COVERAGE",
    "模型适配审查范围",
}
MODEL_FIT_RESULT_HEADERS = {"RESULT", "结果"}
EVIDENCE_STATUS_HEADERS = {"EVIDENCE STATUS", "证据状态"}
MODEL_FIT_RATIONALE_HEADERS = {
    "RATIONALE/LIMITATION",
    "RATIONALE / LIMITATION",
    "理由/限制",
    "理由或限制",
}
UXGAP_SEVERITY_HEADERS = {"SEVERITY", "严重度"}
UXGAP_RESOLUTION_HEADERS = {
    "RESOLUTION/STATUS",
    "RESOLUTION / STATUS",
    "解决/状态",
    "修复与状态",
}
CRITICAL_UXGAP_SEVERITIES = {"CRITICAL", "关键", "严重"}
CLOSED_CRITICAL_UXGAP_STATUSES = {
    "RESOLVED",
    "SUPERSEDED",
    "已解决",
    "已修复",
    "已取代",
}
MODEL_FIT_WAIVER_RESULTS = {
    "BLOCKED",
    "NOT APPLICABLE",
    "N/A",
    "阻塞",
    "不适用",
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
    happy_path_basis_ids: dict[str, set[Site]] = field(
        default_factory=lambda: defaultdict(set)
    )
    happy_path_adversarial_ids: dict[str, set[Site]] = field(
        default_factory=lambda: defaultdict(set)
    )
    happy_path_confirmation_statuses: dict[str, list[tuple[str, Site]]] = field(
        default_factory=lambda: defaultdict(list)
    )
    happy_path_coverage: list[tuple[str, str, Site]] = field(default_factory=list)
    baseline_statuses: list[tuple[str, Site]] = field(default_factory=list)
    delivery_profiles: list[tuple[str, Site]] = field(default_factory=list)
    split_rationales: list[tuple[str, Site]] = field(default_factory=list)
    review_handoff_sites: set[Site] = field(default_factory=set)
    delivered_structure_sites: set[Site] = field(default_factory=set)
    ascii_confirmation_statuses: dict[str, list[tuple[str, Site]]] = field(
        default_factory=lambda: defaultdict(list)
    )
    ascii_queue_statuses: list[tuple[str, Site]] = field(default_factory=list)
    model_fit_coverage: list[
        tuple[str, str, str, str, set[str], Site]
    ] = field(default_factory=list)
    uxgap_records: dict[str, list[tuple[str, str, Site]]] = field(
        default_factory=lambda: defaultdict(list)
    )

    def merge(self, other: "Analysis") -> None:
        self.findings.extend(other.findings)
        for stable_id, sites in other.definitions.items():
            self.definitions[stable_id].update(sites)
        for stable_id, sites in other.occurrences.items():
            self.occurrences[stable_id].update(sites)
        for stable_id, neighbors in other.edges.items():
            self.edges[stable_id].update(neighbors)
        self.ascii_flow_sites.update(other.ascii_flow_sites)
        for stable_id, sites in other.happy_path_basis_ids.items():
            self.happy_path_basis_ids[stable_id].update(sites)
        for stable_id, sites in other.happy_path_adversarial_ids.items():
            self.happy_path_adversarial_ids[stable_id].update(sites)
        for stable_id, statuses in other.happy_path_confirmation_statuses.items():
            self.happy_path_confirmation_statuses[stable_id].extend(statuses)
        self.happy_path_coverage.extend(other.happy_path_coverage)
        self.baseline_statuses.extend(other.baseline_statuses)
        self.delivery_profiles.extend(other.delivery_profiles)
        self.split_rationales.extend(other.split_rationales)
        self.review_handoff_sites.update(other.review_handoff_sites)
        self.delivered_structure_sites.update(other.delivered_structure_sites)
        for stable_id, statuses in other.ascii_confirmation_statuses.items():
            self.ascii_confirmation_statuses[stable_id].extend(statuses)
        self.ascii_queue_statuses.extend(other.ascii_queue_statuses)
        self.model_fit_coverage.extend(other.model_fit_coverage)
        for stable_id, records in other.uxgap_records.items():
            self.uxgap_records[stable_id].extend(records)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a Compact, Balanced, or Modular Markdown requirement delivery."
    )
    parser.add_argument("target", type=Path, help="Markdown file or document directory")
    parser.add_argument(
        "--final",
        action="store_true",
        help="Treat unresolved templates, stale delivery statuses, missing backlinks, and ID integrity issues as errors.",
    )
    parser.add_argument(
        "--profile",
        choices=(
            "structural",
            "baseline",
            "happy-path",
            "interaction",
            "model-fit",
            "delivery",
            "full",
        ),
        default="structural",
        help="Validate one stage contract, or use 'full' for the complete requirement-to-delivery trace chain.",
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


def is_happy_path_id(stable_id: str) -> bool:
    return bool(re.fullmatch(r"FLOW-HP-[A-Z0-9]+", stable_id))


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


def is_confirmed_happy_path_status(value: str) -> bool:
    return normalize_header(value) in CONFIRMED_HAPPY_PATH_STATUSES


def is_flow_model_fit_layer(value: str) -> bool:
    normalized = normalize_header(value)
    return (
        "FLOW-MODEL" in normalized
        or "FLOW MODEL" in normalized
        or "流程模型" in normalized
    )


def is_representation_model_fit_layer(value: str) -> bool:
    normalized = normalize_header(value)
    return (
        "REPRESENTATION-MODEL" in normalized
        or "REPRESENTATION MODEL" in normalized
        or "界面表达模型" in normalized
        or "表达模型" in normalized
    )


def is_open_critical_uxgap(severity_value: str, resolution: str) -> bool:
    return (
        normalize_header(severity_value) in CRITICAL_UXGAP_SEVERITIES
        and normalize_header(resolution) not in CLOSED_CRITICAL_UXGAP_STATUSES
    )


def is_meaningful_rationale(value: str) -> bool:
    normalized = normalize_header(value)
    return normalized not in {
        "",
        "-",
        "—",
        "TBD",
        "TODO",
        "N/A",
        "NOT APPLICABLE",
        "待确认",
        "待补充",
        "不适用",
        "理由",
        "RATIONALE",
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
    rationale_column: int | None = None
    delivery_table = False
    ascii_queue_table = False
    happy_path_basis_table = False
    happy_path_adversarial_table = False
    happy_path_coverage_table = False
    happy_path_basis_required_columns: tuple[int, int] | None = None
    happy_path_adversarial_required_columns: tuple[int, int] | None = None
    model_fit_coverage_table = False
    model_fit_layer_column: int | None = None
    model_fit_result_column: int | None = None
    evidence_status_column: int | None = None
    model_fit_rationale_column: int | None = None
    uxgap_table = False
    uxgap_severity_column: int | None = None
    uxgap_resolution_column: int | None = None

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
            rationale_column = None
            delivery_table = False
            ascii_queue_table = False
            happy_path_basis_table = False
            happy_path_adversarial_table = False
            happy_path_coverage_table = False
            happy_path_basis_required_columns = None
            happy_path_adversarial_required_columns = None
            model_fit_coverage_table = False
            model_fit_layer_column = None
            model_fit_result_column = None
            evidence_status_column = None
            model_fit_rationale_column = None
            uxgap_table = False
            uxgap_severity_column = None
            uxgap_resolution_column = None
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
                happy_path_basis_columns = (
                    next(
                        (
                            index
                            for index, header in enumerate(table_headers)
                            if normalize_header(header) in HAPPY_PATH_BASIS_HEADERS
                        ),
                        None,
                    ),
                    next(
                        (
                            index
                            for index, header in enumerate(table_headers)
                            if normalize_header(header) in HAPPY_PATH_COMPLETION_HEADERS
                        ),
                        None,
                    ),
                )
                happy_path_basis_table = all(
                    column is not None for column in happy_path_basis_columns
                )
                happy_path_basis_required_columns = (
                    happy_path_basis_columns
                    if happy_path_basis_table
                    else None
                )
                happy_path_adversarial_columns = (
                    next(
                        (
                            index
                            for index, header in enumerate(table_headers)
                            if normalize_header(header) in ADVERSARIAL_CHALLENGE_HEADERS
                        ),
                        None,
                    ),
                    next(
                        (
                            index
                            for index, header in enumerate(table_headers)
                            if normalize_header(header) in ADVERSARIAL_IMPACT_HEADERS
                        ),
                        None,
                    ),
                )
                happy_path_adversarial_table = all(
                    column is not None for column in happy_path_adversarial_columns
                )
                happy_path_adversarial_required_columns = (
                    happy_path_adversarial_columns
                    if happy_path_adversarial_table
                    else None
                )
                status_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in STATUS_HEADERS
                    ),
                    None,
                )
                rationale_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in RATIONALE_HEADERS
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
                happy_path_coverage_table = bool(
                    HAPPY_PATH_COVERAGE_HEADERS & normalized_headers
                    and STATUS_HEADERS & normalized_headers
                    and RATIONALE_HEADERS & normalized_headers
                )
                model_fit_layer_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in MODEL_FIT_COVERAGE_HEADERS
                    ),
                    None,
                )
                model_fit_result_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in MODEL_FIT_RESULT_HEADERS
                    ),
                    None,
                )
                evidence_status_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in EVIDENCE_STATUS_HEADERS
                    ),
                    None,
                )
                model_fit_rationale_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in MODEL_FIT_RATIONALE_HEADERS
                    ),
                    None,
                )
                model_fit_coverage_table = all(
                    column is not None
                    for column in (
                        model_fit_layer_column,
                        model_fit_result_column,
                        evidence_status_column,
                    )
                )
                uxgap_severity_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in UXGAP_SEVERITY_HEADERS
                    ),
                    None,
                )
                uxgap_resolution_column = next(
                    (
                        index
                        for index, header in enumerate(table_headers)
                        if normalize_header(header) in UXGAP_RESOLUTION_HEADERS
                    ),
                    None,
                )
                uxgap_table = bool(
                    any(
                        normalize_header(header)
                        in {"UXGAP ID", "UX GAP ID", "UX 鸿沟 ID"}
                        for header in table_headers
                    )
                    and uxgap_severity_column is not None
                    and uxgap_resolution_column is not None
                )
            elif not is_separator_row(cells):
                add_row_edges(analysis, line_ids)
                happy_path_row_ids = {
                    stable_id for stable_id in line_ids if is_happy_path_id(stable_id)
                }
                basis_row_complete = bool(
                    happy_path_basis_table
                    and happy_path_basis_required_columns is not None
                    and all(
                        column < len(cells)
                        and is_meaningful_rationale(cells[column])
                        for column in happy_path_basis_required_columns
                    )
                )
                adversarial_row_complete = bool(
                    happy_path_adversarial_table
                    and happy_path_adversarial_required_columns is not None
                    and all(
                        column < len(cells)
                        and is_meaningful_rationale(cells[column])
                        for column in happy_path_adversarial_required_columns
                    )
                )
                if basis_row_complete:
                    for stable_id in happy_path_row_ids:
                        analysis.happy_path_basis_ids[stable_id].add(site)
                if adversarial_row_complete:
                    for stable_id in happy_path_row_ids:
                        analysis.happy_path_adversarial_ids[stable_id].add(site)
                defined_ids_in_row: set[str] = set()
                for column, allowed_prefixes in definition_columns.items():
                    if column >= len(cells):
                        continue
                    for stable_id in extract_ids(cells[column]):
                        if allowed_prefixes is None or prefix_of(stable_id) in allowed_prefixes:
                            analysis.definitions[stable_id].add(site)
                            defined_ids_in_row.add(stable_id)

                if ascii_queue_table and status_column is not None:
                    queue_status = cells[status_column].strip() if status_column < len(cells) else ""
                    analysis.ascii_queue_statuses.append((queue_status, site))

                if happy_path_coverage_table and status_column is not None:
                    coverage_status = (
                        cells[status_column].strip()
                        if status_column < len(cells)
                        else ""
                    )
                    coverage_rationale = (
                        cells[rationale_column].strip()
                        if rationale_column is not None and rationale_column < len(cells)
                        else ""
                    )
                    analysis.happy_path_coverage.append(
                        (coverage_status, coverage_rationale, site)
                    )

                if model_fit_coverage_table:
                    layer = (
                        cells[model_fit_layer_column].strip()
                        if model_fit_layer_column is not None
                        and model_fit_layer_column < len(cells)
                        else ""
                    )
                    result = (
                        cells[model_fit_result_column].strip()
                        if model_fit_result_column is not None
                        and model_fit_result_column < len(cells)
                        else ""
                    )
                    evidence_status = (
                        cells[evidence_status_column].strip()
                        if evidence_status_column is not None
                        and evidence_status_column < len(cells)
                        else ""
                    )
                    rationale = (
                        cells[model_fit_rationale_column].strip()
                        if model_fit_rationale_column is not None
                        and model_fit_rationale_column < len(cells)
                        else ""
                    )
                    analysis.model_fit_coverage.append(
                        (layer, result, evidence_status, rationale, set(line_ids), site)
                    )

                if uxgap_table:
                    severity_value = (
                        cells[uxgap_severity_column].strip()
                        if uxgap_severity_column is not None
                        and uxgap_severity_column < len(cells)
                        else ""
                    )
                    resolution = (
                        cells[uxgap_resolution_column].strip()
                        if uxgap_resolution_column is not None
                        and uxgap_resolution_column < len(cells)
                        else ""
                    )
                    for stable_id in defined_ids_in_row:
                        if prefix_of(stable_id) == "UXGAP":
                            analysis.uxgap_records[stable_id].append(
                                (severity_value, resolution, site)
                            )

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
                    elif (
                        stable_id.startswith("DEC-HAPPY-")
                        and stable_id in defined_ids_in_row
                    ):
                        confirmation_status = (
                            cells[status_column].strip()
                            if status_column is not None and status_column < len(cells)
                            else ""
                        )
                        analysis.happy_path_confirmation_statuses[stable_id].append(
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

                if len(cells) >= 2 and normalize_header(cells[0]) in DELIVERY_PROFILE_LABELS:
                    analysis.delivery_profiles.append((cells[1].strip(), site))

                if len(cells) >= 2 and normalize_header(cells[0]) in SPLIT_RATIONALE_LABELS:
                    analysis.split_rationales.append((cells[1].strip(), site))

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
            rationale_column = None
            delivery_table = False
            ascii_queue_table = False
            happy_path_basis_table = False
            happy_path_adversarial_table = False
            happy_path_coverage_table = False
            happy_path_basis_required_columns = None
            happy_path_adversarial_required_columns = None
            model_fit_coverage_table = False
            model_fit_layer_column = None
            model_fit_result_column = None
            evidence_status_column = None
            model_fit_rationale_column = None
            uxgap_table = False
            uxgap_severity_column = None
            uxgap_resolution_column = None

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
        if len(files) >= 4:
            findings.append(
                Finding(
                    severity(final),
                    "MISSING_INDEX",
                    target,
                    1,
                    "four-or-more-file Modular delivery requires index.md",
                )
            )
        return findings

    if len(files) <= 3:
        findings.append(
            Finding(
                severity(final),
                "UNNECESSARY_INDEX",
                index,
                1,
                "two-or-three-file delivery should use ux-requirements.md as the entry point instead of index.md",
            )
        )

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


def semantic_findings(
    analysis: Analysis,
    final: bool,
    profile: str,
    file_count: int = 1,
) -> list[Finding]:
    if profile == "structural":
        return []

    if profile != "full":
        full_findings = semantic_findings(
            analysis,
            final=final,
            profile="full",
            file_count=file_count,
        )
        included_stages = {
            "baseline": ("baseline",),
            "happy-path": ("baseline", "happy-path"),
            "interaction": ("baseline", "happy-path", "interaction", "model-fit"),
            "model-fit": ("model-fit",),
            "delivery": ("delivery",),
        }[profile]
        allowed_codes = set(COMMON_STAGE_CODES)
        for stage in included_stages:
            allowed_codes.update(STAGE_PROFILE_CODES[stage])

        findings = [
            Finding(
                item.severity,
                item.code,
                item.file,
                item.line,
                item.message.replace("full profile", f"{profile} profile"),
            )
            for item in full_findings
            if item.code in allowed_codes
        ]

        present_prefixes = {
            prefix_of(stable_id) for stable_id in analysis.definitions
        }
        fallback_file = next(
            (
                next(iter(sites)).file
                for sites in analysis.occurrences.values()
                if sites
            ),
            Path("."),
        )
        required_stages = included_stages if profile != "delivery" else ("delivery",)
        for stage in required_stages:
            for accepted_prefixes, label in STAGE_PROFILE_REQUIREMENTS[stage]:
                if not (accepted_prefixes & present_prefixes):
                    findings.append(
                        Finding(
                            severity(final),
                            "MISSING_STAGE_ARTIFACT",
                            fallback_file,
                            1,
                            f"{profile} profile has no canonical {label} definition",
                        )
                    )
        return findings

    findings: list[Finding] = []
    strict_severity = severity(final)

    if not analysis.delivery_profiles:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_DELIVERY_PROFILE",
                Path("."),
                1,
                "full profile requires Compact, Balanced, or Modular delivery profile",
            )
        )
    else:
        normalized_profiles = {
            normalize_header(value): site
            for value, site in analysis.delivery_profiles
        }
        if len(normalized_profiles) > 1:
            first_site = next(iter(normalized_profiles.values()))
            findings.append(
                Finding(
                    strict_severity,
                    "CONFLICTING_DELIVERY_PROFILE",
                    first_site.file,
                    first_site.line,
                    "delivery documents declare conflicting profiles: "
                    + ", ".join(sorted(normalized_profiles)),
                )
            )
        for normalized_profile, site in normalized_profiles.items():
            expected_range = DELIVERY_PROFILE_FILE_RANGES.get(normalized_profile)
            if expected_range is None:
                findings.append(
                    Finding(
                        strict_severity,
                        "INVALID_DELIVERY_PROFILE",
                        site.file,
                        site.line,
                        f"unknown or unresolved delivery profile: {normalized_profile or '(empty)'}",
                    )
                )
                continue
            minimum, maximum = expected_range
            if file_count < minimum or (maximum is not None and file_count > maximum):
                expected = f"{minimum}+" if maximum is None else (
                    str(minimum) if minimum == maximum else f"{minimum}-{maximum}"
                )
                findings.append(
                    Finding(
                        strict_severity,
                        "DELIVERY_PROFILE_MISMATCH",
                        site.file,
                        site.line,
                        f"{normalized_profile} expects {expected} Markdown file(s), found {file_count}",
                    )
                )

        non_compact_profiles = {
            profile_name
            for profile_name in normalized_profiles
            if profile_name in {"BALANCED", "平衡", "MODULAR", "模块化"}
        }
        meaningful_rationales = [
            (value, rationale_site)
            for value, rationale_site in analysis.split_rationales
            if normalize_header(value)
            not in {
                "",
                "NONE",
                "N/A",
                "NOT APPLICABLE",
                "无",
                "不适用",
                "INDEPENDENT OWNER/REVIEW/RELEASE/READABILITY REASON",
            }
            and "OTHERWISE" not in normalize_header(value)
        ]
        if non_compact_profiles and not meaningful_rationales:
            first_site = next(iter(normalized_profiles.values()))
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_SPLIT_RATIONALE",
                    first_site.file,
                    first_site.line,
                    "Balanced or Modular delivery requires a specific reader, owner, review, release, or readability rationale",
                )
            )

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

    if not analysis.model_fit_coverage:
        findings.append(
            Finding(
                strict_severity,
                "MISSING_MODEL_FIT_COVERAGE",
                fallback_file,
                1,
                "full profile requires target-user model-fit review coverage",
            )
        )
    else:
        if {"FLOW", "INT"} & present_prefixes and not any(
            is_flow_model_fit_layer(layer)
            for layer, _result, _evidence, _rationale, _ids, _site
            in analysis.model_fit_coverage
        ):
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_FLOW_MODEL_FIT_REVIEW",
                    fallback_file,
                    1,
                    "full profile has FLOW/INT definitions but no flow-model fit coverage row",
                )
            )
        if {"UI", "STATE"} & present_prefixes and not any(
            is_representation_model_fit_layer(layer)
            for layer, _result, _evidence, _rationale, _ids, _site
            in analysis.model_fit_coverage
        ):
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_REPRESENTATION_MODEL_FIT_REVIEW",
                    fallback_file,
                    1,
                    "full profile has UI/STATE definitions but no representation-model fit coverage row",
                )
            )

        for (
            layer,
            result,
            evidence,
            rationale,
            ids,
            coverage_site,
        ) in analysis.model_fit_coverage:
            prefixes = {prefix_of(stable_id) for stable_id in ids}
            if not result.strip() or not evidence.strip():
                findings.append(
                    Finding(
                        strict_severity,
                        "INCOMPLETE_MODEL_FIT_COVERAGE",
                        coverage_site.file,
                        coverage_site.line,
                        "model-fit coverage requires non-empty result and evidence status",
                    )
                )
            if "ROLE" not in prefixes or "SCN" not in prefixes:
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_MODEL_FIT_COVERAGE",
                        coverage_site.file,
                        coverage_site.line,
                        "model-fit coverage must reference an explicit ROLE and SCN",
                    )
                )
            if is_flow_model_fit_layer(layer) and not ({"FLOW", "INT"} & prefixes):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_MODEL_FIT_COVERAGE",
                        coverage_site.file,
                        coverage_site.line,
                        "flow-model fit coverage must reference affected FLOW or INT IDs",
                    )
                )
            if is_representation_model_fit_layer(layer) and not ({"UI", "STATE"} & prefixes):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_MODEL_FIT_COVERAGE",
                        coverage_site.file,
                        coverage_site.line,
                        "representation-model fit coverage must reference affected UI or STATE IDs",
                    )
                )
            if (
                normalize_header(result) in MODEL_FIT_WAIVER_RESULTS
                and not is_meaningful_rationale(rationale)
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "MISSING_MODEL_FIT_RATIONALE",
                        coverage_site.file,
                        coverage_site.line,
                        f"model-fit result {result or '(empty)'} requires a concrete rationale or limitation",
                    )
                )

    happy_path_ids = sorted(
        stable_id
        for stable_id in analysis.definitions
        if is_happy_path_id(stable_id)
    )

    waiver_entries = [
        (status, rationale, site)
        for status, rationale, site in analysis.happy_path_coverage
        if normalize_header(status) in HAPPY_PATH_WAIVER_STATUSES
    ]
    valid_waivers = [
        entry for entry in waiver_entries if is_meaningful_rationale(entry[1])
    ]
    for waiver_status, waiver_rationale, waiver_site in waiver_entries:
        if not is_meaningful_rationale(waiver_rationale):
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_HAPPY_PATH_WAIVER_RATIONALE",
                    waiver_site.file,
                    waiver_site.line,
                    f"happy-path coverage status {waiver_status or '(empty)'} requires a concrete rationale",
                )
            )

    if not happy_path_ids:
        if not valid_waivers and not waiver_entries:
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_HAPPY_PATH",
                    fallback_file,
                    1,
                    "full profile requires a canonical FLOW-HP happy path or a Blocked/Not applicable coverage record with rationale",
                )
            )

    confirmed_happy_path_decisions = {
        stable_id
        for stable_id, statuses in analysis.happy_path_confirmation_statuses.items()
        if any(is_confirmed_happy_path_status(status) for status, _site in statuses)
    }

    for stable_id in happy_path_ids:
        first = sorted(
            analysis.definitions[stable_id],
            key=lambda site: (str(site.file), site.line),
        )[0]
        if stable_id not in analysis.happy_path_basis_ids:
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_HAPPY_PATH_BASIS",
                    first.file,
                    first.line,
                    f"{stable_id} has no first-principles basis row linked by ID",
                )
            )
        if stable_id not in analysis.happy_path_adversarial_ids:
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_HAPPY_PATH_ADVERSARIAL_REVIEW",
                    first.file,
                    first.line,
                    f"{stable_id} has no adversarial-review row linked by ID",
                )
            )
        if not reachable_prefix(
            stable_id, {"SCN", "REQ", "TASK"}, analysis.edges
        ):
            findings.append(
                Finding(
                    strict_severity,
                    "ORPHAN_HAPPY_PATH_UPSTREAM",
                    first.file,
                    first.line,
                    f"{stable_id} does not trace to SCN/REQ/TASK",
                )
            )
        if not reachable_prefix(stable_id, {"US", "JS"}, analysis.edges):
            findings.append(
                Finding(
                    strict_severity,
                    "ORPHAN_HAPPY_PATH_STORY",
                    first.file,
                    first.line,
                    f"{stable_id} does not trace to a user/job story",
                )
            )
        direct_happy_path_decisions = {
            neighbor
            for neighbor in analysis.edges.get(stable_id, set())
            if neighbor.startswith("DEC-HAPPY-")
        }
        if not direct_happy_path_decisions:
            findings.append(
                Finding(
                    strict_severity,
                    "MISSING_HAPPY_PATH_CONFIRMATION",
                    first.file,
                    first.line,
                    f"{stable_id} is not directly covered by a DEC-HAPPY confirmation record",
                )
            )
        elif not (direct_happy_path_decisions & confirmed_happy_path_decisions):
            observed_statuses = sorted(
                {
                    status or "(empty)"
                    for decision_id in direct_happy_path_decisions
                    for status, _site in analysis.happy_path_confirmation_statuses.get(
                        decision_id, []
                    )
                }
            )
            findings.append(
                Finding(
                    strict_severity,
                    "UNCONFIRMED_HAPPY_PATH",
                    first.file,
                    first.line,
                    f"{stable_id} is linked only to non-confirmed DEC-HAPPY records: "
                    + (", ".join(observed_statuses) if observed_statuses else "(no status)"),
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
        elif stable_prefix == "UXGAP":
            records = analysis.uxgap_records.get(stable_id, [])
            if not records or any(
                not severity_value.strip() or not resolution.strip()
                for severity_value, resolution, _site in records
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "INCOMPLETE_UXGAP_RECORD",
                        first.file,
                        first.line,
                        f"{stable_id} requires explicit severity and resolution/status",
                    )
                )
            if not (
                reachable_prefix(stable_id, {"ROLE"}, analysis.edges)
                and reachable_prefix(stable_id, {"SCN"}, analysis.edges)
                and reachable_prefix(
                    stable_id, {"FLOW", "INT", "UI", "STATE"}, analysis.edges
                )
            ):
                findings.append(
                    Finding(
                        strict_severity,
                        "ORPHAN_UXGAP_CONTEXT",
                        first.file,
                        first.line,
                        f"{stable_id} must trace to ROLE, SCN, and an affected FLOW/INT/UI/STATE",
                    )
                )
            open_critical = any(
                is_open_critical_uxgap(severity_value, resolution)
                for severity_value, resolution, _site in records
            )
            if open_critical:
                findings.append(
                    Finding(
                        strict_severity,
                        "OPEN_CRITICAL_UXGAP",
                        first.file,
                        first.line,
                        f"{stable_id} is Critical and must be Resolved or Superseded before final confirmation",
                    )
                )
                affected_ui_ids = {
                    neighbor
                    for neighbor in analysis.edges.get(stable_id, set())
                    if prefix_of(neighbor) in {"UI", "STATE"}
                }
                if any(
                    analysis.edges.get(ui_id, set()) & confirmed_ascii_decisions
                    for ui_id in affected_ui_ids
                ):
                    findings.append(
                        Finding(
                            strict_severity,
                            "CONFIRMED_ASCII_WITH_OPEN_CRITICAL_UXGAP",
                            first.file,
                            first.line,
                            f"{stable_id} affects UI/STATE already covered by a confirmed DEC-ASCII record",
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
        semantic_findings(analysis, args.final, args.profile, len(files))
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
