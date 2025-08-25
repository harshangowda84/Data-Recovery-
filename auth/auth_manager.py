import sqlite3
import hashlib

DB_PATH = 'auth/users.db'

class AuthManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_user_table()

    def create_user_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )''')
        self.conn.commit()

    def register_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def verify_user(self, username, password):
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.conn.execute('SELECT * FROM users WHERE username=? AND password_hash=?', (username, password_hash))
        return cursor.fetchone() is not None
