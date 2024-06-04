# backend/create_table.py

from sqlalchemy import create_engine, inspect, Table, Column, Integer, String, Float, DateTime, MetaData
from database import engine

def create_stock_data_table(symbol, timeframe):
    metadata = MetaData()
    table_name = f"{symbol}_{timeframe}_stock_data"
    
    # Check if table exists
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        table = Table(
            table_name, metadata,
            Column('id', Integer, primary_key=True),
            Column('symbol', String),
            Column('date', DateTime),
            Column('open', Float),
            Column('high', Float),
            Column('low', Float),
            Column('close', Float),
            Column('volume', Integer),
        )
        metadata.create_all(engine)
        print(f"Table {table_name} created.")
    else:
        print(f"Table {table_name} already exists.")

# if __name__ == '__main__':
#     symbol = 'AMZN'
#     timeframe = 'minute'
#     create_stock_data_table(symbol, timeframe)
