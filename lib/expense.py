import sqlite3

class Expense:
    @classmethod
    def create(cls, name, category, price, date, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (name, category, price, date, user_id) VALUES (?, ?, ?, ?, ?)", (name, category, price, date, user_id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_date(cls, start_date, end_date, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ? AND user_id = ?", (start_date, end_date, user_id))
        expenses = cursor.fetchall()
        conn.close()
        if expenses:
            for expense in expenses:
                print(f"ID: {expense[0]}, Name: {expense[1]}, Price: ${expense[3]}, Date: {expense[4]}")
            return ""
        else:
            return (f"\nNo expenses found between {start_date} and {end_date}.")

    @classmethod
    def remove(cls, id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @classmethod
    def view_expense_by_category(cls, category, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE category = ? AND user_id = ?", (category,user_id))
        expenses = cursor.fetchall()
        conn.close()
        if expenses:
            print(f"\nExpenses in the {category} category:\n")
            for expense in expenses:
                print(f"ID: {expense[0]}, Name: {expense[1]}, Price: ${expense[3]}, Date: {expense[4]}")
        else:
            print(f"\nNo expenses found in the {category} category.\n")

    @classmethod
    def find_user_categories(cls, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = """
            SELECT category from expenses WHERE user_id = ?
        """
        cursor.execute(sql, (user_id,))
        expenses = cursor.fetchall()
        conn.close()
        categories = []
        for row in expenses:
            categories.append(row[0])
        return set(categories)
    
    @classmethod
    def view_total_expenses(cls, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        for category in Expense.find_user_categories(user_id):
            sql = """
                SELECT SUM(price) FROM expenses WHERE category = ? AND user_id = ?
            """
            cursor.execute(sql, (category, user_id))
            row = cursor.fetchone()
            print(f"The Total Expense in {category} is ${row[0]}")
        conn.close()
        return ""


