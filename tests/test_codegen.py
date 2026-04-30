from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import codegen

ROOT = Path(__file__).resolve().parents[1]


def test_specs_have_examples_and_required_fields():
    for spec_file in sorted((ROOT / "specs" / "wecom").glob("*.yaml")):
        if spec_file.name == "catalog.yaml":
            continue
        spec = json.loads(spec_file.read_text(encoding="utf-8"))
        assert spec["domain"]
        for op in spec["operations"]:
            assert op["name"]
            assert op["method"] in {"GET", "POST"}
            assert op["endpoint"].startswith("/cgi-bin/")
            assert op["examples"], f"{spec_file}::{op['name']} missing examples"


def test_codegen_outputs_current_files(tmp_path):
    specs = codegen._load_specs()
    generated_client = codegen._render_client(specs)
    generated_cli = codegen._render_cli(specs)

    assert "class GeneratedWeComClient" in generated_client
    assert "def contacts_list_users" in generated_client
    assert "def register_generated_commands" in generated_cli
    assert "('messages', 'send-text')" in generated_cli

    (tmp_path / "generated_client.py").write_text(generated_client, encoding="utf-8")
    (tmp_path / "generated_commands.py").write_text(generated_cli, encoding="utf-8")


def test_signature_type_bool_named_limit_maps_to_int():
    assert codegen._signature_type("bool", "limit") == "int"
    assert codegen._signature_type("bool", "offset") == "int"
    assert codegen._signature_type("bool", "count") == "int"
    assert codegen._signature_type("bool", "page") == "int"
    assert codegen._signature_type("bool", "size") == "int"


def test_signature_type_normal_bool_stays_bool():
    assert codegen._signature_type("bool", "fetch_child") == "bool"
    assert codegen._signature_type("bool", "is_temp") == "bool"
    assert codegen._signature_type("bool", "skip_verify") == "bool"


def test_generated_client_compiles():
    specs = codegen._load_specs()
    generated = codegen._render_client(specs)
    compile(generated, "<generated_client>", "exec")


def test_generated_cli_compiles():
    specs = codegen._load_specs()
    generated = codegen._render_cli(specs)
    compile(generated, "<generated_commands>", "exec")


def test_specs_have_valid_types():
    valid_types = {"str", "int", "float", "bool", "json"}
    for spec_file in sorted((ROOT / "specs" / "wecom").glob("*.yaml")):
        if spec_file.name == "catalog.yaml":
            continue
        spec = json.loads(spec_file.read_text(encoding="utf-8"))
        if "domain" not in spec:
            continue
        for op in spec.get("operations", []):
            for arg in op.get("args", []):
                assert arg.get("type", "str") in valid_types, (
                    f"{spec_file.name}::{op['name']} arg '{arg['name']}' has type {arg.get('type')!r}"
                )


def test_spec_validation_rejects_missing_name():
    bad_spec = [{"domain": "test", "operations": [{"method": "GET", "endpoint": "/cgi-bin/test"}]}]
    with pytest.raises(ValueError, match="missing 'name'"):
        codegen._validate_specs(bad_spec)


def test_spec_validation_rejects_bad_method():
    bad_spec = [{"domain": "test", "operations": [{"name": "bad", "method": "DELETE", "endpoint": "/x"}]}]
    with pytest.raises(ValueError, match="invalid method"):
        codegen._validate_specs(bad_spec)


def test_spec_validation_rejects_bad_type():
    bad_spec = [{"domain": "test", "operations": [
        {"name": "bad", "method": "GET", "endpoint": "/x",
         "args": [{"name": "p", "type": "unknown"}]}
    ]}]
    with pytest.raises(ValueError, match="invalid type"):
        codegen._validate_specs(bad_spec)


def test_render_cli_uses_dunder_action_dest():
    specs = codegen._load_specs()
    cli_code = codegen._render_cli(specs)
    assert "dest='__action'" in cli_code
    assert "dest='action'" not in cli_code


def test_render_client_body_mode():
    specs = [{"domain": "test", "operations": [
        {"name": "complex_op", "cli_action": "complex-op", "mode": "body",
         "method": "POST", "endpoint": "/cgi-bin/test",
         "request": {"json_body": {"key": "val"}},
         "examples": ["wecom test complex-op --body '{}'"]}
    ]}]
    client_code = codegen._render_client(specs)
    assert "body: dict[str, Any]" in client_code
    assert "json_body=body" in client_code
