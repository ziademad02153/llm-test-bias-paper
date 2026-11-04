"""Build a public analysis package using an explicit file allowlist."""
import csv
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "data/main_experiment_results"
RESTRICTED = {f"REAL_TASK_{n:03d}" for n in (4, 6, 10, 11, 19, 20)}
accepted = json.loads((ROOT / "data/fault_harvest/accepted_faults.json").read_text(encoding="utf-8-sig"))
included = set(accepted) - RESTRICTED
files = {}
def add(path):
    files[path] = (ROOT / path).read_bytes()

for name in ("main_glmm_dataset.csv", "GLMM_OUTPUT.txt", "GLMM_COEFFICIENTS.csv",
             "GLMM_DIAGNOSTICS.csv", "PROBLEM_LEVEL_SENSITIVITY.csv",
             "GLMM_RANDOM_SLOPES_SENSITIVITY.csv", "GLMM_RANDOM_SLOPES_OUTPUT.txt"):
    path = RESULTS / name
    if path.exists():
        add(path.relative_to(ROOT).as_posix())
add("scripts/fit_interaction_glmm.R")
add("src/stats_utils.py")
for task in sorted(included):
    add(f"data/problems/{task}.json")
files["data/fault_harvest/accepted_faults_public.json"] = json.dumps(
    {k: v for k, v in accepted.items() if k in included}, indent=2, ensure_ascii=False
).encode("utf-8")
tests = 0
for path in sorted((RESULTS / "generated_tests").glob("*.py")):
    task = re.search(r"REAL_TASK_\d{3}", path.name)
    if task and task.group() in included:
        add(path.relative_to(ROOT).as_posix())
        tests += 1

# Metadata for all tasks contains identifiers and source pointers only.
metadata = []
for task in sorted(accepted):
    problem = json.loads((ROOT / f"data/problems/{task}.json").read_text(encoding="utf-8-sig"))
    metadata.append({k: problem.get(k, "") for k in
                     ("problem_id", "function_name", "repo_url", "commit_hash", "commit_date", "author")})
    metadata[-1]["source_included"] = task in included
files["data/task_source_metadata.json"] = json.dumps(metadata, indent=2).encode()
for path in ("data/licenses/LICENSE-MIT.txt", "data/licenses/LICENSE-GPL3.txt"):
    add(path)
notices = (ROOT / "data/licenses/COPYRIGHT_NOTICES.txt").read_text(encoding="utf-8-sig")
# Keep the original notices for the included MIT/GPL artifacts, without fair-use assertions.
split = re.search(r"(?m)^3\. ", notices)
if not split:
    raise ValueError("Cannot locate excluded-source notice section")
files["data/licenses/COPYRIGHT_NOTICES.txt"] = (
    notices[:split.start()] +
    "\nThe six tasks without an established redistribution license are excluded from this public source subset.\n"
).encode("utf-8")

statement = """The supplementary public package contains all 900 recorded condition outcomes across 225 matched trials on 15 tasks and the R scripts and outputs needed to reproduce the statistical analyses. Source implementations, task specifications and generated test suites are supplied for nine tasks with documented licenses. Source-bearing artifacts for six tasks (REAL_TASK_004, 006, 010, 011, 019 and 020) are withheld pending clarification of redistribution permission. Their numerical outcomes and source repository/commit pointers remain included. Consequently, the public package supports reanalysis of the full study but does not support complete re-execution of test evaluation for the six withheld tasks. No numerical outcomes were removed or recalculated for this release.
"""
files["DATA_AVAILABILITY.txt"] = statement.encode()
files["README.md"] = ("""# Public analysis and licensed-source subset

This is supplementary_material_public.zip, prepared for journal submission.
The separate historical supplementary_material.zip contains restricted-source artifacts and should not be used as the public release.

""" + statement + """
## Reproduce the full statistical analysis

Install R and lme4, then run from the extracted package directory:

    Rscript scripts/fit_interaction_glmm.R data/main_experiment_results/main_glmm_dataset.csv

This uses the numerical results from all 15 tasks. It needs no API key.
GLMM_OUTPUT.txt records R/lme4 versions and the model diagnostics.

## Included source subset

Nine tasks and 540 generated test-suite files are included. The subset is for source inspection; a turnkey regeneration harness is not included in this public package.
Source license classifications are carried over from the project's provenance audit. Check the upstream license terms for reuse. No blanket license is applied to third-party artifacts.
The GPL source subset is REAL_TASK_005 and its associated artifacts. Preserve its license and modification notices.
No claim that the withheld material qualifies for fair use is made in this package.
Numerical outputs for withheld tasks contain identifiers, counts and measurements, not source implementations or assertions.

## Release status

This archive is prepared locally. Upload this exact public archive and update the paper's repository link/version before claiming it is publicly accessible.
Any previously uploaded unrestricted archives and source copies require a separate repository review.
""").encode()

rows = list(csv.DictReader(io.StringIO(files["data/main_experiment_results/main_glmm_dataset.csv"].decode())))
assert len(rows) == 900 and len({(r["trial_id"], r["condition"]) for r in rows}) == 900
assert len(included) == 9 and tests == 540
# Scan all payloads without exposing any matched values.
for name, content in files.items():
    assert not re.search(r"(?i)(^|/)(\.env|\.git)(/|$)", name)
    if re.search(rb"sk-or-v1-[a-zA-Z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----", content):
        raise ValueError(f"Credential-like content in {name}")
    for task in RESTRICTED:
        if task in name and ("/generated_tests/" in name or "/problems/" in name):
            raise ValueError(f"Restricted source path {name}")
manifest = {
    "rows": len(rows), "tasks": 15, "source_tasks": sorted(included),
    "withheld_source_tasks": sorted(RESTRICTED), "generated_tests": tests,
    "full_source_regeneration_supported": False,
    "sha256": {name: hashlib.sha256(content).hexdigest() for name, content in files.items()}
}
files["PUBLIC_PACKAGE_MANIFEST.json"] = json.dumps(manifest, indent=2).encode()
output = ROOT / "supplementary_material_public.zip"
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for name, content in files.items():
        archive.writestr(name, content)
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    assert archive.read("data/main_experiment_results/main_glmm_dataset.csv") == (RESULTS / "main_glmm_dataset.csv").read_bytes()
print(json.dumps({"files": len(files), "tests": tests, "data_rows": len(rows), "bytes": output.stat().st_size}))
(ROOT / "PUBLIC_DATA_AVAILABILITY.txt").write_text(statement, encoding="utf-8")
