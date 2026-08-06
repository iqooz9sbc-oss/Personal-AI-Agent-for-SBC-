import sqlite3
import os

DB_FOLDER = "database"
DB_FILE = os.path.join(DB_FOLDER, "database.db")

os.makedirs(DB_FOLDER, exist_ok=True)

conn = sqlite3.connect(DB_FILE)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    response TEXT
)
""")

conn.commit()

conn.close()

print("Database created successfully.")
