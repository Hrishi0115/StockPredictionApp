# backend/fetch_data.py

import pandas as pd
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from keys import api_key, api_secret
from database import get_session
from models import StockData

# Initialize the Alpaca API client
client = StockHistoricalDataClient(api_key, api_secret)

def get_historical_data(symbol_or_symbols, start, end, timeframe):
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol_or_symbols,
        timeframe=timeframe,
        start=start,
        end=end
    )
    
    bars = client.get_stock_bars(request_params)
    return bars.df.reset_index()

def store_data(data, symbol, timeframe):
    table_name = f"{symbol}_{timeframe}_stock_data"
    with get_session() as session:
        try:
            for index, row in data.iterrows():
                stock_entry = StockData(
                    symbol=row['symbol'],
                    date=row['timestamp'],
                    open=row['open'],
                    high=row['high'],
                    low=row['low'],
                    close=row['close'],
                    volume=row['volume']
                )
                session.add(stock_entry)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")

# if __name__ == '__main__':
#     symbol = 'AMZN'
#     timeframe = 'minute'
#     start = '2023-01-01'
#     end = '2023-01-02'

#     # Fetch data
#     data = get_historical_data([symbol], start, end, TimeFrame.Minute)
    
#     if data is not None:
#         store_data(data, symbol, timeframe)
#     else:
#         print(f"No data fetched for {symbol} from {start} to {end}")
