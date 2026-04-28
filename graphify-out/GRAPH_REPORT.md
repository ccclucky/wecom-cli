# Graph Report - .  (2026-04-29)

## Corpus Check
- 53 files · ~45,885 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 815 nodes · 1517 edges · 20 communities detected
- Extraction: 64% EXTRACTED · 36% INFERRED · 0% AMBIGUOUS · INFERRED: 540 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Generated Client & Commands|Generated Client & Commands]]
- [[_COMMUNITY_Discovery Crawler Core|Discovery Crawler Core]]
- [[_COMMUNITY_Agent Task Planning|Agent Task Planning]]
- [[_COMMUNITY_Core Infrastructure (AuthConfigHTTP)|Core Infrastructure (Auth/Config/HTTP)]]
- [[_COMMUNITY_Spec & Catalog Data Models|Spec & Catalog Data Models]]
- [[_COMMUNITY_Documentation & Project Overview|Documentation & Project Overview]]
- [[_COMMUNITY_CICD & Workflow Automation|CI/CD & Workflow Automation]]
- [[_COMMUNITY_Test Suite|Test Suite]]
- [[_COMMUNITY_Coverage & Quality Gates|Coverage & Quality Gates]]
- [[_COMMUNITY_CLI Interface & Routing|CLI Interface & Routing]]
- [[_COMMUNITY_Code Generation Engine|Code Generation Engine]]
- [[_COMMUNITY_Menu Tree & Seed Management|Menu Tree & Seed Management]]
- [[_COMMUNITY_Empty Page Cache|Empty Page Cache]]
- [[_COMMUNITY_CAPTCHA Detection|CAPTCHA Detection]]
- [[_COMMUNITY_API Scaffolding|API Scaffolding]]
- [[_COMMUNITY_Spec Document Sync|Spec Document Sync]]
- [[_COMMUNITY_OA Approval Ops|OA Approval Ops]]
- [[_COMMUNITY_Meeting Ops|Meeting Ops]]
- [[_COMMUNITY_Wedoc Ops|Wedoc Ops]]
- [[_COMMUNITY_Wedrive Ops|Wedrive Ops]]

