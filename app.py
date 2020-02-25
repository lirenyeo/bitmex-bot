import os
import time
import datetime
from bitmex import bitmex
from bitmex_websocket import BitMEXWebsocket
from dotenv import load_dotenv
from time import sleep
from logger import TradeLogger

"""
Load in the environment variables as soon as the script is run
"""

load_dotenv()


class BitMEXTrader():
    def __init__(self):
        """
        Load environment Variables from .env file
        Initialize the socket of the trader to None until the setup assigns them
        Setup the connection to the BitMEX websocket to retrieve the live data
        """
        load_dotenv()
        self.socket = None
        self.__initialize_socket()
        self.tradeState = 1  # 1 means ready to take a trade
        self.client = bitmex(
            test=True,
            api_key=os.getenv('BITMEX_API_KEY'),
            api_secret=os.getenv('BITMEX_API_SECRET')
        )

    def __initialize_socket(self):
        BM_WEBSOCKET_URL = os.getenv('BITMEX_SOCKET_URL')
        BM_KEY = os.getenv('BITMEX_API_KEY')
        BM_SECRET = os.getenv('BITMEX_API_SECRET')
        self.socket = BitMEXWebsocket(
            endpoint=BM_WEBSOCKET_URL, symbol="XBTUSD", api_key=BM_KEY, api_secret=BM_SECRET)
        TradeLogger.log_instrument_data(self.socket.get_instrument())
        # FUNDS() GIVES MARGIN BALANCE
        TradeLogger.log_wallet_data(self.socket.funds())

    def long(self, price, quantity):
        unix_timestamp = str(round(time.time()))

        self.client.Order.Order_cancelAll().result()
        # Entry Order
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Market', orderQty=int(
            quantity), text='Enter Long', clOrdID='long-' + unix_timestamp + '-entry').result()
        # Sell Order
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Stop', pegPriceType="TrailingStopPeg", pegOffsetValue=-1 * round(
            price * 0.0025 * 2)/2, orderQty=-1 * int(quantity), execInst='LastPrice', text="Close Long", clOrdID='long-' + unix_timestamp + '-exit').result()


    def short(self, price, quantity):
        unix_timestamp = str(round(time.time()))

        self.client.Order.Order_cancelAll().result()
        # Buy Order
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Market', orderQty=int(
            quantity), text='Enter Short', clOrdID='short-' + unix_timestamp + '-entry').result()
        # Sell Order
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Stop', pegPriceType="TrailingStopPeg", pegOffsetValue=round(
            price * 0.0025 * 2)/2, orderQty=-1 * int(quantity), execInst='LastPrice', text="Close Short", clOrdID='short-' + unix_timestamp + '-exit').result()

    def run(self):
        while(self.socket.ws.sock.connected):
            ticker = self.socket.get_ticker()
            position =  self.socket.positions()
            TradeLogger.log_tick(ticker)
            TradeLogger.log_positions(position)
            # TradeLogger.log_instrument_data()

            if ticker['buy'] < ticker['last']:
                self.long(ticker['buy'], 10)
            elif ticker['sell'] > ticker['last']:
                self.short(ticker['sell'], 10)
            sleep(3600) # 1 hour


trader_bot = BitMEXTrader()

if __name__ == '__main__':
    trader_bot.run()

print(TradeLogger)
