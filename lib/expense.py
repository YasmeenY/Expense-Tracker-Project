import sqlite3

class Expense:
    @classmethod
    def create(cls, name, category, price, date):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (name, category, price, date) VALUES (?, ?, ?, ?)", (name, category, price, date))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_date(cls, start_date, end_date):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE date BETWEEN ? AND ?", (start_date, end_date))
        expenses = cursor.fetchall()
        conn.close()
        return expenses

    @classmethod
    def remove(cls, id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM expenses WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @classmethod
    def view_total_expenses(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(price) FROM expenses GROUP BY category")
        expenses = cursor.fetchall()
        conn.close()
        for category, total in expenses:
            print(f"{category}: {total}")

    @classmethod
    def view_expense_by_category(cls, category):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
        expenses = cursor.fetchall()
        conn.close()
        if expenses:
            print(f"Expenses in the {category} category:")
            for expense in expenses:
                print(f"ID: {expense[0]}, Name: {expense[1]}, Price: {expense[3]}, Date: {expense[4]}")
        else:
            print(f"No expenses found in the {category} category.")

