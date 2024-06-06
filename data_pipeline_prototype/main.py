# backend/main.py

from fetch_store_data import fetch_and_store
from alpaca.data.timeframe import TimeFrame

if __name__ == '__main__':
    symbol = 'NVDA'
    timeframe = TimeFrame.Minute  # or 'hour', 'day', etc.
    start = '2023-01-01'
    end = '2023-01-31'

    fetch_and_store(symbol, timeframe, start, end)
