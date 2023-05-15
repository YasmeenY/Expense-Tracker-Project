import sqlite3

class Expense:
    @staticmethod
    def create(name, category, price):
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Insert a new expense into the 'expenses' table
        cursor.execute("INSERT INTO expenses (name, category, price) VALUES (?, ?, ?)", (name, category, price))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_category(category):
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Select all expenses with the provided category
        cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))

        # Fetch all the matching records
        rows = cursor.fetchall()

        # Close the connection
        conn.close()

        # Return the fetched records
        return rows

    @staticmethod
    def delete(name, category):
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Delete the expense with the provided name and category
        cursor.execute("DELETE FROM expenses WHERE name = ? AND category = ?", (name, category))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()