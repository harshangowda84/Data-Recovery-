import sqlite3

DB_PATH = 'cases/cases.db'

class CaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_case_table()

    def create_case_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT NOT NULL,
            case_name TEXT NOT NULL,
            investigator_name TEXT NOT NULL,
            description TEXT
        )''')
        self.conn.commit()

    def save_case(self, case_id, case_name, investigator_name, description):
        self.conn.execute(
            'INSERT INTO cases (case_id, case_name, investigator_name, description) VALUES (?, ?, ?, ?)',
            (case_id, case_name, investigator_name, description)
        )
        self.conn.commit()

    def get_cases(self):
        cursor = self.conn.execute('SELECT * FROM cases')
        return cursor.fetchall()
