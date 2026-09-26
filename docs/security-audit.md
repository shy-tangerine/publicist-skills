# Skill security audit

This report records the local static SkillSpector coverage of the complete Publicist Skills set at commit `31593234075fb40c0b41cc15e9ef820e1a52f499` on 2026-09-22. It is a point-in-time result, not an endorsement or a substitute for reviewing a skill before installation.

## 2026-09-22 result: complete 46-package set

| Scanner | Result | Scope and limitation |
| --- | --- | --- |
| [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) 2.11.2 | **Warn** | Static-only scans of all 46 packages from a clean Git archive. LLM analysis was disabled, and `--fail-on-incomplete` was used for every package. |

`Warn` means the scanner returned `CAUTION`; it does not mean that a vulnerability was confirmed.

The scan covered 5 country packages, 36 platform companions, and 5 cross-market packages. All 46 reports were written successfully and every report's component ledger inspected 100% of its components with zero partially or entirely uninspected files. One package (`launch-economics`) was complete; 45 were marked partial by non-fatal reference-resolution entries, so the aggregate result remains `CAUTION`. The 45 partial scans exited `1` under `--fail-on-incomplete`; the complete scan exited `0`. All 46 executions were otherwise successful.

The maximum package score was 19/100 (`LOW`). There were 24 reported matches across 13 packages. Every match was reviewed against the clean `31593234075fb40c0b41cc15e9ef820e1a52f499` archive: 24 were classified as false positives, with no confirmed finding and no needs-validation finding.

### Package detail

