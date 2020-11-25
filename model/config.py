"""Config file."""

from pathlib import Path


BASE_DIR = Path(".").resolve()
DATA_DIR = BASE_DIR / "data"

SCRIPTSQL = DATA_DIR / "scriptsql.sql"
