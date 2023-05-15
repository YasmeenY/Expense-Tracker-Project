import sqlite3

EARNINGS_CATEGORIES = ["Passive Income", "Salary", "Freelance", "Gifts"]

class Earnings:
    @staticmethod
    def create(name, category, amount):
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Insert a new earning into the 'earnings' table
        cursor.execute("INSERT INTO earnings (name, category, amount) VALUES (?, ?, ?)", (name, category, amount))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_category(category):
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Select all earnings with the provided category
        cursor.execute("SELECT * FROM earnings WHERE category = ?", (category,))

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

        # Delete the earning with the provided name and category
        cursor.execute("DELETE FROM earnings WHERE name = ? AND category = ?", (name, category))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
    @staticmethod
    def total():
        for category in EARNINGS_CATEGORIES:
            # Connect to the database
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            # Delete the expense with the provided name and category
            cursor.execute("SELECT SUM(amount) FROM earnings WHERE category = ?", (category,))
            row = cursor.fetchone()
            if row[0] == None:
                print(f"You Haven't earned anything in {category}")
            else:
                print(f"The Total Earnings in {category} is {row[0]}")

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
