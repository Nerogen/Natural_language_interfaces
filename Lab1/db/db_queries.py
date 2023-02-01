import sqlite3

from Lab1.db.config import CREATE_TABLE, DB_NAME


def write_to_db(db_name: str = DB_NAME, text: str = '') -> None:
    """Write to db file data"""
    with sqlite3.connect(f"../db/{DB_NAME}.db") as db:
        cursor = db.cursor()
        cursor.execute(CREATE_TABLE)
        db.commit()


def create_db() -> None:
    """Create new db with table if not exist"""
    with sqlite3.connect(f"../db/{DB_NAME}.db") as db:
        cursor = db.cursor()
        cursor.execute(CREATE_TABLE)
        db.commit()
