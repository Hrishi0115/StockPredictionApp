from keys import api_key, api_secret

from alpaca.data.live import StockDataStream

wss_client = StockDataStream(api_key, api_secret)

# async handler

async def quote_data_handler(data):
    print(data)

wss_client.subscribe_quotes(quote_data_handler, "AAPL")

wss_client.run()