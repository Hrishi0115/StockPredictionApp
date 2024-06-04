# this file will handle the logic for creating a table if it doesn't exist

# backend/create_table.py

from sqlalchemy import inspect, Table, Column, Integer, String, Float, DateTime, MetaData
from database import engine

def create_stock_data_table(symbol, timeframe):
    metadata = MetaData() # creates a `MetaData` instance to hold the schema of the table
    table_name = f"{symbol}_{timeframe}_stock_data"
    
    inspector = inspect(engine) # uses the `inspector` to check if a table with the generated name already exists in the database

    if not inspector.has_table(table_name):
        # if the table does not exist
        table = Table(
            table_name, metadata,
            Column('id', Integer, primary_key=True),
            Column('symbol', String),
            Column('timestamp', DateTime),
            Column('open', Float),
            Column('high', Float),
            Column('low', Float),
            Column('close', Float),
            Column('volume', Integer),            
            Column('trade_count', Integer),
            Column('vwap', Float)
        )
        # define the table schema with the specified columns

        metadata.create_all(engine) # creates the table in the database
        print(f"Table {table_name} created.")
    else:
        print(f"Table {table_name} already exists.")

