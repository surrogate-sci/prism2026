import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).parents[1]
VALIDATOR = ROOT / "scripts/validate_publication_metadata.py"
PUBLICATION_TITLE = "PRISM 2026: Scientific Causal Reasoning for Interpretability"
REPOSITORY_URL = "https://github.com/surrogate-sci/prism2026"
PUBLICATION_URL = "https://surrogate-sci.github.io/prism2026/"


def test_prism_metadata_and_public_links_replace_template_values():
    variables = yaml.safe_load((ROOT / "_variables.yml").read_text())
    citation = (ROOT / "CITATION.cff").read_text()
    active_docs = "\n".join(
        path.read_text()
        for path in (
            ROOT / "README.md",
            ROOT / "pages/CONTRIBUTING.qmd",
            ROOT / "pages/FAQ.qmd",
            ROOT / "pages/SETUP.qmd",
            ROOT / "_variables.yml",
            ROOT / "CITATION.cff",
            ROOT / "ai-use.yml",
        )
    )

    assert variables["pub"] == {
        "org": "surrogate-sci",
        "repo": "prism2026",
        "title": PUBLICATION_TITLE,
    }
    assert f'title: "{PUBLICATION_TITLE}"' in citation
    assert f"repository-code: {REPOSITORY_URL}" in citation
    assert f"url: {PUBLICATION_URL}" in citation
    assert "science-pub-template" not in active_docs
    assert "surrogate-sci.dev" not in active_docs
    assert "[REPOSITORY-NAME]" not in active_docs
    assert "[REPO-NAME]" not in active_docs
    assert "[PUBLICATION TITLE]" not in active_docs
    assert "[PUB-TITLE]" not in active_docs


def test_readme_is_a_student_facing_quick_start():
    readme = (ROOT / "README.md").read_text()

    for required in (
        PUBLICATION_TITLE,
        PUBLICATION_URL,
        "Student quick start",
        "make preview-warm",
        "make preview-technical",
        "index.ipynb",
        "authors.yml",
        "ai-use.yml",
        "CRediT",
        "ref.bib",
        "pull request",
        "pages/CONTRIBUTING.qmd",
    ):
        assert required in readme


def test_contribution_guide_covers_the_reviewed_student_workflow():
    guide = (ROOT / "pages/CONTRIBUTING.qmd").read_text()

    for required in (
        "branch",
        "index.ipynb",
        "make preview-warm",
        "make preview-technical",
        "authors.yml",
        "CRediT",
        "ai-use.yml",
        "ref.bib",
        "pull request",
        "review",
        "main",
        PUBLICATION_URL,
    ):
        assert required.lower() in guide.lower()


def test_agent_guidance_is_shared_without_committing_agent_session_folders():
    agents = (ROOT / "AGENTS.md").read_text()
    claude = (ROOT / "CLAUDE.md").read_text()

    assert "@AGENTS.md" in claude
    for required in (
        "Do not change the publication theme",
        "Do not commit session notes",
        "make render-warm",
        "make render-technical",
        "ai-use.yml",
        "CRediT",
        "pull request",
    ):
        assert required in agents
    assert not (ROOT / ".agents").exists()
    assert not (ROOT / ".claude").exists()


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
