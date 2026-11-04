import json

with open("data/fault_harvest/accepted_faults.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Original count: {len(data)}")
filtered = {k: v for k, v in data.items() if v["kill_ratio"] <= 0.50}
print(f"Compliant count (kill_ratio <= 0.50): {len(filtered)}")
for k, v in sorted(filtered.items()):
    print(f"  {k:<14} | {v['function_name']:<25} | Fail: {v['failed_asserts']}/{v['total_asserts']} ({v['kill_ratio']:.1%}) | {v['difficulty']}")

# Overwrite accepted_faults.json with compliant faults only
with open("data/fault_harvest/accepted_faults.json", "w", encoding="utf-8") as f:
    json.dump(filtered, f, indent=2, ensure_ascii=False)
print("Updated accepted_faults.json to contain only compliant faults.")

