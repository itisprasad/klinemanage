import pandas as pd
import talib

def calculate_macd(data: pd.DataFrame):
    macd, macd_signal, macd_hist = talib.MACD(
        data['close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    data["macd"] = macd
    data["macd_signal"] = macd_signal
    data["macd_hist"] = macd_hist
    return data.dropna()

def calculate_rsi(data: pd.DataFrame):
    data["rsi"] = talib.RSI(data["close"], timeperiod=14)
    return data.dropna()


