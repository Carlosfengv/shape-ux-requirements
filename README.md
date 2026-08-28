# UX 需求梳理工具集

面向复杂企业产品的多 Skill 工具集。它把原来单一、较重的需求梳理流程拆成四个可独立调用的专业阶段，并保留一个端到端编排入口。

## Skill 组成

| Skill | 负责什么 | 主要产物 |
| --- | --- | --- |
| `$shape-ux-requirements` | 跨阶段编排与确认门控制 | 一份持续演进的端到端需求文档 |
| `$shape-requirement-baseline` | 仓库证据、输入评估、问题框定、用户/场景、术语、需求与 Stories | `DEC-BASELINE` 确认的需求基线 |
| `$shape-happy-paths` | 第一性原理推导、对抗性审查、成功路径分支与确认 | `FLOW-HP`、`DEC-HAPPY` |
| `$shape-ascii-interactions` | 功能点、IA、任务流、交互逻辑、ASCII UI/状态及逐项确认 | `FUNC/IA/FLOW/INT/UI/STATE`、`DEC-ASCII` |
| `$deliver-ux-requirements` | 规格、验收、追踪、Markdown 组装、校验、Review 与交付 | `SPEC/SYS/AC/NFR`、最终文件与交付摘要 |

每个专业 Skill 都可以单独触发。只有请求跨越多个阶段时，才需要加载编排入口。

## 端到端流程

```text
仓库与来源证据
      ↓
需求/Story 基线 ── DEC-BASELINE
      ↓
Happy Path 推导与审查 ── DEC-HAPPY
      ↓
IA、流程和 ASCII 交互 ── DEC-ASCII
      ↓
规格、验收、追踪、校验与交付
```

每个确认门都必须同时提供修改路径和明确的下一阶段。上游确认不能自动替代下游确认；确认后的 ID 和决定会通过共享 artifact contract 继续传递。

## 主要能力

- 优先检查可用仓库中的代码、测试、文档、文案、模型、权限和状态，而不是只复述用户输入。
- 区分当前实现、文档意图、请求行为和最终差异，并标注事实、决定、推断、假设、未知与冲突。
- 将工程术语转换为不改变技术含义的用户语言。
- 在页面设计前确认问题、目标用户、场景、范围、需求和完整 Stories。
- 从用户结果和不可删除的约束推导 Happy Path，不默认沿用当前页面顺序。
- 对角色、权限、数据、生命周期、等待、跨角色协作和完成信号进行对抗性审查。
- 用 ASCII 表达信息层级、任务流、决策、异步协作、页面结构和用户可见状态。
- 把行为连接到规格、系统契约、验收标准和端到端追踪关系。
- 默认生成一份 `ux-requirements.md`；只有独立所有权、评审、发布或明显阅读负担时才拆文件。

## 安装

### 作为 Plugin 分发

仓库根目录已经包含标准 `.codex-plugin/plugin.json`，`skills/` 下包含全部五个 Skill。将该目录放入个人或团队 marketplace 的 `plugins/shape-ux-requirements` 后即可作为一个 Plugin 安装。

Plugin 和 marketplace 的结构以 [OpenAI 官方 Plugin 文档](https://developers.openai.com/plugins/build/plugins) 为准。

### 本地直接使用 Skills

克隆仓库：

```bash
git clone https://github.com/Carlosfengv/shape-ux-requirements.git
```

将 `skills/` 下的每个 Skill 目录链接到个人 Skill 目录：

```bash
mkdir -p ~/.agents/skills
ln -s /absolute/path/shape-ux-requirements/skills/shape-ux-requirements ~/.agents/skills/shape-ux-requirements
ln -s /absolute/path/shape-ux-requirements/skills/shape-requirement-baseline ~/.agents/skills/shape-requirement-baseline
ln -s /absolute/path/shape-ux-requirements/skills/shape-happy-paths ~/.agents/skills/shape-happy-paths
ln -s /absolute/path/shape-ux-requirements/skills/shape-ascii-interactions ~/.agents/skills/shape-ascii-interactions
ln -s /absolute/path/shape-ux-requirements/skills/deliver-ux-requirements ~/.agents/skills/deliver-ux-requirements
```

Codex 支持符号链接并会自动检测 Skill 变更；如未显示，重启 Codex。目录发现规则见 [OpenAI 官方 Skills 文档](https://developers.openai.com/codex/skills)。

### 旧安装兼容

根目录的 `SKILL.md` 仍是 `$shape-ux-requirements` 兼容入口。旧方式把整个仓库克隆到个人 Skill 目录时，端到端调用仍可工作，但四个专业 Skill 不一定会作为独立名称显示；建议迁移到 Plugin 或上述五个链接。

## 调用示例

只建立需求基线：

```text
请使用 $shape-requirement-baseline 分析这个需求和当前仓库，
形成可确认的需求与 Story 基线，先不要设计页面。
```

只审查 Happy Path：

```text
请使用 $shape-happy-paths 基于已确认基线推导主要成功路径，
进行第一性原理和对抗性审查，先不要进入页面与 ASCII UI。
```

只做交互：

```text
请使用 $shape-ascii-interactions 把已确认的需求和 FLOW-HP
转换为 IA、任务流和逐项确认的 ASCII 交互。
```

只做最终交付：

```text
请使用 $deliver-ux-requirements 整理现有确认结果，
补齐规格、验收、追踪、校验和最终交付摘要。
```

端到端编排：

```text
请使用 $shape-ux-requirements 从仓库证据开始梳理该需求，
并在 Baseline、Happy Path 和 ASCII 三个确认门分别等待我确认。
```

## 文档校验

根目录保留兼容命令，实际实现属于 `$deliver-ux-requirements`：

```bash
python3 scripts/validate_requirement_docs.py path/to/requirements.md
```

可以按阶段使用更精确的 profile：

```bash
python3 scripts/validate_requirement_docs.py path/to/requirements.md --final --profile baseline
python3 scripts/validate_requirement_docs.py path/to/requirements.md --final --profile happy-path
python3 scripts/validate_requirement_docs.py path/to/requirements.md --final --profile interaction
python3 scripts/validate_requirement_docs.py path/to/requirements.md --final --profile delivery
python3 scripts/validate_requirement_docs.py path/to/requirements.md --final --profile full
```

| Profile | 检查范围 |
| --- | --- |
| `structural` | Markdown、链接、占位符和基础结构 |
| `baseline` | 基线所需实体、Story 上游追踪和 `DEC-BASELINE` |
| `happy-path` | Baseline 加 `FLOW-HP` 依据、对抗审查、确认或豁免理由 |
| `interaction` | Happy Path 加功能分解、IA、ASCII、交互与 `DEC-ASCII` |
| `delivery` | Delivery profile、规格、验收、Review 和真实文件结构 |
| `full` | 全阶段契约和端到端追踪 |

校验器只能验证确定性的文档结构，不能替代对证据质量、产品决定、用户结果、可用性和无障碍约束的人工 Review。

## 仓库结构

```text
shape-ux-requirements/
├── .codex-plugin/plugin.json
├── skills/
│   ├── shape-ux-requirements/
│   ├── shape-requirement-baseline/
│   ├── shape-happy-paths/
│   ├── shape-ascii-interactions/
│   └── deliver-ux-requirements/
├── scripts/validate_requirement_docs.py
├── tests/
└── SKILL.md
```

根 `SKILL.md` 和根校验脚本都是兼容层；新功能应进入对应专业 Skill。
