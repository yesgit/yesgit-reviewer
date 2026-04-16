import json
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "duck-code-reviewer"
SCRIPT_ROOT = SKILL_ROOT / "scripts"


def run_script(*args: str, cwd: Path | None = None) -> str:
    completed = subprocess.run(
        ["python3", *args],
        cwd=cwd or REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def skill_script(name: str) -> str:
    return str(SCRIPT_ROOT / name)


class ScriptTests(unittest.TestCase):
    def test_packaged_skill_is_self_contained(self) -> None:
        skill_root = SKILL_ROOT
        skill = (skill_root / "SKILL.md").read_text(encoding="utf-8")
        agent = (skill_root / "agents" / "openai.yaml").read_text(encoding="utf-8")

        self.assertIn("name: duck-code-reviewer", skill)
        self.assertNotIn("../../references", skill)
        self.assertTrue((skill_root / "references" / "input-modes.md").is_file())
        self.assertTrue((skill_root / "scripts" / "normalize_diff.py").is_file())
        self.assertIn("quick review passes", agent)

    def test_quick_review_mode_is_documented_consistently(self) -> None:
        skill = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        input_modes = (SKILL_ROOT / "references" / "input-modes.md").read_text(encoding="utf-8")
        output_format = (SKILL_ROOT / "references" / "output-format.md").read_text(encoding="utf-8")
        scoring = (SKILL_ROOT / "references" / "scoring.md").read_text(encoding="utf-8")
        agent = (SKILL_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")

        self.assertIn("quick review", skill)
        self.assertIn("compact, decision-oriented triage", skill)
        self.assertIn("### Quick review", input_modes)
        self.assertIn("high-signal findings rather than exhaustive coverage", input_modes)
        self.assertIn("Coverage note: quick review, not exhaustive", output_format)
        self.assertIn("Use `1-10` by default for quick review mode.", scoring)
        self.assertIn("quick review passes", agent)
        self.assertIn("review or quickly review", agent)

    def test_discover_constraints_finds_reference_docs_in_skill_style_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (root / "references").mkdir()
            (root / "references" / "architecture-review.md").write_text("# rules\n", encoding="utf-8")
            (root / "references" / "general-design-principles.md").write_text("# advisory\n", encoding="utf-8")

            data = json.loads(run_script(skill_script("discover_constraints.py"), str(root)))
            paths = {entry["path"] for entry in data}

            self.assertIn("SKILL.md", paths)
            self.assertIn("references/architecture-review.md", paths)
            self.assertIn("references/general-design-principles.md", paths)

    def test_discover_constraints_finds_skill_and_style_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (root / ".editorconfig").write_text("root = true\n", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / ".eslintrc.json").write_text("{}", encoding="utf-8")

            data = json.loads(run_script(skill_script("discover_constraints.py"), str(root)))
            paths = {entry["path"] for entry in data}

            self.assertIn("SKILL.md", paths)
            self.assertIn(".editorconfig", paths)
            self.assertIn("src/.eslintrc.json", paths)

    def test_resolve_effective_constraints_prefers_nearest_configs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".editorconfig").write_text("root = true\n", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / ".eslintrc.json").write_text("{}", encoding="utf-8")
            (root / "src" / "index.ts").write_text("export const value = 1;\n", encoding="utf-8")

            data = json.loads(run_script(skill_script("resolve_effective_constraints.py"), str(root), "src/index.ts"))

            self.assertEqual(data[0]["path"], "src/.eslintrc.json")
            self.assertEqual(data[1]["path"], ".editorconfig")

    def test_resolve_effective_constraints_includes_reference_docs_from_repo_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (root / "references").mkdir()
            (root / "references" / "architecture-review.md").write_text("# rules\n", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / "index.ts").write_text("export const value = 1;\n", encoding="utf-8")

            data = json.loads(run_script(skill_script("resolve_effective_constraints.py"), str(root), "src/index.ts"))
            paths = [entry["path"] for entry in data]

            self.assertIn("SKILL.md", paths)
            self.assertIn("references/architecture-review.md", paths)

    def test_infer_design_constraints_recognizes_non_python_imports(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "src" / "services").mkdir(parents=True)
            (root / "src" / "repositories").mkdir(parents=True)
            (root / "src" / "services" / "userService.js").write_text(
                'const repo = require("../repositories/userRepo");\n',
                encoding="utf-8",
            )
            (root / "src" / "services" / "goService.go").write_text(
                textwrap.dedent(
                    """
                    package services

                    import (
                        "project/repositories"
                    )
                    """
                ).strip()
                + "\n",
                encoding="utf-8",
            )

            data = json.loads(run_script(skill_script("infer_design_constraints.py"), str(root)))

            self.assertEqual(data["import_tendencies"]["service"]["repository"], 2)

    def test_summarize_findings_supports_chinese_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            review = root / "chunk.md"
            review.write_text("### High\n- Example\n", encoding="utf-8")

            output = run_script(skill_script("summarize_findings.py"), "--lang", "zh", str(review))

            self.assertIn("## 总结", output)
            self.assertIn("## 分块审查结果", output)
            self.assertIn("## 收尾说明", output)


if __name__ == "__main__":
    unittest.main()
