import sqlite3
import os
from data import tools

def init_db():
    conn = sqlite3.connect('ai_hub.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Create tools table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            link TEXT
        )
    ''')

    # Check if tools are already populated
    cursor.execute('SELECT COUNT(*) FROM tools')
    if cursor.fetchone()[0] == 0:
        # Populate initial tools
        for tool in tools:
            cursor.execute('''
                INSERT INTO tools (name, category, description, link)
                VALUES (?, ?, ?, ?)
            ''', (tool['name'], tool['category'], tool['description'], tool['link']))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database `ai_hub.db` initialized successfully.")
