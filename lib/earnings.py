import sqlite3

class Earnings:
    @classmethod
    def create(cls, source, category, amount, date):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO earnings (source, category, amount, date) VALUES (?, ?, ?, ?)", (source, category, amount, date))
        conn.commit()
        conn.close()

    @classmethod
    def find_by_date(cls, start_date, end_date):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM earnings WHERE date BETWEEN ? AND ?", (start_date, end_date))
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
    def view_total_earnings(cls):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM earnings GROUP BY category")
        earnings = cursor.fetchall()
        conn.close()
        for category, total in earnings:
            print(f"{category}: {total}")

    @classmethod
    def view_earnings_by_category(cls, category):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM earnings WHERE category = ?", (category,))
        earnings = cursor.fetchall()
        conn.close()
        if earnings:
            print(f"Earnings in the {category} category:")
            for earning in earnings:
                print(f"ID: {earning[0]}, Source: {earning[1]}, Amount: {earning[3]}, Date: {earning[4]}")
        else:
            print(f"No earnings found in the {category} category.")
