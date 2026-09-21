# 示例：YunaiV/ruoyi-vue-pro

这是用本仓库 Skill 对 [YunaiV/ruoyi-vue-pro](https://github.com/YunaiV/ruoyi-vue-pro) 做的一次完整分析产物。打开 [00-index.html](00-index.html) 作为总册；左侧为可检索目录索引，可跳到分册、章节、模块和每一张主库表。

## 证据边界

- 仓库：https://github.com/YunaiV/ruoyi-vue-pro
- 提交：`8e80602b875f69158faf4c92445e67691821bf0f`
- 描述：`v2026.08(jdk8/11)-47-g8e80602b87`
- 分支：`master`（分析时与 `origin/master` 一致）

报告只描述该提交的仓库状态。README 功能清单、演示站和默认 Maven 反应堆并不等同，总册里写了分层证据。

## 分册

| 文件 | 内容 |
| --- | --- |
| [00-index.html](00-index.html) | 总册：范围与证据、目录索引、核验计数 |
| [01-platform-system-infra.html](01-platform-system-infra.html) | 平台分册：system + infra 需求、设计、ER、字段、接口 |
| [02-business-modules.html](02-business-modules.html) | 业务分册：Mall / CRM / ERP / MES 等源码模块 |

## 怎么看

```bash
python -m http.server 8765
```

然后打开 `http://127.0.0.1:8765/00-index.html`。部分浏览器对 `file://` 限制跨 HTML 锚点跳转。

打印时，粘性侧栏会作为第一页目录输出。
