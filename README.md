# 软件工程全景报告

这是一个面向 Codex / Cursor 等 Agent 的 [Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)：根据**当前仓库的真实证据**，生成一份可独立打开的 UTF-8 HTML **软件工程现状报告**。

它不凭印象画架构，也不把附件、截图或示例接口文档当成必须照抄的模板。报告里的页面、接口、表、类、测试和部署结论，都要能追溯到源码、迁移、配置、已执行的检查，或只读访问过的线上环境。

## 这个 Skill 做什么

当你需要「这份系统现在到底长什么样」的工程文档时，Agent 会：

1. 锁定证据边界：仓库根目录、当前提交、分支或标签、远程地址、工作区是否有未纳入版本的改动。
2. 盘点前端路由与页面、后端接口与类层次、数据库迁移与物理表、测试与部署文件。
3. 把重要业务从页面操作一路追到 API、鉴权、事务、持久化和失败态。
4. 按规格写出完整报告：需求分析、系统设计、数据库与 ER、页面清单、接口与类、测试、部署与运维。
5. 交付**单文件 HTML**（CSS / JavaScript 内嵌），不依赖 CDN，不在运行时去拉本地数据。每份报告带可检索的**目录索引**（分册、章节、模块、物理表锚点），打印时作为首页目录。

显示名称：**软件工程全景报告**。Skill 目录名：`project-engineering-report`。

## 适合用 / 不适合用

**适合：**

- 当前版本的项目现状报告、软件生命周期说明
- 数据库 / ER 文档、接口与类设计说明
- 页面盘点，或按模块拆成多份独立报告

**不适合：**

- 普通 Code Review
- 只做推测性架构规划、还没有可核对证据的方案讨论

## 报告里会写什么

完整报告按下面结构组织（项目不同可以改标题，但不能因为证据散落在多个模块就整章省略）：

| 章节 | 内容 |
| --- | --- |
| 范围与证据 | 产品名、目标版本、commit、分支/标签、证据来源与边界 |
| 需求分析 | 用户、角色、权限、主路径、功能目录、业务规则；推断之处必须标明 |
| 系统设计 | 运行拓扑、模块边界、前后端职责、鉴权、事务与关键时序 |
| 数据库设计 | 表/列/外键/索引统计、每张表的字段说明、Crow's Foot ER 图 |
| 前端页面 | 页面组件数与可达路由数分别统计，含空态、失败态、权限态 |
| 接口与类 | 约定、完整端点目录、关键接口定义、真实类调用链 |
| 测试与质量 | 只报告实际跑过的检查，并区分静态阅读与运行时验证 |
| 部署与运维 | 构建、配置、进程、存储、备份与可观察性中有证据的部分 |
| 附录 | 目录树、术语、未核实项与已知缺口 |

ER 图使用 Crow's Foot 基数，同时给出物理表名与中文业务名，标出主键、外键和 SQL 类型。图不能代替字段表。

多模块、用户路径或数据模型明显不同时，应为各模块各出一份独立 HTML，共享的登录、媒体、基础设施在各报告里写成外部依赖，而不是假装本模块拥有它们。

## 证据原则（摘要）

- 只描述**当前系统状态**。迭代史、废弃方案、规划中的行为，除非你明确要求，否则不写。
- 源码、迁移、配置、测试、远程仓库、线上站点如果互相矛盾，要写清楚不确定点，而不是选一个看起来圆的说法。
- 线上环境只用只读请求探查；不写入报告凭据、令牌、私有配置和个人数据。
- 附件与截图默认是参考，不是指令。
- 交付前要核对总数、锚点、检索/筛选、打印样式、内嵌脚本和 SVG 是否为空，并在本地打开确认中文与图表正常。

更细的规则见 `references/`。

## 仓库结构

```text
.
├── SKILL.md                              # Skill 入口：何时启用、如何取证、如何写报告
├── agents/openai.yaml                    # Codex 显示名与默认提示
├── examples/
│   └── ruoyi-vue-pro/                    # 一次完整分析示例（独立 HTML）
├── references/
│   ├── report-spec.md                    # 报告章节规格
│   ├── evidence-and-verification.md      # 仓库对比与线上只读核验
│   └── er-and-class-design.md            # ER 图与类设计约定
└── scripts/
    └── extract_flyway_schema.py          # 从 Flyway 迁移抽出初始表结构清单
```

`extract_flyway_schema.py` 只做 Flyway 的初步盘点。生成报告前仍需人工（由 Agent）核对厂商方言、重命名、动态 SQL、触发器、视图和跨表规则。

## 安装

把本仓库放到 Agent 会扫描的 skills 目录，目录名建议保持为 `project-engineering-report`。

**Codex**

```bash
git clone https://github.com/LingXI5499/project-engineering-report-skills.git ~/.codex/skills/project-engineering-report
```

Windows 示例：

```powershell
git clone https://github.com/LingXI5499/project-engineering-report-skills.git "$env:USERPROFILE\.codex\skills\project-engineering-report"
```

**Cursor**

```powershell
git clone https://github.com/LingXI5499/project-engineering-report-skills.git "$env:USERPROFILE\.cursor\skills\project-engineering-report"
```

安装后新开一轮对话，或确认该 Skill 已出现在可用 skills 列表中。

## 怎么用

在目标项目仓库里直接说，例如：

- 「按 project-engineering-report 给当前项目出一份软件工程现状 HTML 报告」
- 「只出数据库和 ER 文档」
- 「按模块各出一份独立报告」

也可以使用 `agents/openai.yaml` 里的默认提示：

```text
Use $project-engineering-report to inspect this project and generate a current-state HTML engineering report.
```

生成结果应是可双击打开的 HTML 文件，带可检索目录索引；目录与检索在打印时仍可读。

## 分析示例

[examples/ruoyi-vue-pro](examples/ruoyi-vue-pro) 是对本 Skill 的一次完整使用结果：分析 [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) 检出 `8e80602b875f`（`v2026.08(jdk8/11)-47-g8e80602b87`，`master`）。

| 文件 | 内容 |
| --- | --- |
| [00-index.html](examples/ruoyi-vue-pro/00-index.html) | 总册：证据边界、分册/章节/模块/主库表目录索引、核验计数 |
| [01-platform-system-infra.html](examples/ruoyi-vue-pro/01-platform-system-infra.html) | 平台分册：默认启用的 system + infra |
| [02-business-modules.html](examples/ruoyi-vue-pro/02-business-modules.html) | 业务分册：源码中存在、默认未接入 Maven 的模块 |

建议在该目录执行 `python -m http.server` 后打开总册，避免部分浏览器限制 `file://` 跨文件锚点。

## 许可

本仓库未附带许可证文件。使用、修改或再发布前请与仓库所有者确认。