| Package | Score | Recommendation | Components | Findings | Exit |
|---|---:|---|---:|---:|---:|
| `publicist-us` | 15 | CAUTION | 10/10 (100%) | 2 | 1 |
| `publicist-germany` | 19 | CAUTION | 9/9 (100%) | 3 | 1 |
| `publicist-china` | 15 | CAUTION | 9/9 (100%) | 2 | 1 |
| `publicist-japan` | 15 | CAUTION | 9/9 (100%) | 2 | 1 |
| `publicist-brazil` | 7 | CAUTION | 9/9 (100%) | 1 | 1 |
| `publicist-brazil-assessoria-culture` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-brazil-lgpd-compliance` | 8 | CAUTION | 1/1 (100%) | 1 | 1 |
| `publicist-brazil-regional-media` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-brazil-whatsapp-pitch` | 7 | CAUTION | 1/1 (100%) | 1 | 1 |
| `publicist-brazil-wire-services` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-ai-compliance` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-bilibili` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-distribution` | 14 | CAUTION | 1/1 (100%) | 5 | 1 |
| `publicist-china-douyin` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-guanxi` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-pipl` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-prnasia` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-wechat` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-xiaohongshu` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-china-zhihu` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-germany-business-culture` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-germany-compliance` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-germany-pressclub` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-germany-pressrelease` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-germany-wireservice` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-japan-business-culture` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-japan-compliance` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-japan-fpcj` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-japan-kishaclub` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-japan-pressrelease` | 12 | CAUTION | 1/1 (100%) | 2 | 1 |
| `publicist-japan-prwire` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-compliance` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-crisis-playbook` | 8 | CAUTION | 1/1 (100%) | 1 | 1 |
| `publicist-us-freelancer-pitch` | 14 | CAUTION | 1/1 (100%) | 2 | 1 |
| `publicist-us-journalist-platforms` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-local-broadcast` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-local-seo` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-regional-media` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-state-government` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `publicist-us-trade-verticals` | 6 | CAUTION | 1/1 (100%) | 1 | 1 |
| `publicist-us-wire-services` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `cro` | 7 | CAUTION | 3/3 (100%) | 1 | 1 |
| `launch-economics` | 0 | SAFE | 1/1 (100%) | 0 | 0 |
| `pricing` | 0 | CAUTION | 4/4 (100%) | 0 | 1 |
| `signup` | 0 | CAUTION | 1/1 (100%) | 0 | 1 |
| `social` | 0 | CAUTION | 9/9 (100%) | 0 | 1 |

### Completeness and limitations

SkillSpector reported 125 non-fatal `reference_missing` entries across the 45 partial reports. They were all in `SKILL.md` reference resolution: 41 metadata `version` lines and 84 repository, sibling-skill, optional-context, or example-asset paths outside the installed package boundary. These entries explain the partial status; they did not leave a component uninspected. No baseline was supplied, no suppression was applied, and no source change was made in response.

Because `--no-llm` was used, this result covers SkillSpector's static, AST, taint, integrity, MCP-oriented, and YARA analyzers only. SkillSpector did not execute the bundled Python scripts. The result is not a runtime, provider, or deployment security assessment.

### Finding review

- **10 × `AS3`.** First-party sibling-skill paths in related-reference lists. These are navigation/documentation references, not instructions to enumerate peer instructions or access secrets.
- **7 × `EA2`.** Form-friction prose and safety controls covering consent, provider terms, optional wiki access, and data handling. They constrain behavior and grant no autonomous high-impact authority.
- **5 × `E1`.** Static provider URLs in the country `provider_wizard.py` metadata. Source review found offline selectors that return JSON guidance; no HTTP client, socket, upload, or data transmission is performed.
- **2 × `YR4`.** The word “Fierce” in trade-publication names such as Fierce Biotech and Fierce Pharma, not a reconnaissance or exploit tool.

All 24 matches were reviewed individually against the clean `31593234075fb40c0b41cc15e9ef820e1a52f499` archive and classified as false positives. No suppression file was added.

## Historical runs

The 2026-09-17 SkillSpector 2.11.2 rerun covered the prior 41-package set at `f82892a3e3796e92fc7aad96d74afd6eeb3c3fc1`. It used a clean Git-tree input and `--no-llm`; 24 packages reported zero findings, the maximum score was 14, and 18 matches across 13 packages were reviewed as false positives. The recursive command was limited to 32 packages, so the remaining nine were scanned individually. This historical result does not cover the five cross-market packages added afterward.

The original 2026-09-13 SkillSpector 2.11.0 run covered only the five country packages at `62fd3bbd9ccf56791244bf479a791e378ed2f8f0`. Its five matches were reviewed as false positives, but unresolved references left the reports partial. Neither historical run is a substitute for the 46-package result above.

## Reproduce the 46-package scan

Use the exact commit and a clean Git archive so ignored files, untracked local instructions, repository history, and local evidence are absent. Individual scans avoid SkillSpector's 32-package recursive discovery limit; do not replace this loop with one recursive scan and claim complete coverage.

```sh
REV=31593234075fb40c0b41cc15e9ef820e1a52f499
AUDIT_DIR="$(mktemp -d)"
git archive --format=tar "$REV" | tar -xf - -C "$AUDIT_DIR"
skillspector --version
mkdir "$AUDIT_DIR/reports" "$AUDIT_DIR/logs"
find "$AUDIT_DIR/skills" -mindepth 2 -maxdepth 2 -type f -name SKILL.md -printf '%h\n' | sort > "$AUDIT_DIR/skill-dirs.txt"
test "$(wc -l < "$AUDIT_DIR/skill-dirs.txt")" -eq 46

: > "$AUDIT_DIR/status.tsv"
while IFS= read -r skill_dir; do
  name=${skill_dir##*/}
  if skillspector scan "$skill_dir" \
      --no-llm --fail-on-incomplete --format json \
      --output "$AUDIT_DIR/reports/$name.json" \
      >"$AUDIT_DIR/logs/$name.stdout" \
      2>"$AUDIT_DIR/logs/$name.stderr"; then
    rc=0
  else
    rc=$?
  fi
  printf '%s\t%s\n' "$name" "$rc" >> "$AUDIT_DIR/status.tsv"
done < "$AUDIT_DIR/skill-dirs.txt"
```

Aggregate the 46 JSON files by `skill.name`, retaining each `risk_assessment`, `issues`, `execution_successful`, `analysis_completeness`, and recorded exit code. Report package counts, maximum score, rule counts, incomplete limitations, and source-reviewed classifications separately; a nonzero exit under `--fail-on-incomplete` is not itself a confirmed vulnerability.

Refresh this report after any material skill change and before publishing a claim based on a different revision.
