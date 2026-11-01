import json
import sys
from pathlib import Path

# Ensure project root in sys.path
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.github_miner import GitHubMiner

def main():
    audit_dir = project_root / "data" / "clone_audit"
    audit_dir.mkdir(parents=True, exist_ok=True)

    problems_dir = project_root / "data" / "problems"
    for p in sorted(problems_dir.glob("*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        report = GitHubMiner.generate_clone_audit_report(
            function_name=data["function_name"],
            signature=data["signature"],
            func_code=data["ref_implementation"],
            repo_url=data.get("repo_url", ""),
            commit_hash=data.get("commit_hash", ""),
            commit_date=data.get("commit_date", "")
        )
        report_file = audit_dir / f"{data['problem_id']}_audit.json"
        report_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Generated audit artifact: {report_file.name}")

if __name__ == "__main__":
    main()
