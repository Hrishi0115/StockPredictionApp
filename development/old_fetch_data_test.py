# test script to populate Postgre table: stock_data

# backend/fetch_data.py

import pandas as pd
from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from keys import api_key, api_secret
from database import get_db_connection, get_session
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

# def store_data(data):
#     with get_db_connection() as conn: # conn acts as the object returned by get_db_connection() - engine.connect()
#         # establishes a context manager for the database connection - 
#         # when you enter the with block, the __enter__() method of the context manager (in this case, the get_db_connection() function) is executed
#         # inside the block, you then have a valid database connection (conn) that you have use
#         # when you exit the block, the __exit__() method is called, which ensures that the connection is properly closed
#         # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#         # the conn represents a database connection established between this Python application and the PostgreSQL database
#         # conn can be used to send SQL queries to the database

#         for index, row in data.iterrows():
#             conn.execute("""
#                 INSERT INTO stock_data (symbol, date, open, high, low, close, volume)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#             """, (row['symbol'], row['timestamp'], row['open'], row['high'], row['low'], row['close'], row['volume']))

def store_data(data):
    with get_session() as session:
        try:
            for index, row in data.iterrows():
                # Create an ORM object and add it to the session
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

            # Commit the transaction
            session.commit()
        except Exception as e:
            # Handle exceptions (rollback if needed)
            session.rollback()
            print(f"Error: {e}")


# if __name__ == '__main__':
#     symbol_or_symbols = ['AAPL']
#     timeframe = TimeFrame.Minute  # Use TimeFrame.Minute for minute-level data
#     # Fetch data in smaller chunks to handle large volumes
#     start_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='MS')
#     end_dates = pd.date_range(start='2023-01-31', end='2024-01-31', freq='ME')

#     for start, end in zip(start_dates, end_dates):
#         start = start.strftime('%Y-%m-%dT%H:%M:%SZ')
#         end = end.strftime('%Y-%m-%dT%H:%M:%SZ')
#         data = get_historical_data(symbol_or_symbols, start, end, timeframe)
#         if data is not None:
#             store_data(data)
#         else:
#             print(f"No data fetched for {symbol_or_symbols} from {start} to {end}")


if __name__ == '__main__':
    symbol_or_symbols=['AMZN']
    timeframe = TimeFrame.Minute
    start = '2023-01-01'
    end = '2023-01-02'
    # fetch data
    data = get_historical_data(symbol_or_symbols, start, end, timeframe)
    if data is not None:
        store_data(data)
    else:
        print(f"No data fetched for {symbol_or_symbols} from {start} to {end}")

