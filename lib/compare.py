import sqlite3

def total_expenses():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(price) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()

    return total if total else 0

def total_earnings():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM earnings")
    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0

def compare():
    expenses = total_expenses()
    earnings = total_earnings()

    if expenses > earnings:
        return f"Warning! Your expenses exceed your earnings. {earnings - expenses} "
    else:
        return f"You have saved {earnings - expenses} this period."
