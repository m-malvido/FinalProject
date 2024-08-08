from database import Database

class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def save(self):
        db = Database()
        db.execute_query("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)",
                         (self.username, self.password, self.is_admin))
        db.close()

    @staticmethod
    def authenticate(username, password):
        db = Database()
        user = db.execute_query("SELECT * FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        db.close()
        return user

class Book:
    def __init__(self, title, author, description=""):
        self.title = title
        self.author = author
        self.description = description
        self.available = True

    def save(self):
        db = Database()
        db.execute_query("INSERT INTO books (title, author, description, available) VALUES (?, ?, ?, ?)",
                         (self.title, self.author, self.description, self.available))
        db.close()
