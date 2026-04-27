from __future__ import annotations

import json

from scripts.sync_spec_docs import sync_specs_with_catalog


def test_sync_specs_with_catalog_dry_run_does_not_write(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    spec_path = spec_dir / "contacts.yaml"
    spec_path.write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [
                    {
                        "name": "list_users",
                        "summary": "TODO: list_users",
                        "method": "GET",
                        "endpoint": "/cgi-bin/user/simplelist",
                        "args": [],
                        "request": {},
                        "examples": ["ok"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    original = spec_path.read_text(encoding="utf-8")

    catalog = {
        "operations": [
            {
                "id": "contacts.list_users",
                "doc": {
                    "title": "获取部门成员",
                    "request_params": [
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                        {"name": "department_id", "required": True, "description": "部门 ID"},
                    ],
                },
            }
        ]
    }

    changed, stats = sync_specs_with_catalog(catalog, spec_dir, apply=False)
    assert changed == [spec_path]
    assert stats["spec_files_changed"] == 1
    assert spec_path.read_text(encoding="utf-8") == original


def test_sync_specs_with_catalog_enriches_get_contracts(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    spec_path = spec_dir / "contacts.yaml"
    spec_path.write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [
                    {
                        "name": "list_users",
                        "summary": "TODO: list_users",
                        "method": "GET",
                        "endpoint": "/cgi-bin/user/simplelist",
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
        "operations": [
            {
                "id": "contacts.list_users",
                "doc": {
                    "title": "获取部门成员",
                    "source_url": "u1",
                    "request_params": [
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                        {"name": "department_id", "required": True, "description": "部门 ID"},
                        {"name": "fetch_child", "required": False, "description": "是否递归"},
                    ],
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                        {"name": "errmsg", "description": "返回信息"},
                    ],
                    "response_example_json": {"errcode": 0, "errmsg": "ok"},
                    "notes": ["注意分页"],
                },
            }
        ]
    }

    changed, stats = sync_specs_with_catalog(catalog, spec_dir, apply=True)
    assert changed == [spec_path]
    assert stats["get_contracts_enriched"] == 1

    payload = json.loads(spec_path.read_text(encoding="utf-8"))
    op = payload["operations"][0]
    assert op["summary"] == "获取部门成员"
    assert [arg["name"] for arg in op["args"]] == ["department_id", "fetch_child"]
    assert op["request"]["query"]["department_id"] == {"from_arg": "department_id"}
    assert op["request"]["query"]["fetch_child"] == {"int_bool_arg": "fetch_child"}
    assert op["doc"]["source_url"] == "u1"
    assert op["output"]["formats"] == ["json"]
    assert op["output"]["json_schema"]["properties"]["errmsg"]["description"] == "返回信息"
    assert "Review doc.notes" in op["doc"]["review_hints"][0]


def test_sync_specs_with_catalog_adds_review_hints_for_post(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    spec_path = spec_dir / "messages.yaml"
    spec_path.write_text(
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
        "operations": [
            {
                "id": "messages.send_text",
                "doc": {
                    "title": "发送应用消息",
                    "request_params": [
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                    ],
                    "request_example_json": {"touser": "zhangsan", "msgtype": "text"},
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                        {"name": "errmsg", "description": "返回信息"},
                    ],
                    "response_example_json": {"errcode": 0, "errmsg": "ok"},
                },
            }
        ]
    }

    changed, stats = sync_specs_with_catalog(catalog, spec_dir, apply=True)
    assert changed == [spec_path]
    assert stats["operations_review_hinted"] == 1

    payload = json.loads(spec_path.read_text(encoding="utf-8"))
    op = payload["operations"][0]
    assert op["request"] == {}
    assert op["output"]["json_schema"]["properties"]["errcode"]["type"] == "integer"
    assert len(op["doc"]["review_hints"]) == 2
