import sqlite3
from seed import add_to_db

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    date TEXT,
    user_id INTEGER)
""")

CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS earnings
    (id INTEGER PRIMARY KEY,
    source TEXT,
    category TEXT,
    amount REAL,
    date TEXT,
    user_id INTEGER)
""")


# Create 'users' table if it doesn't exist
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    password TEXT,
    UNIQUE(first_name, last_name))
""")

CONN.commit()
CONN.close()

add_to_db()