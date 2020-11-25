"""Main."""

from model.create import InitDatabase
from config import SCRIPTSQL

database = InitDatabase()

database.executesql(SCRIPTSQL)
