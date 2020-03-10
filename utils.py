import datetime
import time
from colorama import Fore, Style


# TRANSACTION UTILS

def get_leverage(position, marginBTC, price):
    return position / ((marginBTC / 100000000) * price)

def format_ts(unix_timestamp):
    value = datetime.datetime.fromtimestamp(int(unix_timestamp))
    return(f"{value:%Y-%m-%d %H:%M:%S}")

def current_time():
    return format_ts(round(time.time()))

# LOGGING

def red(text):
    return Fore.RED + text + Style.RESET_ALL

def green(text):
    return Fore.GREEN + text + Style.RESET_ALL

def blue(text):
    return Fore.BLUE + text + Style.RESET_ALL

def yellow(text):
    return Fore.YELLOW + text + Style.RESET_ALL

def cyan(text):
    return Fore.CYAN + text + Style.RESET_ALL

def magenta(text):
    return Fore.MAGENTA + text + Style.RESET_ALL
