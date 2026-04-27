from __future__ import annotations

import json

from scripts.scaffold_from_catalog import apply_plan, build_missing_plan, prune_unknown_operations


def test_build_missing_plan_and_apply(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()

    (spec_dir / "contacts.yaml").write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [{"name": "list_users"}],
            }
        ),
        encoding="utf-8",
    )

    catalog = {
        "operations": [
            {
                "id": "contacts.list_users",
                "domain": "contacts",
                "name": "list_users",
                "endpoint": "/cgi-bin/user/simplelist",
                "method": "GET",
            },
            {
                "id": "contacts.get_user",
                "domain": "contacts",
                "name": "get_user",
                "endpoint": "/cgi-bin/user/get",
                "method": "GET",
            },
        ]
    }

    plan = build_missing_plan(catalog, spec_dir)
    assert len(plan["contacts"]) == 1
    assert plan["contacts"][0]["name"] == "get_user"

    changed = apply_plan(plan, spec_dir)
    assert changed == [spec_dir / "contacts.yaml"]

    result = json.loads((spec_dir / "contacts.yaml").read_text(encoding="utf-8"))
    names = [op["name"] for op in result["operations"]]
    assert names == ["list_users", "get_user"]


def test_build_missing_plan_prefers_id_over_domain_name_fields(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()

    catalog = {
        "operations": [
            {
                "id": "todo.cgi_bin_agent_get",
                "domain": "unknown",
                "name": "cgi_bin_agent_get",
                "endpoint": "/cgi-bin/agent/get",
                "method": "GET",
            }
        ]
    }

    plan = build_missing_plan(catalog, spec_dir)
    assert "todo" in plan
    assert "unknown" not in plan
    assert plan["todo"][0]["name"] == "cgi_bin_agent_get"


def test_build_missing_plan_uses_doc_metadata_for_get_specs(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()

    catalog = {
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
                        {"name": "access_token", "required": True, "description": "调用凭证"},
                        {"name": "department_id", "required": True, "description": "部门 ID"},
                        {"name": "fetch_child", "required": False, "description": "是否递归"},
                    ],
                    "response_params": [
                        {"name": "errcode", "description": "返回码"},
                        {"name": "errmsg", "description": "返回信息"},
                        {"name": "userlist", "description": "成员列表"},
                    ],
                    "response_example_json": {
                        "errcode": 0,
                        "errmsg": "ok",
                        "userlist": [{"userid": "zhangsan"}],
                    },
                    "source_url": "https://developer.work.weixin.qq.com/document/path/90200",
                },
            }
        ]
    }

    plan = build_missing_plan(catalog, spec_dir)
    op = plan["contacts"][0]
    assert op["summary"] == "获取部门成员"
    assert [arg["name"] for arg in op["args"]] == ["department_id", "fetch_child"]
    assert op["request"]["query"]["department_id"] == {"from_arg": "department_id"}
    assert op["request"]["query"]["fetch_child"] == {"int_bool_arg": "fetch_child"}
    assert op["doc"]["source_url"].endswith("/90200")
    assert op["output"]["formats"] == ["json"]
    assert op["output"]["json_schema"]["type"] == "object"
    assert op["output"]["json_schema"]["properties"]["errcode"]["type"] == "integer"
    assert op["output"]["json_schema"]["properties"]["errcode"]["description"] == "返回码"


def test_prune_unknown_operations_removes_ops_not_in_catalog(tmp_path):
    spec_dir = tmp_path / "specs"
    spec_dir.mkdir()
    (spec_dir / "contacts.yaml").write_text(
        json.dumps(
            {
                "domain": "contacts",
                "operations": [
                    {"name": "list_users"},
                    {"name": "stale_op"},
                ],
            }
        ),
        encoding="utf-8",
    )
    catalog = {
        "operations": [
            {"id": "contacts.list_users"},
        ]
    }

    changed = prune_unknown_operations(catalog, spec_dir)
    assert changed == [spec_dir / "contacts.yaml"]

    payload = json.loads((spec_dir / "contacts.yaml").read_text(encoding="utf-8"))
    assert [op["name"] for op in payload["operations"]] == ["list_users"]
