# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A minimal Python project containing a single module, `app.py`, which exposes `validate_email(email)`: it returns `True` if the input is a string that matches `EMAIL_RE` after leading and trailing whitespace is stripped. It returns `False` for anything that isn't a string.

## Commands

```bash
pip install -r requirements.txt          # installs pytest (the only dependency)
pytest                                   # run all tests
pytest path/to/test_file.py::test_name   # run a single test
```

No tests exist yet. pytest discovers `test_*.py` / `*_test.py` files, so new tests should follow that naming (e.g. `test_app.py` importing `from app import validate_email`). No linter, formatter, or build step is configured.
