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
        return f"\033[91mUh oh! Your expenses exceed your earnings. {earnings - expenses} Time to start saving!\033[00m\U0001F641"
    elif expenses == earnings:
        return f"\033[93mBe careful You've spent as much as You've made. Total savings is 0. \033[00m\U0001F630"
    else:
        return f"\033[92mYou have saved ${earnings - expenses} this period. Nice!\033[00m\U0001F44D"

def warn_user(user_id):
    expenses = total_expenses(user_id)
    earnings = total_earnings(user_id)

    if expenses > earnings:
        return f"\033[91mUh oh! Your expenses exceed your earnings. {earnings - expenses} Time to start saving!\033[00m\U0001F641"
    elif expenses == earnings:
        return f"\033[93mBe careful You've spent as much as You've made. Total savings is 0\033[00m\U0001F630"

