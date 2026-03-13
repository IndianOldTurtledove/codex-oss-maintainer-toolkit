# Codex OSS Maintainer Toolkit

[中文](README.md) | [English](README_EN.md)

一个面向开源维护者的 Codex-first 工具仓库，用来把项目重构成适合 `Codex + AGENTS.md + 可复用 Skills` 的维护工作流。

## 这是什么？

这个仓库现在包含 5 类能力：

1. **Codex 维护 Skill**：指导如何把仓库整理成适合 Codex 使用的维护环境
2. **AGENTS.md 模板**：为项目补充清晰、可执行的 Codex 指令入口
3. **自动化脚本模板**：为 issue triage、debug、校验、文件检查提供可复用脚本
4. **Maintainer Agent Prompts**：PR review、错误排查等子任务提示词模板
5. **Dev Docs 模板**：跨会话保留上下文，方便持续维护复杂任务

## 仓库定位

推荐把公开仓库名称发布为：`codex-oss-maintainer-toolkit`

这个仓库不再是旧品牌专用基础设施；它现在专注于：

- Codex-native 项目规范
- AGENTS.md 落地
- 开源维护自动化
- Skill authoring 与校验
- PR review / issue triage / release notes 工作流

## 快速开始

### 1）本地克隆后直接使用

```bash
git clone https://github.com/IndianOldTurtledove/codex-oss-maintainer-toolkit.git
cd codex-oss-maintainer-toolkit
```

### 2）作为全局 Codex Skill 安装

```bash
./install.sh --global --yes
```

默认会安装到：

```bash
~/.codex/skills/codex-oss-maintainer-toolkit
```

### 3）为某个仓库生成 Codex 维护骨架

```bash
./install.sh --project --target /path/to/your/repo --yes
```

会生成这些内容：

```text
/path/to/your/repo/
├── AGENTS.md
├── .codex/
│   ├── agents/
│   ├── automation/
│   └── skills/
│       └── skill-rules.json
└── dev/
    ├── active/
    └── archive/
```

## 主要功能

### 1. Codex 维护 Skill

```bash
python3 scripts/init_skill.py issue-triage
python3 scripts/quick_validate.py .codex/skills/issue-triage
python3 scripts/package_skill.py .codex/skills/issue-triage
```

### 2. 自动化脚本模板

位于 `templates/automation/`，可以直接拷到你的项目里。

| Script | 用途 |
|--------|------|
| `recommend-skills.py` | 根据提示词推荐本地 skill |
| `debug-task-detector.py` | 检测是否应该进入系统化排障流程 |
| `investigate-change.py` | 修改前生成调查清单 |
| `suggest-checks.py` | 根据改动文件推荐验证命令 |
| `file-size-check.py` | 检查超大文件 |
| `verify-changed-files.sh` | 对 git diff 中的文件做基础校验 |

### 3. AGENTS.md 模板

`templates/AGENTS.md` 提供一份项目模板，重点覆盖：

- 仓库地图
- 读后改原则
- 校验要求
- 维护者工作流
- 技术债和风险的记录方式

### 4. Maintainer Agent Prompts

`templates/agents/` 提供可直接改造的子任务模板：

- `code-reviewer.md`
- `error-resolver.md`

### 5. Dev Docs 系统

`templates/dev-docs/` 用来保存：

- 计划
- 会话进度
- 任务清单
- 下次接手的上下文

## 项目结构

```text
codex-oss-maintainer-toolkit/
├── AGENTS.md
├── SKILL.md
├── install.sh
├── scripts/
│   ├── init_skill.py
│   ├── quick_validate.py
│   └── package_skill.py
├── references/
│   ├── output-patterns.md
│   └── workflows.md
├── templates/
│   ├── AGENTS.md
│   ├── agents/
│   ├── automation/
│   ├── dev-docs/
│   └── skill-rules.json
├── examples/
│   └── full-project/
└── demo/
```

## 设计原则

1. **Codex-first**：优先围绕 AGENTS.md、skills、可验证脚本来组织仓库
2. **Maintainer-centric**：解决开源维护中的高频重复工作
3. **Minimal but reusable**：核心说明放在主文件，细节拆到 references/
4. **Prove it**：每个工作流都应该有明确的验证命令

## 建议的申请角度

如果你计划申请 OpenAI 的 Codex for Open Source，建议突出：

- 你在做真实的开源维护工作流沉淀
- 这个仓库能帮助维护者减少 triage / review / release 负担
- 它基于 Codex 的原生工作方式（AGENTS.md + skills + automation）

## 验证命令

```bash
python3 scripts/quick_validate.py .
python3 scripts/init_skill.py demo-skill --path /tmp/codex-skills
python3 scripts/package_skill.py /tmp/codex-skills/demo-skill /tmp
bash install.sh --help
rg -n -i "legacy-brand|legacy-hook|legacy-config" .
```

## 许可证

MIT License. See [LICENSE](LICENSE).
