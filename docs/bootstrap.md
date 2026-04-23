# WeCom CLI 初始化说明

## 目录结构

```text
core/      # 配置、鉴权、请求器、统一错误
cli/       # 命令入口与路由
apis/      # 各业务域 API 适配层
models/    # 共享模型
tests/     # 单元测试
docs/      # 文档
```

## 已实现核心能力

- 配置加载：支持环境变量 + `~/.wecom-cli/config.json`。
- 鉴权：统一 `access_token` 获取与内存缓存。
- 请求器：统一 URL 拼装、鉴权注入、JSON 解析、错误转换。
- 错误处理：统一基础错误与 API 错误语义。

## 高频域命令（首批）

- `wecom contacts list`
- `wecom messages send-text`
- `wecom customers list-follow-users`

## 本地运行

```bash
python -m cli.main --help
```
