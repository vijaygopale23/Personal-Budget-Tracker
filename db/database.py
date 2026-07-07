import sqlite3
from datetime import datetime

DB_PATH = "db/my_database.db"

def create_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn

def init_db():
    conn = create_connection()
    c = conn.cursor()
    
    # User profile table
    c.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT,
            profile_pic TEXT
        )
    ''')

    # Expenses table
    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            type TEXT,
            date TEXT,
            month TEXT
        )
    ''')

    # Budget limit table
    c.execute('''
        CREATE TABLE IF NOT EXISTS budget_limit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            limit_amount REAL,
            month TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_expense(category, amount, type, date):
    conn = create_connection()
    c = conn.cursor()
    month = datetime.strptime(date, "%Y-%m-%d").strftime("%B-%Y")
    c.execute(
        "INSERT INTO expenses (category, amount, type, date, month) VALUES (?, ?, ?, ?, ?)",
        (category, amount, type, date, month)
    )
    conn.commit()
    conn.close()

def get_expenses(month=None):
    conn = create_connection()
    c = conn.cursor()
    if month:
        c.execute("SELECT * FROM expenses WHERE month = ?", (month,))
    else:
        c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    conn.close()
    return rows

def get_todays_expenses():
    conn = create_connection()
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT * FROM expenses WHERE date = ?", (today,))
    rows = c.fetchall()
    conn.close()
    return rows

def reset_month_data(month):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM expenses WHERE month = ?", (month,))
    conn.commit()
    conn.close()

def set_budget_limit(limit, month):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM budget_limit WHERE month = ?", (month,))
    c.execute("INSERT INTO budget_limit (limit_amount, month) VALUES (?, ?)", (limit, month))
    conn.commit()
    conn.close()

def get_budget_limit(month):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT limit_amount FROM budget_limit WHERE month = ?", (month,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def get_total_spent(month):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM expenses WHERE month = ?", (month,))
    total = c.fetchone()[0]
    conn.close()
    return total or 0

def get_total_spent_today():
    conn = create_connection()
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")
    c.execute("SELECT SUM(amount) FROM expenses WHERE date = ?", (today,))
    total = c.fetchone()[0]
    conn.close()
    return total or 0

def save_user_profile(name, profile_pic_path):
    conn = create_connection()
    c = conn.cursor()
    c.execute("DELETE FROM user")
    c.execute("INSERT INTO user (name, profile_pic) VALUES (?, ?)", (name, profile_pic_path))
    conn.commit()
    conn.close()

def get_user_profile():
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT name, profile_pic FROM user LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result if result else (None, None)
