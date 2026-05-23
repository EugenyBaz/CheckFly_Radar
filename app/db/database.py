from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DB_PATH = BASE_DIR / "data" / "checkfly_radar.db"
SCHEMA_PATH = BASE_DIR / "app" / "db" / "schema.sql"


def get_connection() -> sqlite3.Connection:
    """
    Create and return SQLite connection.
    """

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def init_db() -> None:
    """
    Initialize database using schema.sql
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = get_connection()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        schema_sql = schema_file.read()

    connection.executescript(schema_sql)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")
