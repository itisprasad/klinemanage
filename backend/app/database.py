import sqlite3
import pandas as pd

DB_FILE = "market_data.db"

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kline_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        interval TEXT NOT NULL,
        time TEXT NOT NULL,
        open REAL NOT NULL,
        high REAL NOT NULL,
        low REAL NOT NULL,
        close REAL NOT NULL,
        volume REAL NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indicators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        interval TEXT NOT NULL,
        time TEXT NOT NULL,
        type TEXT NOT NULL,
        value REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def get_kline_data(symbol, interval):
    conn = sqlite3.connect(DB_FILE)
    query = """
    SELECT time, open, high, low, close, volume 
    FROM kline_data 
    WHERE symbol = ? AND interval = ?
    ORDER BY time
    """
    data = pd.read_sql_query(query, conn, params=(symbol, interval))
    conn.close()
    return data.to_dict(orient="records")

def get_indicator_data(symbol, interval, indicator_type):
    conn = sqlite3.connect(DB_FILE)
    query = """
    SELECT time, value 
    FROM indicators 
    WHERE symbol = ? AND interval = ? AND type = ?
    ORDER BY time
    """
    data = pd.read_sql_query(query, conn, params=(symbol, interval, indicator_type))
    conn.close()
    return data.to_dict(orient="records")

