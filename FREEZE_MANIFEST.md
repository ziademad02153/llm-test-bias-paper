# Formal Experiment Freeze Manifest
**Freeze Timestamp:** 2026-11-03 11:10:46 UTC
**Status:** FROZEN & SEALED PRE-MAIN-EXPERIMENT

This document records the cryptographic SHA-256 checksums of all experimental specifications,
datasets, natural fault inventories, and analysis protocols prior to launching the Main Experiment.
Any modification to any of these files invalidates the freeze and requires documented audit trail approval.

## 1. Core Experimental Protocols & Decisions

| File Path | Description | SHA-256 Checksum |
| :--- | :--- | :--- |
| `EXPERIMENT_PROTOCOL.md` | Approved Pre-Registered Experimental Protocol | `67b96b05143d139fae2a153c632a9768e384da40216af89719e5f67600f44511` |
| `data/dataset_decisions.csv` | Dataset Inclusion/Exclusion Audit Decisions (26 Tasks) | `520a622ef45f645f35f3d9211934a3e35a940384dd051186e4cb23fae95174ca` |
| `data/fault_harvest/accepted_faults.json` | Natural LLM Fault Inventory (15 Verified Subtle Defects) | `ea74e6d67d2b37bec0fe7e14ba907995feb0ca32292e999af66805bd069a39d8` |
| `data/fault_harvest/FAULT_HARVEST_REPORT.md` | Formal Fault Harvesting Audit Report | `ea8864440950dcce1ad446c0a027d24ba085db36bb7a7766e607f45183aff2a8` |
| `src/schema.py` | Data Contracts & Schema Definitions | `e2e35b96e66792b82b5e14851344c284d7ebb09b134235ee25a87be9ffb75d86` |
| `src/sandbox.py` | AST Assertion Execution Sandbox | `8ad678d0821b385900571c1f23b419be61dfa2b6413728ce496d307b451c5ea1` |
| `src/runner.py` | LLM API Client & Experiment Orchestrator | `5e549142cdb95b63dbc9a00d6d7994483f033ac55b5a502cdc8fec19194e2e43` |
| `src/stats_utils.py` | Statistical Utilities (McNemar, TOST, Fisher Exact) | `6cf752a69176473d68cbbcb556a8fa60cc3ab0c3d8b5980a3413e96d85706866` |

## 2. Frozen Dataset Problems (20 Real-World Python Tasks Post-July 2025)

| Problem ID | Category | SHA-256 Checksum |
| :--- | :--- | :--- |
| `REAL_TASK_001.json` | Parsing/String | `25e1783258e610974827cefbb2abfa9246fe45ae2059d8a5ec81f6acccf4bce0` |
| `REAL_TASK_002.json` | Parsing/String | `c3a55698639f1348cb75ad3476bd2d7a4839a6c16fbdafa7ed1b770c701002e3` |
| `REAL_TASK_003.json` | Parsing/String | `3505236ddd85513e8a03bf7e164657e910d02c3d4832e530c260885177f922de` |
| `REAL_TASK_004.json` | Parsing/String | `c5210d3dcc5201b3e97da74e341cddbbc77cbf97234252035c443cffe18be6d2` |
| `REAL_TASK_005.json` | Parsing/String | `2a555d458079380438a7aaa31e550203aabd5bcd712b03b16dc0d44ae2dbfc3a` |
| `REAL_TASK_006.json` | Algorithms/Search | `1e0c896f0e490519b26718d8600e55838e7c8d3d47cdd50aada97c1082af1dde` |
| `REAL_TASK_007.json` | Algorithms/Search | `0b263353966afa36502cbc7d1737c39818c374453009df45bbc2ba786ae603ea` |
| `REAL_TASK_008.json` | Algorithms/Search | `e6c3a2248649ae783a712452e5c47dfc143216cacab021a83013f71f02fe21cc` |
| `REAL_TASK_009.json` | Graphs/Trees | `fc21c3cd1135d6039f27600ae628ec4839c3a57899b9c2e966fc826f5f24151c` |
| `REAL_TASK_010.json` | Graphs/Trees | `1b024574c41fa84317ff53b5e599d795c630ba9de984cea843d6e42e1df245bc` |
| `REAL_TASK_011.json` | Scheduling/Intervals | `3642a131cef47a439b378fccf88fe8ca088c68f3ef465d8b47cb4f2e964b7640` |
| `REAL_TASK_012.json` | Scheduling/Intervals | `ebb20d8bf7c5440f6c0b1ce9fcd205d792a38cbf439c0f6121a270513cf8a4f5` |
| `REAL_TASK_013.json` | Scheduling/Intervals | `145ce888585dc25bcfaf9e21ca9566d63477d75c424db4dca00e6efa7a519263` |
| `REAL_TASK_014.json` | State Machines/Retries | `60a8b6c11523b0eb01c9e5a54f20a420f1a3608383dd2bedcfaa07bccc68a802` |
| `REAL_TASK_015.json` | Algorithms/Search | `21a4c404eb80dc8fd352ce3408d5285ba5b6f1e20605175d6970a93079563010` |
| `REAL_TASK_016.json` | State Machines/Retries | `c739e54a8261cf7f4b090eeea179c7ad7882a8553a2fa745b50982249a4ec111` |
| `REAL_TASK_017.json` | State Machines/Retries | `ee61161c8405f1c3c2922965624a0b5f74e8056cc955e1412b50c69e7aeb4168` |
| `REAL_TASK_018.json` | State Machines/Retries | `976822a464df65b57cb10475c24d8c1a84edf0c74d9b23d0e2e5de7e68e8300e` |
| `REAL_TASK_019.json` | Scheduling/Intervals | `e0eff21df03f42400f046896eab9f4d77b38f843f28e37b6ce71ede52812226e` |
| `REAL_TASK_020.json` | Graphs/Trees | `b7dc08f739723e5a55beeeade61293c7ec5efca259f67fb9280480f82fa65066` |

