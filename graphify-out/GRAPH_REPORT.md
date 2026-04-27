# Graph Report - .  (2026-04-27)

## Corpus Check
- Corpus is ~15,808 words - fits in a single context window. You may not need a graph.

## Summary
- 386 nodes · 793 edges · 18 communities detected
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 180 edges (avg confidence: 0.72)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Core Infrastructure|Core Infrastructure]]
- [[_COMMUNITY_Project Documentation|Project Documentation]]
- [[_COMMUNITY_Generated API Client|Generated API Client]]
- [[_COMMUNITY_API Discovery Crawler|API Discovery Crawler]]
- [[_COMMUNITY_Architecture & Spec Design|Architecture & Spec Design]]
- [[_COMMUNITY_Agent Task Builder|Agent Task Builder]]
- [[_COMMUNITY_Catalog Scaffolding|Catalog Scaffolding]]
- [[_COMMUNITY_CLI Routing|CLI Routing]]
- [[_COMMUNITY_Catalog Diff Report|Catalog Diff Report]]
- [[_COMMUNITY_Spec Doc Sync|Spec Doc Sync]]
- [[_COMMUNITY_Code Generation|Code Generation]]
- [[_COMMUNITY_API Coverage Checker|API Coverage Checker]]
- [[_COMMUNITY_Catalog Sync Runner|Catalog Sync Runner]]
- [[_COMMUNITY_Contacts API|Contacts API]]
- [[_COMMUNITY_Customers API|Customers API]]
- [[_COMMUNITY_Messages API|Messages API]]
- [[_COMMUNITY_Common Models|Common Models]]
- [[_COMMUNITY_Error Docs|Error Docs]]

## God Nodes (most connected - your core abstractions)
1. `GeneratedWeComClient` - 43 edges
2. `UnifiedRequester` - 26 edges
3. `build_agent_tasks()` - 19 edges
4. `WeComConfig` - 15 edges
5. `APIResponseError` - 14 edges
6. `sync_specs_with_catalog()` - 14 edges
7. `AccessTokenProvider` - 12 edges
8. `build_missing_plan()` - 12 edges
9. `APIRequestError` - 11 edges
10. `WeComCLIError` - 10 edges

