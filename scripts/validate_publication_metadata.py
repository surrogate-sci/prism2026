#!/usr/bin/env python3
"""Reject unresolved publication placeholders and stale template links."""

import argparse
from pathlib import Path

ROOT = Path(__file__).parents[1]
FORBIDDEN = (
    "science-pub-template",
    "surrogate-sci.dev",
    "[REPOSITORY-NAME]",
    "[REPO-NAME]",
    "[PUBLICATION TITLE]",
    "[PUB-TITLE]",
    "[AUTHOR FAMILY NAME]",
    "[AUTHOR GIVEN NAME]",
    "[FIRST AUTHOR NAME]",
    "[LAST AUTHOR NAME]",
    "[OTHER AUTHOR NAME]",
    "<author name",
)
ROOT_FILES = (
    "README.md",
    "_variables.yml",
    "CITATION.cff",
    "authors.yml",
    "ai-use.yml",
    "pyproject.toml",
    "uv.lock",
    "index.ipynb",
)
CONTENT_DIRECTORIES = ("pages", "developer-docs", "examples")
CONTENT_SUFFIXES = {".md", ".qmd", ".ipynb", ".bib"}


def default_paths() -> list[Path]:
    """Return publication-authored files that must be free of template residue."""
    paths = [ROOT / relative for relative in ROOT_FILES]
    for directory in CONTENT_DIRECTORIES:
        paths.extend(
            path
            for path in (ROOT / directory).rglob("*")
            if path.is_file() and path.suffix in CONTENT_SUFFIXES
        )
    return sorted(paths)


def find_violations(paths: list[Path]) -> list[str]:
    """Return a readable violation for every forbidden token in each file."""
    violations: list[str] = []
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            violations.append(f"{path}: {error}")
            continue
        for token in FORBIDDEN:
            if token in text:
                violations.append(f"{path}: contains {token}")
    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check publication files for stale template names, links, and placeholders."
    )
    parser.add_argument("paths", nargs="*", type=Path, help="Specific files to validate")
    args = parser.parse_args(argv)

    paths = args.paths or default_paths()
    violations = find_violations(paths)
    if violations:
        parser.error("Publication metadata validation failed:\n" + "\n".join(violations))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
