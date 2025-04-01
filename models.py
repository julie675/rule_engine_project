import sqlite3
from typing import Optional, Tuple

def get_user_from_db(username: str) -> Optional[Tuple]:
    """
    从数据库查询用户信息
    :param username: 用户名
    :return: 返回包含用户信息的元组(id, username, password)或None
    """
    conn = None
    try:
        conn = sqlite3.connect('rules.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def init_db():
    """初始化数据库表结构"""
    conn = None
    try:
        conn = sqlite3.connect('rules.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization failed: {e}")
    finally:
        if conn:
            conn.close()

# 初始化数据库（首次运行时创建表）
if __name__ == '__main__':
    init_db()
    print("Database initialized successfully")