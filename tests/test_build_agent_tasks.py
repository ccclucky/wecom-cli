from __future__ import annotations

import json

from scripts.build_agent_tasks import _render_prompt, build_agent_tasks


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
    assert task["status"] == "review_required"
    assert task["change_type"] == "removed"
    assert task["target_spec"] == "specs/wecom/customers.yaml"
    assert "Do not delete it automatically" in task["review_hints"][0]


def test_render_prompt_forbids_unconfirmed_deletion(tmp_path):
    prompt = _render_prompt(tmp_path / "artifacts" / "implementation.tasks.yaml")
    assert "Treat `artifacts/implementation.tasks.yaml` as authoritative." in prompt
    assert "do not delete files or prune operations unless a human explicitly confirms removal" in prompt
    assert "If `target_spec` is null, report the task as blocked" in prompt


def test_build_agent_tasks_reuses_existing_spec_by_endpoint_when_catalog_id_is_stale(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "departments.yaml").write_text(
        json.dumps(
            {
                "domain": "departments",
                "operations": [
                    {
                        "name": "delete",
                        "summary": "删除部门",
                        "method": "GET",
                        "endpoint": "/cgi-bin/department/delete",
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
                "id": "todo.cgi_bin_department_delete",
                "domain": "unknown",
                "name": "cgi_bin_department_delete",
                "endpoint": "/cgi-bin/department/delete",
                "method": "GET",
                "doc": {
                    "title": "删除部门",
                    "response_example_json": {"errcode": 0, "errmsg": "ok"},
                },
            }
        ],
    }
    diff = {
        "discovery_snapshot": "2026-04-24",
        "added": [{"endpoint": "/cgi-bin/department/delete", "method": "GET"}],
    }

    payload = build_agent_tasks(catalog, spec_dir, diff)
    assert payload["task_count"] == 1
    task = payload["tasks"][0]
    assert task["target_spec"] == "specs/wecom/departments.yaml"
    assert task["status"] in {"incomplete", "review_required"}


def test_build_agent_tasks_blocks_unresolved_unknown_domain(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()

    catalog = {
        "snapshot_date": "2026-04-23",
        "operations": [
            {
                "id": "todo.cgi_bin_unmapped_op",
                "domain": "unknown",
                "name": "cgi_bin_unmapped_op",
                "endpoint": "/cgi-bin/unmapped/op",
                "method": "POST",
                "doc": {
                    "title": "未映射接口",
                    "request_example_json": {"x": 1},
                    "response_example_json": {"errcode": 0},
                },
            }
        ],
    }
    diff = {
        "discovery_snapshot": "2026-04-24",
        "added": [{"endpoint": "/cgi-bin/unmapped/op", "method": "POST"}],
    }

    payload = build_agent_tasks(catalog, spec_dir, diff)
    task = payload["tasks"][0]
    assert task["target_spec"] is None
    assert task["status"] == "review_required"
    assert task["confidence"] <= 0.3


def test_build_agent_tasks_omits_already_implemented_added_tasks(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "batch.yaml").write_text(
        json.dumps(
            {
                "domain": "batch",
                "operations": [
                    {
                        "name": "invite",
                        "summary": "邀请成员",
                        "method": "POST",
                        "endpoint": "/cgi-bin/batch/invite",
                        "args": [{"name": "user", "type": "json"}],
                        "request": {"json_body": {"user": {"from_arg": "user"}}},
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
                "id": "batch.invite",
                "domain": "batch",
                "name": "invite",
                "endpoint": "/cgi-bin/batch/invite",
                "method": "POST",
                "doc": {
                    "title": "邀请成员",
                    "request_example_json": {"user": ["a"]},
                    "response_example_json": {"errcode": 0},
                },
            }
        ],
    }
    diff = {
        "discovery_snapshot": "2026-04-24",
        "added": [{"endpoint": "/cgi-bin/batch/invite", "method": "POST"}],
    }

    payload = build_agent_tasks(catalog, spec_dir, diff)
    assert payload["task_count"] == 0
