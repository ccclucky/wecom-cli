from __future__ import annotations

import json

from scripts.build_agent_tasks import build_agent_tasks


def test_build_agent_tasks_creates_missing_task_with_drafts(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "contacts.yaml").write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [],
            }
        ),
        encoding="utf-8",
    )

    catalog = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "id": "contacts.list_users",
                "domain": "contacts",
                "name": "list_users",
                "endpoint": "/cgi-bin/user/simplelist",
                "method": "GET",
                "doc": {
                    "title": "获取部门成员",
                    "source_url": "u1",
                    "request_params": [
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                        {"name": "department_id", "required": True, "description": "部门 ID"},
                    ],
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                        {"name": "errmsg", "description": "返回信息"},
                    ],
                    "response_example_json": {"errcode": 0, "errmsg": "ok"},
                },
            }
        ],
    }

    payload = build_agent_tasks(catalog, spec_dir)
    assert payload["task_count"] == 1
    task = payload["tasks"][0]
    assert task["status"] == "missing"
    assert task["priority"] == "high"
    assert task["target_spec"] == "specs/wecom/contacts.yaml"
    assert task["draft"]["request"]["query"]["department_id"] == {"from_arg": "department_id"}
    assert task["draft"]["output"]["json_schema"]["properties"]["errcode"]["type"] == "integer"


def test_build_agent_tasks_skips_fully_implemented_operations(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "contacts.yaml").write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [
                    {
                        "name": "list_users",
                        "summary": "获取部门成员",
                        "method": "GET",
                        "endpoint": "/cgi-bin/user/simplelist",
                        "args": [{"name": "department_id"}],
                        "request": {"query": {"department_id": {"from_arg": "department_id"}}},
                        "output": {
                            "formats": ["json"],
                            "json_schema": {
                                "type": "object",
                                "properties": {"errcode": {"type": "integer"}},
                            },
                        },
                        "examples": ["ok"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    catalog = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "id": "contacts.list_users",
                "domain": "contacts",
                "name": "list_users",
                "endpoint": "/cgi-bin/user/simplelist",
                "method": "GET",
                "doc": {
                    "title": "获取部门成员",
                    "request_params": [
                        {"name": "department_id", "required": True, "description": "部门 ID"},
                    ],
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                    ],
                    "response_example_json": {"errcode": 0},
                },
            }
        ],
    }

    payload = build_agent_tasks(catalog, spec_dir)
    assert payload["task_count"] == 0


def test_build_agent_tasks_marks_post_review_required(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "messages.yaml").write_text(
        json.dumps(
            {
                "domain": "messages",
                "operations": [
                    {
                        "name": "send_text",
                        "summary": "发送文本消息",
                        "method": "POST",
                        "endpoint": "/cgi-bin/message/send",
                        "args": [],
                        "request": {},
                        "examples": ["ok"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    catalog = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "id": "messages.send_text",
                "domain": "messages",
                "name": "send_text",
                "endpoint": "/cgi-bin/message/send",
                "method": "POST",
                "doc": {
                    "title": "发送应用消息",
                    "request_params": [
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                    ],
                    "request_example_json": {"touser": "zhangsan", "msgtype": "text"},
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                    ],
                    "response_example_json": {"errcode": 0},
                },
            }
        ],
    }

    payload = build_agent_tasks(catalog, spec_dir)
    assert payload["task_count"] == 1
    task = payload["tasks"][0]
    assert task["status"] == "incomplete"
    assert task["review_hints"]
    assert task["confidence"] < 0.7


def test_build_agent_tasks_includes_removed_cleanup_tasks(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "customers.yaml").write_text(
        json.dumps(
            {
                "domain": "customers",
                "operations": [
                    {
                        "name": "list_follow_users",
                        "summary": "列出配置了客户联系的成员",
                        "method": "GET",
                        "endpoint": "/cgi-bin/externalcontact/get_follow_user_list",
                        "args": [],
                        "request": {},
                        "examples": ["ok"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    catalog = {
        "snapshot_date": "2026-04-23",
        "operations": [],
    }
    diff = {
        "discovery_snapshot": "2026-04-24",
        "removed": [
            {
                "endpoint": "/cgi-bin/externalcontact/get_follow_user_list",
                "method": "GET",
            }
        ],
    }

    payload = build_agent_tasks(catalog, spec_dir, diff)
    assert payload["task_count"] == 1
    task = payload["tasks"][0]
    assert task["status"] == "remove"
    assert task["change_type"] == "removed"
    assert task["target_spec"] == "specs/wecom/customers.yaml"
