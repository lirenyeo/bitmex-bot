import math
from bitmex import bitmex
from bitmexlib.bitmex_websocket import BitMEXWebsocket
from dotenv import load_dotenv
from time import sleep

from global_config import *
from short1x.config import *
from order import Order
from logger import myLogger
from utils import get_leverage

class Short1x:
    def __init__(self):
        self.socket = BitMEXWebsocket(
            endpoint=BITMEX_WS_ENDPOINT,
            symbol="XBTUSD",
            api_key=BITMEX_API_KEY,
            api_secret=BITMEX_API_SECRET,
        )

        self.bitmex = bitmex(
            test=IS_TESTNET, api_key=BITMEX_API_KEY, api_secret=BITMEX_API_SECRET
        )

        self.order = Order(self.bitmex)

        self.socket.get_instrument()

    def run(self):
        last_leverage = 0

        while self.socket.ws.sock.connected:
            position = self.socket.positions()
            wallet = self.socket.funds()
            ticker = self.socket.get_ticker()

            current_pos = 0
            if position:
                current_pos = position[0]["currentQty"]

            margin_btc = wallet["marginBalance"]
            last_price = ticker["last"]
            buy_price = ticker["buy"]
            sell_price = ticker["sell"]

            leverage = get_leverage(current_pos, margin_btc, last_price)
            abs_leverage = abs(leverage)
            lev_per_pos = get_leverage(1, margin_btc, last_price)
            lower_lev = TARGET_LEVERAGE - lev_per_pos
            upper_lev = TARGET_LEVERAGE + lev_per_pos

            myLogger.log_tick_start(
                last=last_price,
                buy=buy_price,
                sell=sell_price,
                tick_interval=TICK_INTERVAL
            )
            myLogger.log_leverage_info(
                current_lev=leverage,
                last_lev=last_leverage,
                pos=current_pos,
                lpp=lev_per_pos,
                lower_lev=lower_lev,
                upper_lev=upper_lev,
                target_lev=TARGET_LEVERAGE
            )

            if abs_leverage <= lower_lev:
                qty = round((TARGET_LEVERAGE - abs_leverage) / lev_per_pos)
                self.order.limit_order(-qty, buy_price)
                # self.order.market_order(-qty)
            elif abs_leverage > upper_lev:
                qty = round((abs_leverage - TARGET_LEVERAGE) / lev_per_pos)
                self.order.market_order(qty)

            last_leverage = leverage
            sleep(TICK_INTERVAL)

strat = Short1x()