import sqlite3

class Database:
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT NOT NULL,
                                    password TEXT NOT NULL,
                                    is_admin BOOLEAN NOT NULL DEFAULT 0)''')
            self.conn.execute('''CREATE TABLE IF NOT EXISTS books (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT NOT NULL,
                                    author TEXT NOT NULL,
                                    description TEXT,
                                    available BOOLEAN NOT NULL DEFAULT 1)''')

    def execute_query(self, query, params=()):
        with self.conn:
            cursor = self.conn.execute(query, params)
            return cursor

    def close(self):
        self.conn.close()
