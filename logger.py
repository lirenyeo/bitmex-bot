import logging
from colorama import init, Fore

init(autoreset=True)


class Logger():
    def __init__(self):
        self.logger = None
        self.__initialize_logger()

    def __initialize_logger(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def log_instrument_data(self, socket_data):
        self.logger.info("Instrument data: ")
        print(Fore.BLUE + f"=========================")
        print(Fore.BLUE + "= " + Fore.RED + f"Symbol: {socket_data['symbol']}")
        print(Fore.BLUE + "= " + Fore.RED + f"State: {socket_data['state']}")
        print(Fore.BLUE + "= " + Fore.RED +
              f"High: {socket_data['highPrice']}")
        print(Fore.BLUE + "= " + Fore.RED + f"Low: {socket_data['lowPrice']}")
        print(Fore.BLUE + f"=========================")
        print("  ")
        print("  ")

    def log_wallet_data(self, socket_data):
        # breakpoint()
        print(Fore.GREEN + f"=========================")
        print(Fore.GREEN + "= " + Fore.RED +
              f"Currency: {socket_data['currency']}")
        print(Fore.GREEN + "= " + Fore.RED +
              f"Wallet Balance: {socket_data['walletBalance']}")
        print(Fore.GREEN + "= " + Fore.RED +
              f"Margin Balance: {socket_data['marginBalance']}")
        print(Fore.GREEN + f"=========================")
        print(" ")
        print(" ")

    def log_positions(self, socket_data):
        print(Fore.GREEN + f"=========================")
        # breakpoint()
        print(Fore.GREEN + "= " + Fore.RED +
              f"Open Orders: {socket_data[0]['currentQty']}")
        print(Fore.GREEN + f"=========================")

    def log_recent_trades(self, socket_data):
        print(Fore.RED + f"=========================")
        for trade in socket_data:
            print(Fore.RED + "==========")
            print(Fore.RED + "= " + Fore.WHITE + f"Symbol: {trade['symbol']}")
            print(Fore.RED + "= " + Fore.WHITE + f"Side: {trade['side']}")
            print(Fore.RED + "= " + Fore.WHITE + f"Size: {trade['size']}")
            print(Fore.RED + "= " + Fore.WHITE + f"Price: {trade['price']}")
            print(Fore.RED + "==========")
        print(Fore.RED + f"=========================")

    def log_tick(self, socket_data):
        print(Fore.RED + f"=========================")
        print(Fore.RED + "= " + Fore.GREEN +
              f"Last Trade: {socket_data['last']}")
        print(Fore.RED + "= " + Fore.GREEN +
              f"Buy Price: {socket_data['buy']}")
        print(Fore.RED + "= " + Fore.GREEN +
              f"Sell Price: {socket_data['sell']}")
        print(Fore.RED + f"=========================")
        print(" ")


TradeLogger = Logger()
