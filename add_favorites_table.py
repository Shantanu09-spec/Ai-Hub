import sqlite3

def add_favorites_table():
    conn = sqlite3.connect('ai_hub.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            tool_id INTEGER NOT NULL,
            UNIQUE(user_id, tool_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Favorites table added successfully.")

if __name__ == "__main__":
    add_favorites_table()
