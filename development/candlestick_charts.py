import sys
import os
import pandas as pd
import plotly.graph_objects as go
from dotenv import load_dotenv

load_dotenv()

module_path = os.getenv('PYTHONPATH')
if module_path and module_path not in sys.path:
    sys.path.append(module_path)

# figure out how to set this permanently - using Environmental variables in settings

from data_pipeline_prototype.database import get_db_connection

def fetch_data(symbol, timeframe, start_date, end_date):
    table_name = f"{symbol}_{timeframe}_stock_data".lower()
    
    query = f"""
    SELECT * FROM {table_name}
    WHERE timestamp BETWEEN '{start_date}' AND '{end_date}'
    ORDER BY timestamp
    """
    
    with get_db_connection() as conn:
        df = pd.read_sql(query, conn)
    
    return df

def generate_candlestick_chart(df, symbol):
    fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                                         open=df['open'],
                                         high=df['high'],
                                         low=df['low'],
                                         close=df['close'])])
    fig.update_layout(
        title=f'Candlestick Chart for {symbol}',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=False
    )
    fig.show()


if __name__ == '__main__':
    symbol = 'MSFT'
    timeframe = '1Min'
    start_date = "2023-01-03 13:00:00"
    end_date = "2023-01-05 14:00:00"

    df = fetch_data(symbol, timeframe, start_date, end_date)
    generate_candlestick_chart(df, symbol)