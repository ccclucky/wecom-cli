from __future__ import annotations

import json
from pathlib import Path

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

    # ensure we can write generated artifacts to a target directory in CI
    (tmp_path / "generated_client.py").write_text(generated_client, encoding="utf-8")
    (tmp_path / "generated_commands.py").write_text(generated_cli, encoding="utf-8")