## God Nodes (most connected - your core abstractions)
1. `GeneratedWeComClient` - 315 edges
2. `UnifiedRequester` - 25 edges
3. `crawl()` - 23 edges
4. `build_agent_tasks()` - 18 edges
5. `WeComConfig` - 14 edges
6. `build_missing_plan()` - 14 edges
7. `sync_specs_with_catalog()` - 14 edges
8. `APIResponseError` - 13 edges
9. `WeCom CLI Project (企业微信命令行工具)` - 11 edges
10. `AccessTokenProvider` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Core Config Loading (core/config.py)` --semantically_similar_to--> `Bootstrap: Core Capabilities (Config/Auth/Requester/Errors)`  [INFERRED] [semantically similar]
  README.md → docs/bootstrap.md
- `Core Auth Token Management (core/auth.py)` --semantically_similar_to--> `Bootstrap: Core Capabilities (Config/Auth/Requester/Errors)`  [INFERRED] [semantically similar]
  README.md → docs/bootstrap.md
- `Project Module Structure (core/cli/apis/models/tests/docs)` --semantically_similar_to--> `4-Layer Architecture (CLI/Application/Domain/Infrastructure)`  [INFERRED] [semantically similar]
  README.md → docs/architecture.md
- `scripts/codegen.py` --references--> `Generated API Examples`  [EXTRACTED]
  README.md → docs/examples/generated-apis.md
- `catalog_diff_report.py` --references--> `API Discovery and Sync Playbook`  [INFERRED]
  artifacts/wecom-catalog-report.md → docs/sync-playbook.md

## Hyperedges (group relationships)
- **Catalog Sync Pipeline** —  [INFERRED]
- **Coverage Quality Gate** —  [INFERRED]
- **Spec-Driven Code Generation Pipeline** —  [INFERRED]
- **CI Pipeline Triad — Coverage Check + Catalog Watch + Diff Report** — check_api_coverage_script, wecom_catalog_watch_ci, catalog_diff_report_script [INFERRED 0.85]
- **End-to-End Coverage Pipeline — Catalog → Discover → Diff → Codegen → Verify** — catalog_yaml, discover_wecom_apis_script, catalog_diff_report_script, codegen_script, check_api_coverage_script [EXTRACTED 1.00]
- **CLI Output Contract — Error Structure + Output Formats + Exit Codes** — cli_exit_codes, cli_output_formats, cli_error_structure [EXTRACTED 1.00]

## Communities

### Community 1 - "Generated Client & Commands"
Cohesion: 0.01
Nodes (1): GeneratedWeComClient

### Community 2 - "Discovery Crawler Core"
Cohesion: 0.05
Nodes (73): collections, _bool_from_required(), build_seed_urls(), crawl(), CrawlFailure, CrawlReport, DiscoveredField, DiscoveredOperation (+65 more)

### Community 3 - "Agent Task Planning"
Cohesion: 0.06
Nodes (64): build_agent_tasks(), _confidence_for_task(), _determine_status(), _load_diff_index(), _load_json_yaml(), _load_spec_indices(), main(), _op_id() (+56 more)

### Community 4 - "Core Infrastructure (Auth/Config/HTTP)"
Cohesion: 0.06
Nodes (43): AccessTokenProvider, WeCom access token acquisition and caching., TokenBundle, WeComConfig, ContactsAPI, Contacts domain APIs., core_auth, core_config (+35 more)

### Community 5 - "Spec & Catalog Data Models"
Cohesion: 0.05
Nodes (55): build_coverage_report(), _collect_from_arg_refs(), _collect_spec_operations(), CoverageReport, _load_json_yaml(), _main(), Validate API coverage from specs against the frozen catalog list., _dedup_args() (+47 more)

### Community 6 - "Documentation & Project Overview"
Cohesion: 0.06
Nodes (50): Infrastructure Layer, Bootstrap Initialization Guide, WeCom API Catalog Daily Report, catalog_diff_report.py, implementation.tasks.yaml as authoritative input, artifacts/implementation.tasks.yaml, access_token (WeCom auth credential), Catalog Sync Pipeline (discover -> diff -> apply -> scaffold -> codegen) (+42 more)

### Community 7 - "CI/CD & Workflow Automation"
Cohesion: 0.07
Nodes (41): 25 Removed Endpoints — batch/department/tag/user/token, Catalog Baseline — 311 Endpoints (2026-04-23), catalog_diff_report.py — Diff Reporter, Catalog Diff Types (Added/Removed/Modified), Catalog Discovery — 291 Endpoints Found, catalog.yaml — Single Source of Truth, check_api_coverage.py — Coverage Verifier, CLI Command Structure — wecom resource action (+33 more)

### Community 8 - "Test Suite"
Cohesion: 0.07
Nodes (29): Architecture: Dependency Rules (One-Way CLI->App->Domain), 4-Layer Architecture (CLI/Application/Domain/Infrastructure), Rationale: Why Strict Layer Separation with One-Way Dependency Flow, Architecture: Test Layering (CLI/App/Domain/Infra Tests), Architecture: v1 Evolution Constraints, PRD: Full Public API Coverage Definition (N_covered/N_total), Rationale: Why Coverage is Defined as N_covered/N_total with Exemptions, Rationale: Why v1 Scope Excludes Non-Public/Internal APIs, SDK, and Web Console (+21 more)

### Community 9 - "Coverage & Quality Gates"
Cohesion: 0.1
Nodes (25): Application Layer, CLI Layer, Dependency Rules (unidirectional inward), Rationale: Unidirectional dependency prevents circular coupling, Domain Layer, Layered Architecture (CLI / Application / Domain / Infrastructure), Test Layering (CLI / Application / Domain / Infrastructure tests), Command Naming Convention (wecom <resource> <action>) (+17 more)

### Community 10 - "CLI Interface & Routing"
Cohesion: 0.16
Nodes (21): ApiItem, _as_items(), build_diff(), build_diff_payload(), build_reconciled_catalog(), _doc_from_discovered(), _infer_catalog_identity(), _load_json_yaml() (+13 more)

### Community 11 - "Code Generation Engine"
Cohesion: 0.14
Nodes (16): apis_generated_client, argparse, cli_generated_commands, cli_main, collections_abc, Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT., register_generated_commands(), build_parser() (+8 more)

### Community 12 - "Menu Tree & Seed Management"
Cohesion: 0.25
Nodes (9): Application Layer (UseCase Orchestration, Input Validation), CLI Layer (Command Entry, Arg Parsing, Output Rendering), Domain Layer (Entities, Business Rules, Error Semantics), Infrastructure Layer (HTTP SDK, Auth, Config, Retry/Logging), Bootstrap: Core Capabilities (Config/Auth/Requester/Errors), Core Auth Token Management (core/auth.py), Core Config Loading (core/config.py), Core Error Handling (core/errors.py) (+1 more)

### Community 13 - "Empty Page Cache"
Cohesion: 0.5
Nodes (3): apis_contacts, apis_customers, apis_messages

### Community 14 - "CAPTCHA Detection"
Cohesion: 1.0
Nodes (2): Bootstrap: High-Frequency Commands (contacts/messages/customers), PRD: Core Scenarios

### Community 15 - "API Scaffolding"
Cohesion: 1.0
Nodes (1): models_common

### Community 16 - "Spec Document Sync"
Cohesion: 1.0
Nodes (1): core/errors.py

### Community 18 - "OA Approval Ops"
Cohesion: 1.0
Nodes (1): Version Plan v0.1.x-v0.3.x

### Community 19 - "Meeting Ops"
Cohesion: 1.0
Nodes (1): Graphify Knowledge Graph Operating Rules

### Community 20 - "Wedoc Ops"
Cohesion: 1.0
Nodes (1): PRD: Target Users

### Community 21 - "Wedrive Ops"
Cohesion: 1.0
Nodes (1): SOP: Common Failure Handling (Missing PR, Incomplete Params)

## Knowledge Gaps
- **78 isolated node(s):** `core/errors.py`, `implementation.tasks.yaml as authoritative input`, `Application Layer`, `Domain Layer`, `Rationale: Unidirectional dependency prevents circular coupling` (+73 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Generated Client & Commands`** (156 nodes): `GeneratedWeComClient`, `.advanced_feature_set_approval_detail()`, `.appchat_get()`, `.batch_invite()`, `.batch_replaceparty()`, `.batch_replaceuser()`, `.batch_syncuser()`, `.chatdata_check_debug_mode()`, `.chatdata_close_debug_mode()`, `.chatdata_get_auth_user_list()`, `.chatdata_set_public_key()`, `.checkin_add_checkin_record()`, `.corp_getapprovaldata()`, `.corpgroup_corp_get_chain_user_custom_id()`, `.corpgroup_corp_gettoken()`, `.corpgroup_corp_remove_corp()`, `.corpgroup_import_chain_contact()`, `.corpgroup_rule_list_ids()`, `.customers_add_contact_way()`, `.customers_batch_get_by_user()`, `.customers_cancel_groupmsg_send()`, `.customers_convert_to_openid()`, `.customers_customer_strategy_list()`, `.customers_get()`, `.customers_get_subscribe_qr_code()`, `.customers_groupchat_onjob_transfer()`, `.customers_list()`, `.customers_mark_tag()`, `.customers_message_send()`, `.customers_opengid_to_chatid()`, `.customers_resigned_transfer_customer()`, `.customers_set_subscribe_mode()`, `.customers_transfer_customer()`, `.departments_delete()`, `.departments_get()`, `.departments_list_ids()`, `.exmail_app_compose_send()`, `.exmail_app_get_email_alias()`, `.exmail_app_read_mail()`, `.exmail_group_get()`, `.exmail_group_search()`, `.exmail_group_update()`, `.exmail_useroption_update()`, `.export_taguser()`, `.export_user()`, `.health_get_health_report_stat()`, `.hr_get_staff_info()`, `.hr_update_staff_info()`, `.idconvert_convert_tmp_external_userid()`, `.__init__()`, `.kf_account_del()`, `.kf_get_corp_statistic()`, `.kf_knowledge_add_group()`, `.kf_knowledge_add_intent()`, `.kf_send_msg()`, `.living_get_user_all_livingid()`, `.meeting_cancel()`, `.meeting_enroll_delete()`, `.meeting_get_customer_short_url()`, `.meeting_get_info()`, `.meeting_get_invitees()`, `.meeting_get_user_meetingid()`, `.meeting_layout_batch_delete_background()`, `.meeting_layout_set_default()`, `.meeting_layout_set_default_background()`, `.meeting_mra_set_default_layout()`, `.meeting_mra_set_raise_hand()`, `.meeting_poll_delete()`, `.meeting_poll_start()`, `.meeting_realcontrol_dismiss()`, `.meeting_record_delete()`, `.meeting_statistics_get_start_list()`, `.meeting_update()`, `.meeting_vip_list()`, `.meeting_webinar_enroll_approve()`, `.meeting_webinar_enroll_delete()`, `.meeting_webinar_enroll_import()`, `.messages_recall()`, `.miniapppay_close_order()`, `.miniapppay_create_order()`, `.miniapppay_get_applyment_status()`, `.miniapppay_get_sign()`, `.msgaudit_check_single_agree()`, `.msgaudit_get_robot_info()`, `.msgaudit_groupchat_get()`, `.network_get_callback_ip()`, `.oa_approval_update_template()`, `.oa_calendar_get()`, `.oa_calendar_update()`, `.oa_getapprovalinfo()`, `.oa_gettemplatedetail()`, `.oa_journal_get_record_detail()`, `.oa_meetingroom_get_booking_info()`, `.oa_schedule_del_attendees()`, `.oa_schedule_get()`, `.oa_schedule_update()`, `.oa_vacation_getuservacationquota()`, `.school_department_create()`, `.school_department_list()`, `.school_get_chat_create_mode()`, `.school_getuserinfo()`, `.school_living_get_living_info()`, `.school_living_get_unwatch_stat()`, `.school_living_get_unwatch_stat_v2()`, `.school_set_upgrade_info()`, `.school_user_batch_delete_student()`, `.school_user_create_parent()`, `.school_user_create_student()`, `.school_user_delete_student()`, `.school_user_update_parent()`, `.security_get_screen_oper_record()`, `.security_get_server_domain_ip()`, `.security_member_oper_log_list()`, `.security_vip_list()`, `.security_vip_submit_batch_add_job()`, `.security_vip_submit_batch_del_job()`, `.tags_addtagusers()`, `.tags_create()`, `.tags_delete()`, `.tags_get()`, `.tags_list()`, `.ticket_get()`, `.unknown_cgi_bin_get_launch_code()`, `.users_authsucc()`, `.users_delete()`, `.users_list_id()`, `.wedoc_doc_share()`, `.wedoc_get_doc_base_info()`, `.wedoc_get_form_info()`, `.wedoc_get_form_statistic()`, `.wedoc_image_upload()`, `.wedoc_smartsheet_add_field_group()`, `.wedoc_smartsheet_add_fields()`, `.wedoc_smartsheet_add_sheet()`, `.wedoc_smartsheet_add_view()`, `.wedoc_smartsheet_delete_fields()`, `.wedoc_smartsheet_delete_records()`, `.wedoc_smartsheet_get_records()`, `.wedoc_smartsheet_get_sheet()`, `.wedoc_smartsheet_update_fields()`, `.wedoc_spreadsheet_get_sheet_properties()`, `.wedoc_spreadsheet_get_sheet_range_data()`, `.wedoc_vip_batch_add()`, `.wedoc_vip_list()`, `.wedrive_file_create()`, `.wedrive_file_download()`, `.wedrive_file_move()`, `.wedrive_file_secure_setting()`, `.wedrive_file_share()`, `.wedrive_file_upload()`, `.wedrive_file_upload_init()`, `.wedrive_get_file_permission()`, `.wedrive_space_acl_del()`, `.wedrive_space_info()`, `.wedrive_vip_batch_add()`, `.wedrive_vip_list()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CAPTCHA Detection`** (2 nodes): `Bootstrap: High-Frequency Commands (contacts/messages/customers)`, `PRD: Core Scenarios`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `API Scaffolding`** (2 nodes): `models_common`, `__init__.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Spec Document Sync`** (1 nodes): `core/errors.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `OA Approval Ops`** (1 nodes): `Version Plan v0.1.x-v0.3.x`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Meeting Ops`** (1 nodes): `Graphify Knowledge Graph Operating Rules`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Wedoc Ops`** (1 nodes): `PRD: Target Users`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Wedrive Ops`** (1 nodes): `SOP: Common Failure Handling (Missing PR, Incomplete Params)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `GeneratedWeComClient` connect `Generated Client & Commands` to `Catalog Discovery Pipeline`, `Code Generation Engine`, `Core Infrastructure (Auth/Config/HTTP)`?**
  _High betweenness centrality (0.221) - this node is a cross-community bridge._
- **Why does `fetch_html()` connect `Discovery Crawler Core` to `Catalog Discovery Pipeline`, `Spec & Catalog Data Models`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `UnifiedRequester` connect `Core Infrastructure (Auth/Config/HTTP)` to `Catalog Discovery Pipeline`, `Generated Client & Commands`?**
  _High betweenness centrality (0.045) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `GeneratedWeComClient` (e.g. with `UnifiedRequester` and `Auto-generated CLI command registration from specs/wecom/*.yaml. DO NOT EDIT.`) actually correct?**
  _`GeneratedWeComClient` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 21 inferred relationships involving `UnifiedRequester` (e.g. with `GeneratedWeComClient` and `Auto-generated API client from specs/wecom/*.yaml. DO NOT EDIT.`) actually correct?**
  _`UnifiedRequester` has 21 INFERRED edges - model-reasoned connections that need verification._
- **Are the 13 inferred relationships involving `crawl()` (e.g. with `test_crawl_visits_all_seeds()` and `test_crawl_respects_max_pages()`) actually correct?**
  _`crawl()` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Are the 11 inferred relationships involving `build_agent_tasks()` (e.g. with `test_build_agent_tasks_creates_missing_task_with_drafts()` and `test_build_agent_tasks_skips_fully_implemented_operations()`) actually correct?**
  _`build_agent_tasks()` has 11 INFERRED edges - model-reasoned connections that need verification._