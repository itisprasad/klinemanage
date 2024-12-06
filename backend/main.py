from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base, KLineData
from app.indicators import calculate_macd, calculate_rsi
import pandas as pd

# Initialize database
Base.metadata.create_all(bind=engine)

# FastAPI application
app = FastAPI()

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/kline")
def get_kline(interval: str = Query("1min"), db: Session = Depends(get_db)):
    data = db.query(KLineData).filter(KLineData.interval == interval).all()
    return [{"timestamp": row.timestamp, "open": row.open, "high": row.high, 
             "low": row.low, "close": row.close, "volume": row.volume} for row in data]

@app.get("/indicator/macd")
def get_macd(interval: str = Query("1min"), db: Session = Depends(get_db)):
    data = db.query(KLineData).filter(KLineData.interval == interval).all()
    df = pd.DataFrame([{
        "timestamp": row.timestamp, "close": row.close
    } for row in data])
    if len(df) < 35:
        return {"error": "Not enough data to calculate MACD"}
    df = calculate_macd(df)
    return df[["timestamp", "macd", "macd_signal", "macd_hist"]].to_dict(orient="records")

@app.get("/indicator/rsi")
def get_rsi(interval: str = Query("1min"), db: Session = Depends(get_db)):
    data = db.query(KLineData).filter(KLineData.interval == interval).all()
    df = pd.DataFrame([{
        "timestamp": row.timestamp, "close": row.close
    } for row in data])
    if len(df) < 14:
        return {"error": "Not enough data to calculate RSI"}
    df = calculate_rsi(df)
    return df[["timestamp", "rsi"]].to_dict(orient="records")

