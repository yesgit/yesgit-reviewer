import json
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def run_script(*args: str, cwd: Path | None = None) -> str:
    completed = subprocess.run(
        ["python3", *args],
        cwd=cwd or REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


class ScriptTests(unittest.TestCase):
    def test_discover_constraints_finds_reference_docs_in_skill_style_repo(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (root / "references").mkdir()
            (root / "references" / "architecture-review.md").write_text("# rules\n", encoding="utf-8")
            (root / "references" / "general-design-principles.md").write_text("# advisory\n", encoding="utf-8")

            data = json.loads(run_script("scripts/discover_constraints.py", str(root)))
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

            data = json.loads(run_script("scripts/discover_constraints.py", str(root)))
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

            data = json.loads(run_script("scripts/resolve_effective_constraints.py", str(root), "src/index.ts"))

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

            data = json.loads(run_script("scripts/resolve_effective_constraints.py", str(root), "src/index.ts"))
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

            data = json.loads(run_script("scripts/infer_design_constraints.py", str(root)))

            self.assertEqual(data["import_tendencies"]["service"]["repository"], 2)

    def test_summarize_findings_supports_chinese_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            review = root / "chunk.md"
            review.write_text("### High\n- Example\n", encoding="utf-8")

            output = run_script("scripts/summarize_findings.py", "--lang", "zh", str(review))

            self.assertIn("## 总结", output)
            self.assertIn("## 分块审查结果", output)
            self.assertIn("## 收尾说明", output)


if __name__ == "__main__":
    unittest.main()
