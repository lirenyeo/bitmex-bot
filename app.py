import os
import time
import datetime
import math
from bitmex import bitmex
from bitmex_websocket import BitMEXWebsocket
from dotenv import load_dotenv
from time import sleep
from logger import TradeLogger

"""
Load in the environment variables as soon as the script is run
"""

load_dotenv()

def calculate_leverage(position, marginBTC, price):
    return position / ((marginBTC / 100000000) * price)


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
            test=os.getenv('BITMEX_IS_TEST') == 'yes',
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

    def market_buy(self, quantity):
        print("==== BUY ======")
        print('MARKET BUY -- Qty: ', quantity)
        print("===============")
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Market', orderQty=int(quantity), text='Enter Market Long').result()

    def market_sell(self, quantity):
        print("==== SELL ======")
        print('MARKET SELL -- Qty: ', quantity)
        print("================")
        self.client.Order.Order_new(symbol='XBTUSD', ordType='Market', orderQty=(-int(quantity)), text='Enter Market Short').result()

    '''
    MB: 0.0011 / Price: 8742
    Position	Leverage
        1	         0.1039911815
        2	         0.2079823631
        3	         0.3119735446
        4	         0.4159647262
        5	         0.5199559077
        6	         0.6239470893
        7	         0.7279382708
        8	         0.8319294524
        9	         0.9359206339
        10         1.039911815

    price - => leverage + => buy/long
    price + => leverage - => sell/short
    '''
    def run(self):
        last_leverage = 0
        while(self.socket.ws.sock.connected):
            # instruments = self.socket.get_instrument()
            position = self.socket.positions()
            wallet = self.socket.funds()
            ticker = self.socket.get_ticker()

            # TradeLogger.log_positions(position)
            # TradeLogger.log_tick(ticker)
            # TradeLogger.log_instrument_data(instruments)

            current_pos = 0
            if position:
                current_pos = position[0]['currentQty']

            margin_btc = wallet['marginBalance']
            last_price = ticker['last']

            leverage = calculate_leverage(current_pos, margin_btc, last_price)
            abs_leverage = abs(leverage)
            lev_per_pos = calculate_leverage(1, margin_btc, last_price)
            lower_lev = 0.9 - lev_per_pos
            upper_lev = 0.9 + lev_per_pos

            TradeLogger.log_wallet_data(wallet)
            print('last leverage           : ', last_leverage)
            print('current leverage        : ', leverage)
            print('difference              : ', leverage - last_leverage)
            print('current position        : ', current_pos)
            print('Leverage per Position   : ', lev_per_pos)
            print('Sell when Leverage is < : ', lower_lev)
            print('Buy when Leverage is  > : ', upper_lev)


            if abs_leverage <= lower_lev:
                qty = round((0.7 - abs_leverage) / lev_per_pos)
                self.market_sell(qty)
            elif abs_leverage > upper_lev:
                qty = round((abs_leverage - 0.7) / lev_per_pos)
                self.market_buy(qty)


            last_leverage = leverage
            sleep(60) # 1 minute wait


trader_bot = BitMEXTrader()

if __name__ == '__main__':
    trader_bot.run()

print(TradeLogger)
