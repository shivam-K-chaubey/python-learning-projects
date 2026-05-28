import sqlite3

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("quiz_game.db")
        self.cursor = self.connection.cursor()
        self.create_users_table()

    def create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        self.connection.commit()
    def create_user(self, username, password):
        try:
            self.cursor.execute("""
                INSERT INTO users (username, password)
                VALUE (?, ?)
            """, (username, password))
            self.connection.commit()
            return True

        except sqlite3.IntegrityError:
            return False

    def validate_user(self, username, password):
        self.cursor.execute("""
            SELECT * FROM users
            WHERE username = ? AND password = ?
        """, (username, password))

        user = self.cursor.fetchone()

        return user is not None