import time

from global_config import *
from logger import myLogger

class Order:
    def __init__(self, bitmex):
        self.bitmex = bitmex

    def market_order(self, quantity):
        ts = str(round(time.time()))
        if quantity >= 0:
            text = 'Enter Market Long'
            clOrdID = f'market-long-{ts}-entry'
        else:
            text = 'Enter Market Short'
            clOrdID = f'market-short-{ts}-entry'

        myLogger.log_market_order(
            quantity=quantity,
            timestamp=ts
        )

        if PLACE_TRADES:
            self.bitmex.Order.Order_new(
                symbol="XBTUSD",
                ordType="Market",
                orderQty=int(quantity),
                text=text,
                clOrdID=clOrdID
            ).result()


    def limit_order(self, quantity, price):
        ts = str(round(time.time()))
        if quantity >= 0:
            text = f'Enter Market Long at {price}'
            clOrdID = f'limit-long-{ts}-entry-{price}'
        else:
            text = f'Enter Market Short at {price}'
            clOrdID = f'limit-short-{ts}-entry-{price}'

        myLogger.log_limit_order(
            quantity=quantity,
            timestamp=ts,
            price=price
        )

        if PLACE_TRADES:
            self.bitmex.Order.Order_cancelAll().result()
            self.bitmex.Order.Order_new(
                symbol="XBTUSD",
                price=price,
                orderQty=int(quantity),
                text=text,
                clOrdID=clOrdID
            ).result()