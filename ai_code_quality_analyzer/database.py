import sqlite3, json
from werkzeug.security import generate_password_hash, check_password_hash
DB = "users.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        code TEXT NOT NULL,
        complexity TEXT,
        lint TEXT,
        summary TEXT,
        improved TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

def register_user(name, email, password):
    conn = sqlite3.connect(DB); c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)", (name,email,generate_password_hash(password)))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

def validate_user(email, password):
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("SELECT name, password FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    if row and check_password_hash(row[1], password):
        return row[0]
    return None

def save_history(email, code, complexity, lint, summary, improved):
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("INSERT INTO history (email, code, complexity, lint, summary, improved) VALUES (?,?,?,?,?,?)",
              (email, code, json.dumps(complexity, ensure_ascii=False), lint, summary, improved))
    conn.commit()
    conn.close()

def get_user_history(email):
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("SELECT id, email, code, complexity, lint, summary, improved, created_at FROM history WHERE email = ? ORDER BY created_at DESC", (email,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_history_entry(entry_id):
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("SELECT id, email, code, complexity, lint, summary, improved, created_at FROM history WHERE id = ?", (entry_id,))
    row = c.fetchone()
    conn.close()
    return row
