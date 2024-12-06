from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel
from .database import get_kline_data, get_indicator_data, setup_database

app = FastAPI()

@app.on_event("startup")
async def startup():
    setup_database()

class KlineResponse(BaseModel):
    time: str
    open: float
    high: float
    low: float
    close: float
    volume: float

class IndicatorResponse(BaseModel):
    time: str
    value: float

@app.get("/kline", response_model=List[KlineResponse])
async def get_kline(
    symbol: str,
    interval: str = Query("1min", regex="^(1min|5min|60min)$")
):
    return get_kline_data(symbol, interval)

@app.get("/indicator", response_model=List[IndicatorResponse])
async def get_indicator(
    symbol: str,
    interval: str = Query("1min", regex="^(1min|5min|60min)$"),
    type: str = Query("MACD", regex="^(MACD|RSI)$")
):
    return get_indicator_data(symbol, interval, type)

