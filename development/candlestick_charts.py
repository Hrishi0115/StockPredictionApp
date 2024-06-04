import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import matplotlib.pyplot as plt
import mplfinance as mpf
from datacredentials import database, username, password, host, port


# Setup SQLAlchemy
DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def fetch_data(symbol, start_date, end_date):
    query = """
    SELECT symbol, date, open, high, low, close, volume
    FROM stock_data
    WHERE symbol = :symbol AND date BETWEEN :start_date AND :end_date
    ORDER BY date
    """
    df = pd.read_sql(query, engine, params={"symbol": symbol, "start_date": start_date, "end_date": end_date})
    return df

def resample_data(df, timeframe):
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    if timeframe == 'hour':
        df_resampled = df.resample('H').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })
    elif timeframe == 'day':
        df_resampled = df.resample('D').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })
    return df_resampled

def plot_candlestick(df, symbol, timeframe):
    mpf.plot(df, type='candle', volume=True, title=f'{symbol} - {timeframe.capitalize()} Candlestick Chart')

# Fetch and plot data
symbol = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-12-31'

df = fetch_data(symbol, start_date, end_date)
df_hourly = resample_data(df, 'hour')
df_daily = resample_data(df, 'day')

# Plot hourly candlestick chart
plot_candlestick(df_hourly, symbol, 'hour')
plt.show()

# Plot daily candlestick chart
plot_candlestick(df_daily, symbol, 'day')
plt.show()
