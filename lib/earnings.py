import sqlite3

class Earnings:
    @classmethod
    def create(cls, source, category, amount, date, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO earnings (source, category, amount, date, user_id) VALUES (?, ?, ?, ?, ?)", (source, category, amount, date, user_id))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_date(cls, start_date, end_date, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM earnings WHERE date BETWEEN ? AND ? AND user_id = ?", (start_date, end_date, user_id))
        earnings = cursor.fetchall()
        conn.close()
        return earnings

    @classmethod
    def remove(cls, id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM earnings WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    @classmethod
    def view_earnings_by_category(cls, category, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM earnings WHERE category = ? AND user_id = ?", (category,user_id))
        earnings = cursor.fetchall()
        conn.close()
        if earnings:
            print(f"Earnings in the {category} category:")
            for earning in earnings:
                print(f"ID: {earning[0]}, Source: {earning[1]}, Amount: {earning[3]}, Date: {earning[4]}")
        else:
            print(f"No earnings found in the {category} category.")

    @classmethod
    def find_user_categories(cls, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = """
            SELECT category from earnings WHERE user_id = ?
        """
        cursor.execute(sql, (user_id,))
        expenses = cursor.fetchall()
        conn.close()
        categories = []
        for row in expenses:
            categories.append(row[0])
        return set(categories)
    @classmethod
    def view_total_earnings(cls, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        for category in Earnings.find_user_categories(user_id):
            sql = """
                SELECT SUM(amount) FROM earnings WHERE category = ? AND user_id = ?
            """
            cursor.execute(sql, (category, user_id))
            row = cursor.fetchone()
            print(f"The Total Earnings in {category} is {row[0]}")
        conn.close()
        return ""
