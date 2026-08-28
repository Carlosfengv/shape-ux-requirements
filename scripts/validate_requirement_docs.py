#!/usr/bin/env python3
"""Compatibility launcher for the delivery skill's requirement validator."""

from __future__ import annotations

import runpy
from pathlib import Path


VALIDATOR = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "deliver-ux-requirements"
    / "scripts"
    / "validate_requirement_docs.py"
)


if __name__ == "__main__":
    runpy.run_path(str(VALIDATOR), run_name="__main__")
