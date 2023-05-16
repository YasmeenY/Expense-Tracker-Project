import sqlite3

class Users:
    @classmethod
    def create(cls, first_name, last_name, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = """
            SELECT * FROM users
            WHERE (first_name, last_name) = (?, ?)
            LIMIT 1
        """

        row = cursor.execute(sql, (first_name, last_name)).fetchone()
        if not row:
            sql = """
                INSERT INTO users (first_name, last_name, password)
                VALUES (?, ?, ?)
            """

            cursor.execute(sql, (first_name, last_name, password))
        conn.commit()
        conn.close()
    @classmethod
    def get_id(cls, first_name, last_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = """
            SELECT * FROM users WHERE (first_name, last_name) = (?,?)
            LIMIT 1
        """
        row = cursor.execute(sql, (first_name, last_name)).fetchone()
        conn.commit()
        conn.close()
        return row[0]
    @classmethod
    def get_password(cls, first_name, last_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = """
            SELECT password FROM users WHERE (first_name, last_name) = (?,?)
            LIMIT 1
        """
        row = cursor.execute(sql, (first_name, last_name)).fetchone()
        conn.commit()
        conn.close()
        return row[0]


