import sqlite3

DB_PATH = 'cases/cases.db'

class CaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_case_table()

    def create_case_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            analyst TEXT NOT NULL
        )''')
        self.conn.commit()

    def create_case(self, name, analyst):
        self.conn.execute('INSERT INTO cases (name, analyst) VALUES (?, ?)', (name, analyst))
        self.conn.commit()

    def get_cases(self):
        cursor = self.conn.execute('SELECT * FROM cases')
        return cursor.fetchall()