## 3. Natural Logic Fault Inventory Summary (15 Faults)

| Task ID | Function Name | Category | Difficulty | Kill Ratio | Coder Model |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `REAL_TASK_001` | `parse_github_url` | Parsing/String | **Hard** | 5/6 (16.7%) | llama-3.3-70b-instruct |
| `REAL_TASK_002` | `split_by_positions` | Parsing/String | **Medium** | 2/4 (50.0%) | llama-3.3-70b-instruct |
| `REAL_TASK_003` | `get_parent_dn` | Parsing/String | **Medium** | 2/5 (60.0%) | llama-3.3-70b-instruct |
| `REAL_TASK_004` | `validate_tags` | Parsing/String | **Hard** | 4/5 (20.0%) | llama-3.1-8b-instruct |
| `REAL_TASK_005` | `split_host_port` | Parsing/String | **Medium** | 3/7 (57.1%) | llama-3.3-70b-instruct |
| `REAL_TASK_006` | `get_consistent_hash_node` | Algorithms/Search | **Medium** | 2/4 (50.0%) | llama-3.3-70b-instruct |
| `REAL_TASK_010` | `find_conflicting_reservations` | Graphs/Trees | **Easy** | 1/4 (75.0%) | llama-3.1-8b-instruct |
| `REAL_TASK_011` | `check_half_open_overlap` | Scheduling/Intervals | **Hard** | 5/6 (16.7%) | llama-3.3-70b-instruct |
| `REAL_TASK_013` | `intersect_intervals` | Scheduling/Intervals | **Hard** | 4/5 (20.0%) | llama-3.3-70b-instruct |
| `REAL_TASK_015` | `compute_fibonacci_backoff_sequence` | Algorithms/Search | **Easy** | 1/3 (66.7%) | qwen-2.5-7b-instruct |
| `REAL_TASK_016` | `evaluate_token_bucket` | State Machines/Retries | **Hard** | 6/7 (14.3%) | llama-3.3-70b-instruct |
| `REAL_TASK_017` | `check_sliding_window_rate_limit` | State Machines/Retries | **Hard** | 8/9 (11.1%) | llama-3.3-70b-instruct |
| `REAL_TASK_018` | `evaluate_circuit_breaker_transition` | State Machines/Retries | **Hard** | 7/9 (22.2%) | llama-3.3-70b-instruct |
| `REAL_TASK_019` | `merge_overlapping_intervals` | Scheduling/Intervals | **Hard** | 3/4 (25.0%) | llama-3.3-70b-instruct |
| `REAL_TASK_020` | `detect_dag_cycle_and_ancestors` | Graphs/Trees | **Medium** | 2/5 (60.0%) | llama-3.3-70b-instruct |

## 4. Methodological Compliance Guarantee
- **Zero Synthetic Mutations:** All 15 faults are 100% natural completions from live LLMs.
- **Ceiling Effect Elimination:** 8 Hard (53.3%), 5 Medium (33.3%), 2 Easy (13.3%).
- **Execution Integrity:** AST assertion instrumentation preserves complete runtime state without syntax hacks.