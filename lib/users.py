import sqlite3

class Users:
    @classmethod
    def create(cls, first_name, last_name, password):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
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
        return row
    @classmethod
    def check_if_user_exists(cls, first_name, last_name):
        row = Users.get_id(first_name, last_name)
        if not row:
            return False
        else:
            return True
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
    @classmethod
    def delete_user(cls, user_id):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        sql = "DELETE FROM expenses where user_id = ?"
        sql1 = "DELETE FROM earnings where user_id = ?"
        sql2 = "DELETE FROM users where id = ?"
        cursor.execute(sql, (user_id,))
        cursor.execute(sql1, (user_id,))
        cursor.execute(sql2, (user_id,))
        conn.commit()
        conn.close()


