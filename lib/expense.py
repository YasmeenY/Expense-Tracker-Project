import sqlite3

CONN = sqlite3.connect("database.db")
CURSOR = CONN.cursor()

class Expense():
    def __init__(self, name, category, price):
        self.id = None
        self.name = name
        self.category = category
        self.price = price

    def save(self):
        sql = """
            INSERT INTO expenses (name, category, price)
            VALUES ( ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.category, self.price))
        CONN.commit()

        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM expenses").fetchone()[0]

    @classmethod
    def create(cls, name, category, price):
        expense = Expense(name, category, price)
        expense.save()
        return expense
    
    ##not working yet
    @classmethod
    def find_by_category(cls, category):
        sql = """
            SELECT * FROM expenses
            WHERE category = ?
            LIMIT 1
        """

        rows = CURSOR.execute(sql, (category,)).fetchmany(2)
        
        for row in rows:
            return Expense(
                name=row[1],
                category=row[2],
                price =row[3],
            )
        if not row:
            return None