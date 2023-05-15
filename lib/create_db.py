import sqlite3

# Establish a connection to the SQLite database
CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

# Create 'expenses' table if it doesn't exist
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL)
""")

# Create 'earnings' table if it doesn't exist
CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS earnings
    (id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    amount REAL)
""")

# Commit the changes and close the connection
CONN.commit()
CONN.close()
