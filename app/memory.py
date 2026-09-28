import sqlite3
from datetime import datetime

DB_NAME = "agent_logs.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_input TEXT,
            agent_output TEXT,
            tool_used TEXT,
            success INTEGER
        )
    """)
    conn.close()

def save_log(user_input: str, agent_output: str, tool_used: str, success: int):
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        INSERT INTO logs (timestamp, user_input, agent_output, tool_used, success)
        VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.utcnow().isoformat(),
        user_input,
        agent_output,
        tool_used,
        success
    ))
    conn.commit()
    conn.close()

def get_recent_logs(limit: int = 10):
    conn = sqlite3.connect(DB_NAME)
    rows = conn.execute("""
        SELECT timestamp, user_input, agent_output, tool_used, success
        FROM logs
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    data = rows.fetchall()
    conn.close()
    return data

def get_success_rate():
    conn = sqlite3.connect(DB_NAME)
    row = conn.execute("""
        SELECT COUNT(*), SUM(success)
        FROM logs
    """).fetchone()
    conn.close()

    total = row[0] or 0
    success = row[1] or 0
    return {
        "total": total,
        "success_count": success,
        "success_rate": round((success / total) * 100, 2) if total else 0.0,
    }