import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DB_NAME = "app.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gst_returns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gstin TEXT,
        period TEXT,
        amount REAL
    )
    """)

    # -------- INSERT FIRST ADMIN --------
    cursor.execute("SELECT * FROM users WHERE username='admin'")
    admin = cursor.fetchone()

    if not admin:
        hashed = hash_password("admin123")
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", hashed)
        )

    conn.commit()
    conn.close()
