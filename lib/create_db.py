import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()


CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL)
""")

CONN.commit()
CONN.close()