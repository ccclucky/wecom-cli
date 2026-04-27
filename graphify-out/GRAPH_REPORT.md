# Graph Report - wecom-cli  (2026-04-28)

## Corpus Check
- 35 files · ~15,992 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 351 nodes · 620 edges · 19 communities detected
- Extraction: 71% EXTRACTED · 29% INFERRED · 0% AMBIGUOUS · INFERRED: 180 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 21|Community 21]]

## God Nodes (most connected - your core abstractions)
1. `GeneratedWeComClient` - 42 edges
2. `UnifiedRequester` - 25 edges
3. `build_agent_tasks()` - 18 edges
4. `WeComConfig` - 14 edges
5. `APIResponseError` - 13 edges
6. `sync_specs_with_catalog()` - 13 edges
7. `AccessTokenProvider` - 11 edges
8. `build_missing_plan()` - 11 edges
9. `APIRequestError` - 10 edges
10. `WeComCLIError` - 9 edges

## Surprising Connections (you probably didn't know these)
- `GeneratedWeComClient` --uses--> `Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT.`  [INFERRED]
  apis/generated_client.py → D:\project\pers\wecom-cli\cli\generated_commands.py
- `Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\generated_client.py → core/requester.py
- `Contacts domain APIs.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\contacts.py → core/requester.py
- `Messages domain APIs.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\messages.py → core/requester.py
- `External contact domain APIs.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\customers.py → core/requester.py

## Hyperedges (group relationships)
- **End-to-End Catalog Sync Pipeline** — coverage_seeds_txt, coverage_discover_script, coverage_catalog_sot, sync_playbook_scaffold, readme_codegen_script, coverage_check_script [EXTRACTED 1.00]
- **v1 Freeze Triple Lock (architecture + cli-ux + spec-schema)** — architecture_layered, cli_ux_v1_freeze, spec_schema_v1_freeze [EXTRACTED 1.00]
- **Issue Resolution Loop (detect -> report -> auto-apply -> scaffold -> codegen -> test -> PR)** — issue_runbook, workflow_sop, issue_runbook_auto_apply, coverage_check_script [INFERRED 0.85]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (31): AccessTokenProvider, WeCom access token acquisition and caching., TokenBundle, load(), Configuration loading for WeCom CLI., WeComConfig, APIRequestError, APIResponseError (+23 more)

### Community 1 - "Community 1"
Cohesion: 0.09
Nodes (2): GeneratedWeComClient, Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.

### Community 2 - "Community 2"
Cohesion: 0.1
Nodes (29): _bool_from_required(), build_seed_urls(), crawl(), CrawlFailure, CrawlReport, DiscoveredField, DiscoveredOperation, DocBlock (+21 more)

### Community 3 - "Community 3"
Cohesion: 0.09
Nodes (34): WeCom API Catalog Daily Report, catalog_diff_report.py, implementation.tasks.yaml as authoritative input, artifacts/implementation.tasks.yaml, Catalog Sync Pipeline (discover -> diff -> apply -> scaffold -> codegen), Coding Agent (automated spec implementation), Rationale: catalog.yaml is directory sync only, not business implementation, Single Source of Truth: catalog.yaml (+26 more)

### Community 4 - "Community 4"
Cohesion: 0.17
Nodes (20): build_agent_tasks(), _confidence_for_task(), _determine_status(), _load_diff_index(), _load_json_yaml(), _load_spec_indices(), main(), _op_id() (+12 more)

### Community 5 - "Community 5"
Cohesion: 0.2
Nodes (19): _annotate_schema_descriptions(), apply_plan(), _build_args_and_request(), _build_doc_payload(), build_missing_plan(), _build_output_from_doc(), _infer_arg_type(), _infer_json_schema() (+11 more)

### Community 6 - "Community 6"
Cohesion: 0.14
Nodes (20): CLI Layer, Command Naming Convention (wecom <resource> <action>), Error Classification (INVALID_ARGUMENT, UNAUTHORIZED, etc.), Exit Codes (0/2/3/4/5), Output Formats (table/json/text), CLI UX Specification (v1), Rationale: Stability rules protect downstream programmatic consumers, v1 Command Surface Freeze Policy (+12 more)

### Community 7 - "Community 7"
Cohesion: 0.2
Nodes (16): ApiItem, _as_items(), build_diff(), build_diff_payload(), build_reconciled_catalog(), _doc_from_discovered(), _infer_catalog_identity(), _load_json_yaml() (+8 more)

### Community 8 - "Community 8"
Cohesion: 0.18
Nodes (11): Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT., register_generated_commands(), bootstrap(), build_parser(), main(), route(), _build_parser_and_table(), DummyClient (+3 more)

