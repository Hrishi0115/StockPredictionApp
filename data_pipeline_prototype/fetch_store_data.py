# this script will handle fetching and storing it in the database using sessions provided by `database.py`

# backend/fetch_store_data.py

from alpaca.data import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from keys import api_key, api_secret
from database import get_session, engine
from create_table import create_stock_data_table
from sqlalchemy import MetaData

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
    metadata = MetaData() # used to collect information about the tables in the database
    metadata.reflect(bind=engine) # reflect is a method of `MetaData` that reads the database schema (tables, columns, constraints, etc.) from the database connected by 
    # engine
    table = metadata.tables[table_name] # contains info about table with table name = table_name

    with get_session() as session:
        try:
            # Convert DataFrame to list of dictionaries for bulk insertion
            data_dicts = data.to_dict(orient='records')
            # Use SQLAlchemy's bulk insert
            session.execute(table.insert(), data_dicts)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")

def fetch_and_store(symbol, timeframe, start, end):
    # Create table if it doesn't exist
    create_stock_data_table(symbol, timeframe)
    
    # Fetch data
    data = get_historical_data([symbol], start, end, timeframe)
    
    if data is not None:
        store_data(data, symbol, timeframe)
    else:
        print(f"No data fetched for {symbol} from {start} to {end}")

