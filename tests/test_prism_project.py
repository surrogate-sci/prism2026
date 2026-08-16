import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
VALIDATOR = ROOT / "scripts/validate_publication_metadata.py"


def test_metadata_validator_blocks_template_links_and_placeholders(tmp_path):
    bad_readme = tmp_path / "README.md"
    bad_readme.write_text("https://surrogate-sci.github.io/science-pub-template/ [REPOSITORY-NAME]")
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(bad_readme)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert "science-pub-template" in result.stderr
    assert "[REPOSITORY-NAME]" in result.stderr


def test_metadata_validator_accepts_initialized_prism_publication():
    result = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_validation_action_runs_metadata_and_ai_disclosure_checks():
    workflow = (ROOT / ".github/workflows/validate-ai-use.yml").read_text()

    assert "python scripts/validate_publication_metadata.py" in workflow
    assert "python scripts/generate_ai_disclosure.py ai-use.yml --check" in workflow


def test_existing_theme_choice_is_preserved():
    config = (ROOT / "_quarto.yml").read_text()

    assert "default: warm-journal" in config
    assert "- [warm-journal, technical-notebook]" in config
