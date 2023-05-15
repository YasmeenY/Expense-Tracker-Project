import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    date TEXT)
""")

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS earnings
    (id INTEGER PRIMARY KEY,
    source TEXT,
    category TEXT,
    amount REAL,
    date TEXT)
""")

CONN.commit()
CONN.close()
