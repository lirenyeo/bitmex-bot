import logging
from colorama import init, Fore, Style

from global_config import PLACE_TRADES
from utils import *

init(autoreset=True)

class Logger:
    def __init__(self):
        self.tick_count = 1
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_market_order(self, quantity, timestamp):
        if not PLACE_TRADES:
            self.logger.info(blue("!!! Not Placing Trade !!!"))
        self.logger.info(red("**** MARKET ORDER ****"))
        self.logger.info(red(f"Timestamp: {format_ts(timestamp)}"))
        self.logger.info(red(f"Quantity: {quantity}"))
        self.logger.info(red("**********************\n"))

    def log_limit_order(self, quantity, timestamp, price):
        if not PLACE_TRADES:
            self.logger.info(blue("!!! Not Placing Trade !!!"))
        self.logger.info(red("**** LIMIT ORDER  ****"))
        self.logger.info(red(f"Timestamp: {format_ts(timestamp)}"))
        self.logger.info(red(f"Quantity: {quantity}"))
        self.logger.info(red(f"Price: {price}"))
        self.logger.info(red("**********************\n"))

    def log_tick_start(self, last, buy, sell, tick_interval):
        self.logger.info(magenta(f"\nTick #{self.tick_count} (Interval: {tick_interval}s)"))
        self.logger.info(green(f"------- {current_time()} -------"))
        self.logger.info(yellow(f"Last: {last} | Buy: {buy} | Sell: {sell}"))
        self.tick_count += 1

    def log_leverage_info(self, last_lev, current_lev, pos, lpp, lower_lev, upper_lev, target_lev):
        self.logger.info(green("-----------------------------------"))
        self.logger.info(cyan(f"Current Leverage        : {round(current_lev, 4)}"))
        self.logger.info(cyan(f"Last Leverage           : {round(last_lev, 4)}"))
        self.logger.info(cyan(f"Leverage Difference     : {round(current_lev - last_lev, 4)}"))
        self.logger.info(cyan(f"Target Leverage         : {target_lev}"))
        self.logger.info(green("-----------------------------------"))
        self.logger.info(cyan(f"Current Position        : {round(pos, 4)}"))
        self.logger.info(cyan(f"Leverage per Position   : {round(lpp, 4)}"))
        self.logger.info(green("-----------------------------------"))
        self.logger.info(cyan(f"Sell when Leverage is < : {round(lower_lev, 4)}"))
        self.logger.info(cyan(f"Buy when Leverage is  > : {round(upper_lev, 4)}"))
        self.logger.info(green("-----------------------------------\n"))


myLogger = Logger()


"""
Future Reference

# def log_instrument_data(self, socket_data):
    #     self.logger.info("Instrument data: ")
    #     print(Fore.BLUE + f"=========================")
    #     print(Fore.BLUE + "= " + Fore.RED + f"Symbol: {socket_data['symbol']}")
    #     print(Fore.BLUE + "= " + Fore.RED + f"State: {socket_data['state']}")
    #     print(Fore.BLUE + "= " + Fore.RED +
    #           f"High: {socket_data['highPrice']}")
    #     print(Fore.BLUE + "= " + Fore.RED + f"Low: {socket_data['lowPrice']}")
    #     print(Fore.BLUE + f"=========================")
    #     print("  ")
    #     print("  ")

    # def log_wallet_data(self, socket_data):
    #     # breakpoint()
    #     print(Fore.GREEN + f"=========================")
    #     print(Fore.GREEN + "= " + Fore.RED +
    #           f"Currency: {socket_data['currency']}")
    #     print(Fore.GREEN + "= " + Fore.RED +
    #           f"Wallet Balance: {socket_data['walletBalance']}")
    #     print(Fore.GREEN + "= " + Fore.RED +
    #           f"Margin Balance: {socket_data['marginBalance']}")
    #     print(Fore.GREEN + f"=========================")
    #     print(" ")
    #     print(" ")

    # def log_positions(self, socket_data):
    #     print(Fore.GREEN + f"=========================")
    #     # breakpoint()
    #     print(Fore.GREEN + "= " + Fore.RED +
    #           f"Open Orders: {socket_data[0]['currentQty']}")
    #     print(Fore.GREEN + f"=========================")

    # def log_recent_trades(self, socket_data):
    #     print(Fore.RED + f"=========================")
    #     for trade in socket_data:
    #         print(Fore.RED + "==========")
    #         print(Fore.RED + "= " + Fore.WHITE + f"Symbol: {trade['symbol']}")
    #         print(Fore.RED + "= " + Fore.WHITE + f"Side: {trade['side']}")
    #         print(Fore.RED + "= " + Fore.WHITE + f"Size: {trade['size']}")
    #         print(Fore.RED + "= " + Fore.WHITE + f"Price: {trade['price']}")
    #         print(Fore.RED + "==========")
    #     print(Fore.RED + f"=========================")

    # def log_tick(self, socket_data):
    #     print(Fore.RED + f"=========================")
    #     print(Fore.RED + "= " + Fore.GREEN +
    #           f"Last Trade: {socket_data['last']}")
    #     print(Fore.RED + "= " + Fore.GREEN +
    #           f"Buy Price: {socket_data['buy']}")
    #     print(Fore.RED + "= " + Fore.GREEN +
    #           f"Sell Price: {socket_data['sell']}")
    #     print(Fore.RED + f"=========================")
    #     print(" ")
"""

