import sqlite3

def total_expenses(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(price) FROM expenses WHERE user_id = ?", (user_id,))
    total = cursor.fetchone()[0]
    conn.close()

    return total if total else 0

def total_earnings(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT SUM(amount) FROM earnings WHERE user_id = ?", (user_id,))
    total = cursor.fetchone()[0]
    conn.close()

    return total if total else 0

def compare(user_id):
    expenses = total_expenses(user_id)
    earnings = total_earnings(user_id)

    if expenses > earnings:
        return f"Uh oh! Your expenses exceed your earnings. {earnings - expenses} Time to start saving!"
    else:
        return f"You have saved ${earnings - expenses} this period. Nice!"
