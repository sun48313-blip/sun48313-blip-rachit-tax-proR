import sqlite3

def get_db():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # default admin user
    cursor.execute("""
    INSERT OR IGNORE INTO users (username, password)
    VALUES ('admin', '1234')
    """)

    conn.commit()
    conn.close()
