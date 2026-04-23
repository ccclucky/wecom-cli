from __future__ import annotations

import json

from scripts.scaffold_from_catalog import apply_plan, build_missing_plan


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
