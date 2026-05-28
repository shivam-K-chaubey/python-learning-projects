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