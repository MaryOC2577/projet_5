"""Config file."""

from pathlib import Path


BASE_DIR = Path(".").resolve()
APP_DIR = BASE_DIR / "application"
DATA_DIR = APP_DIR / "data"


SCRIPTSQL = DATA_DIR / "scriptsql.sql"