## Surprising Connections (you probably didn't know these)
- `ContactsAPI` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\contacts.py → D:\project\pers\wecom-cli\core\requester.py
- `Contacts domain APIs.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\contacts.py → D:\project\pers\wecom-cli\core\requester.py
- `CustomersAPI` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\customers.py → D:\project\pers\wecom-cli\core\requester.py
- `External contact domain APIs.` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\customers.py → D:\project\pers\wecom-cli\core\requester.py
- `GeneratedWeComClient` --uses--> `UnifiedRequester`  [INFERRED]
  D:\project\pers\wecom-cli\apis\generated_client.py → D:\project\pers\wecom-cli\core\requester.py

## Hyperedges (group relationships)
- **End-to-End Catalog Sync Pipeline** — coverage_seeds_txt, coverage_discover_script, coverage_catalog_sot, sync_playbook_scaffold, readme_codegen_script, coverage_check_script [EXTRACTED 1.00]
- **v1 Freeze Triple Lock (architecture + cli-ux + spec-schema)** — architecture_layered, cli_ux_v1_freeze, spec_schema_v1_freeze [EXTRACTED 1.00]
- **Issue Resolution Loop (detect -> report -> auto-apply -> scaffold -> codegen -> test -> PR)** — issue_runbook, workflow_sop, issue_runbook_auto_apply, coverage_check_script [INFERRED 0.85]

## Communities

### Community 0 - "Core Infrastructure"
Cohesion: 0.07
Nodes (30): AccessTokenProvider, WeCom access token acquisition and caching., TokenBundle, load(), Configuration loading for WeCom CLI., WeComConfig, APIRequestError, APIResponseError (+22 more)

### Community 1 - "Project Documentation"
Cohesion: 0.07
Nodes (43): Infrastructure Layer, Bootstrap Initialization Guide, WeCom API Catalog Daily Report, catalog_diff_report.py, implementation.tasks.yaml as authoritative input, artifacts/implementation.tasks.yaml, access_token (WeCom auth credential), Catalog Sync Pipeline (discover -> diff -> apply -> scaffold -> codegen) (+35 more)

### Community 2 - "Generated API Client"
Cohesion: 0.09
Nodes (2): GeneratedWeComClient, Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.

### Community 3 - "API Discovery Crawler"
Cohesion: 0.13
Nodes (29): _bool_from_required(), build_seed_urls(), crawl(), CrawlFailure, CrawlReport, DiscoveredField, DiscoveredOperation, DocBlock (+21 more)

### Community 4 - "Architecture & Spec Design"
Cohesion: 0.1
Nodes (26): Application Layer, CLI Layer, Dependency Rules (unidirectional inward), Rationale: Unidirectional dependency prevents circular coupling, Domain Layer, Layered Architecture (CLI / Application / Domain / Infrastructure), Test Layering (CLI / Application / Domain / Infrastructure tests), Command Naming Convention (wecom <resource> <action>) (+18 more)

### Community 5 - "Agent Task Builder"
Cohesion: 0.21
Nodes (20): build_agent_tasks(), _confidence_for_task(), _determine_status(), _load_diff_index(), _load_json_yaml(), _load_spec_indices(), main(), _op_id() (+12 more)

### Community 6 - "Catalog Scaffolding"
Cohesion: 0.24
Nodes (19): _annotate_schema_descriptions(), apply_plan(), _build_args_and_request(), _build_doc_payload(), build_missing_plan(), _build_output_from_doc(), _infer_arg_type(), _infer_json_schema() (+11 more)

### Community 7 - "CLI Routing"
Cohesion: 0.17
Nodes (12): Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT., register_generated_commands(), bootstrap(), build_parser(), main(), Command-line interface for WeCom CLI., route(), _build_parser_and_table() (+4 more)

### Community 8 - "Catalog Diff Report"
Cohesion: 0.25
Nodes (17): ApiItem, _as_items(), build_diff(), build_diff_payload(), build_reconciled_catalog(), _doc_from_discovered(), _infer_catalog_identity(), key() (+9 more)

### Community 9 - "Spec Doc Sync"
Cohesion: 0.28
Nodes (13): _load_json_yaml(), main(), _merge_doc(), _merge_get_contract(), _merge_output(), _op_id(), Sync structured catalog doc metadata into existing WeCom specs., _review_hints_for_operation() (+5 more)

### Community 10 - "Code Generation"
Cohesion: 0.3
Nodes (11): _indent_block(), _load_specs(), main(), _py_expr(), Generate API client and CLI command skeletons from specs/wecom/*.yaml., _render_add_argument(), _render_cli(), _render_client() (+3 more)

### Community 11 - "API Coverage Checker"
Cohesion: 0.32
Nodes (10): build_coverage_report(), _collect_from_arg_refs(), _collect_spec_operations(), CoverageReport, _load_json_yaml(), _main(), Validate API coverage from specs against the frozen catalog list., test_api_coverage_is_100_percent_for_catalog_snapshot() (+2 more)

### Community 12 - "Catalog Sync Runner"
Cohesion: 0.31
Nodes (10): _assert_clean(), _clean_summary(), _load_json(), main(), One-command orchestrator for WeCom catalog discovery/diff/sync workflow., _run(), _task_catalog_path(), test_clean_summary_reads_diff_and_tasks() (+2 more)

### Community 13 - "Contacts API"
Cohesion: 0.4
Nodes (2): ContactsAPI, Contacts domain APIs.

### Community 14 - "Customers API"
Cohesion: 0.4
Nodes (2): CustomersAPI, External contact domain APIs.

### Community 15 - "Messages API"
Cohesion: 0.4
Nodes (2): MessagesAPI, Messages domain APIs.

### Community 16 - "Common Models"
Cohesion: 0.67
Nodes (1): APIResult

### Community 23 - "Error Docs"
Cohesion: 1.0
Nodes (1): core/errors.py

## Knowledge Gaps
- **19 isolated node(s):** `Base class for predictable CLI failures.`, `Raised when loading configuration fails.`, `Raised when access token acquisition fails.`, `Raised when a transport-level request error occurs.`, `Raised when WeCom API returns a non-success errcode.` (+14 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Generated API Client`** (42 nodes): `generated_client.py`, `generated_client.py`, `GeneratedWeComClient`, `.auth_get_token()`, `.batch_invite()`, `.batch_replaceparty()`, `.batch_replaceuser()`, `.batch_syncuser()`, `.contacts_list_users()`, `.corp_get_join_qrcode()`, `.corp_opencorpid_to_corpid()`, `.departments_create()`, `.departments_delete()`, `.departments_get()`, `.departments_list()`, `.departments_list_ids()`, `.departments_update()`, `.idconvert_convert_tmp_external_userid()`, `.__init__()`, `.messages_send_text()`, `.network_get_api_domain_ip()`, `.network_get_callback_ip()`, `.tags_addtagusers()`, `.tags_create()`, `.tags_delete()`, `.tags_deltagusers()`, `.tags_get()`, `.tags_list()`, `.tags_update()`, `.users_authsucc()`, `.users_batchdelete()`, `.users_convert_to_openid()`, `.users_create()`, `.users_delete()`, `.users_get()`, `.users_get_userid_by_email()`, `.users_getuserid()`, `.users_list()`, `.users_list_id()`, `.users_update()`, `Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.`, `.request()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Contacts API`** (6 nodes): `contacts.py`, `ContactsAPI`, `.__init__()`, `.list_users()`, `Contacts domain APIs.`, `contacts.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Customers API`** (6 nodes): `customers.py`, `CustomersAPI`, `.__init__()`, `.list_follow_users()`, `External contact domain APIs.`, `customers.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Messages API`** (6 nodes): `messages.py`, `messages.py`, `MessagesAPI`, `.__init__()`, `.send_text()`, `Messages domain APIs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Common Models`** (3 nodes): `APIResult`, `common.py`, `common.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Error Docs`** (1 nodes): `core/errors.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `fetch_html()` connect `API Discovery Crawler` to `Core Infrastructure`, `Generated API Client`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Why does `UnifiedRequester` connect `Core Infrastructure` to `Generated API Client`, `CLI Routing`, `Contacts API`, `Customers API`, `Messages API`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Why does `GeneratedWeComClient` connect `Generated API Client` to `Core Infrastructure`, `CLI Routing`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `GeneratedWeComClient` (e.g. with `UnifiedRequester` and `Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT.`) actually correct?**
  _`GeneratedWeComClient` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `UnifiedRequester` (e.g. with `ContactsAPI` and `Contacts domain APIs.`) actually correct?**
  _`UnifiedRequester` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `build_agent_tasks()` (e.g. with `_build_doc_payload()` and `_build_args_and_request()`) actually correct?**
  _`build_agent_tasks()` has 11 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `WeComConfig` (e.g. with `Command-line interface for WeCom CLI.` and `TokenBundle`) actually correct?**
  _`WeComConfig` has 13 INFERRED edges - model-reasoned connections that need verification._