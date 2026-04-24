# 生成式接口示例（specs/wecom）

以下示例来自 `specs/wecom/*.yaml`，由 `python scripts/codegen.py` 生成 CLI 命令与 API client。

## contacts.list_users

```bash
wecom contacts list --department-id 1 --fetch-child
```

## messages.send_text

```bash
wecom messages send-text --to-user zhangsan --agent-id 1000002 --content "hello"
```

## customers.list_follow_users

```bash
wecom customers list-follow-users
```
