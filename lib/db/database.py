import sqlite3

DB_FILE = "courseflow.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute()
    