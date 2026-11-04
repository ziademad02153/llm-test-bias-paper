import json
from pathlib import Path

d = json.loads(Path('data/fault_harvest/accepted_faults.json').read_text(encoding='utf-8'))
for k, v in sorted(d.items()):
    pas = v['passed_asserts']
    fld = v['failed_asserts']
    tot = v['total_asserts']
    kr = v['kill_ratio']
    status = "<= 50% VALID" if kr <= 0.50 else "> 50% EXCEEDS"
    print(f"{k}: {pas}/{tot} Passed | {fld}/{tot} Failed ({kr:.1%}) -> {status}")

