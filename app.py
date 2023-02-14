import requests
import websocket
import json
import asyncio


def get_current_price():
    key = "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT"
    data = requests.get(key).json()
    print(f"{data['symbol']} price is {data['price']}")

def on_message(self, ws, message):
    print(f"Message: {message}")
    event = json.loads(message)
    if event["e"] == "kline":
        if (float(event["l"])[3] / float(event["h"])[3] * 100) >= 1:
           get_current_price()
        return event

def on_open(ws):
    """Стартовое сообщение запуска сокета."""
    print(f"Open: futures order stream connected")

def on_close(ws):
    """Сообщение закрытия соединения."""
    print(f"Closed: Connection closed")

async def stream_kline(symbol, interval):
    socket = f'wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close)

    ws.run_forever()

asyncio.run(stream_kline('xrpusdt', '1h'))



# wss://stream.binance.com:9443/ws/symbol@kline_interval'
# {
#   "e": "kline",         // Event type
#   "E": 1672515782136,   // Event time
#   "s": "BNBBTC",        // Symbol
#   "k": {
#     "t": 1672515780000, // Kline start time
#     "T": 1672515839999, // Kline close time
#     "s": "BNBBTC",      // Symbol
#     "i": "1m",          // Interval
#     "f": 100,           // First trade ID
#     "L": 200,           // Last trade ID
#     "o": "0.0010",      // Open price
#     "c": "0.0020",      // Close price
#     "h": "0.0025",      // High price
#     "l": "0.0015",      // Low price
#     "v": "1000",        // Base asset volume
#     "n": 100,           // Number of trades
#     "x": false,         // Is this kline closed?
#     "q": "1.0000",      // Quote asset volume
#     "V": "500",         // Taker buy base asset volume
#     "Q": "0.500",       // Taker buy quote asset volume
#     "B": "123456"       // Ignore
#   }
# }