### Community 9 - "Community 9"
Cohesion: 0.24
Nodes (13): _load_json_yaml(), main(), _merge_doc(), _merge_get_contract(), _merge_output(), _op_id(), Sync structured catalog doc metadata into existing WeCom specs., _review_hints_for_operation() (+5 more)

### Community 10 - "Community 10"
Cohesion: 0.16
Nodes (15): Application Layer, Dependency Rules (unidirectional inward), Rationale: Unidirectional dependency prevents circular coupling, Domain Layer, Infrastructure Layer, Layered Architecture (CLI / Application / Domain / Infrastructure), Test Layering (CLI / Application / Domain / Infrastructure tests), Bootstrap Initialization Guide (+7 more)

### Community 11 - "Community 11"
Cohesion: 0.27
Nodes (10): _indent_block(), _load_specs(), main(), _py_expr(), Generate API client and CLI command skeletons from specs/wecom/*.yaml., _render_add_argument(), _render_cli(), _render_client() (+2 more)

### Community 12 - "Community 12"
Cohesion: 0.29
Nodes (10): build_coverage_report(), _collect_from_arg_refs(), _collect_spec_operations(), CoverageReport, _load_json_yaml(), _main(), Validate API coverage from specs against the frozen catalog list., test_api_coverage_is_100_percent_for_catalog_snapshot() (+2 more)

### Community 13 - "Community 13"
Cohesion: 0.27
Nodes (10): _assert_clean(), _clean_summary(), _load_json(), main(), One-command orchestrator for WeCom catalog discovery/diff/sync workflow., _run(), _task_catalog_path(), test_clean_summary_reads_diff_and_tasks() (+2 more)

### Community 14 - "Community 14"
Cohesion: 0.4
Nodes (2): ContactsAPI, Contacts domain APIs.

### Community 15 - "Community 15"
Cohesion: 0.4
Nodes (2): MessagesAPI, Messages domain APIs.

### Community 16 - "Community 16"
Cohesion: 0.4
Nodes (2): CustomersAPI, External contact domain APIs.

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (1): APIResult

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (1): core/errors.py

## Knowledge Gaps
- **29 isolated node(s):** `Unified error hierarchy for WeCom CLI.`, `Base class for predictable CLI failures.`, `Raised when loading configuration fails.`, `Raised when access token acquisition fails.`, `Raised when a transport-level request error occurs.` (+24 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 1`** (41 nodes): `generated_client.py`, `GeneratedWeComClient`, `.auth_get_token()`, `.batch_invite()`, `.batch_replaceparty()`, `.batch_replaceuser()`, `.batch_syncuser()`, `.contacts_list_users()`, `.corp_get_join_qrcode()`, `.corp_opencorpid_to_corpid()`, `.departments_create()`, `.departments_delete()`, `.departments_get()`, `.departments_list()`, `.departments_list_ids()`, `.departments_update()`, `.idconvert_convert_tmp_external_userid()`, `.__init__()`, `.messages_send_text()`, `.network_get_api_domain_ip()`, `.network_get_callback_ip()`, `.tags_addtagusers()`, `.tags_create()`, `.tags_delete()`, `.tags_deltagusers()`, `.tags_get()`, `.tags_list()`, `.tags_update()`, `.users_authsucc()`, `.users_batchdelete()`, `.users_convert_to_openid()`, `.users_create()`, `.users_delete()`, `.users_get()`, `.users_get_userid_by_email()`, `.users_getuserid()`, `.users_list()`, `.users_list_id()`, `.users_update()`, `Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.`, `.request()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (5 nodes): `contacts.py`, `ContactsAPI`, `.__init__()`, `.list_users()`, `Contacts domain APIs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (5 nodes): `messages.py`, `MessagesAPI`, `.__init__()`, `.send_text()`, `Messages domain APIs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (5 nodes): `customers.py`, `CustomersAPI`, `.__init__()`, `.list_follow_users()`, `External contact domain APIs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (2 nodes): `APIResult`, `common.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `core/errors.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `fetch_html()` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Why does `UnifiedRequester` connect `Community 0` to `Community 1`, `Community 8`, `Community 14`, `Community 15`, `Community 16`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Why does `GeneratedWeComClient` connect `Community 1` to `Community 0`, `Community 8`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `GeneratedWeComClient` (e.g. with `UnifiedRequester` and `Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT.`) actually correct?**
  _`GeneratedWeComClient` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `UnifiedRequester` (e.g. with `GeneratedWeComClient` and `Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.`) actually correct?**
  _`UnifiedRequester` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `build_agent_tasks()` (e.g. with `test_build_agent_tasks_creates_missing_task_with_drafts()` and `test_build_agent_tasks_skips_fully_implemented_operations()`) actually correct?**
  _`build_agent_tasks()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `WeComConfig` (e.g. with `TokenBundle` and `AccessTokenProvider`) actually correct?**
  _`WeComConfig` has 13 INFERRED edges - model-reasoned connections that need verification._