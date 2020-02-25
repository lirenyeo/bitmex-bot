import os
from dotenv import load_dotenv
load_dotenv()

PLACE_TRADES = True
LIVE_EXCHANGE = False
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")

# Strategy Parameters

# PREDICTION PARAMETERS
TIMEFRAME = '5m'  # the bucketed data frames to retrieve from bitmex, think of this as how many minute candles
# when EMA crosses over SMA, go long. when EMA crosses below SMA, go short
EMA_PERIOD = 20  # this is the shorter duration moving average that reacts more quickly to price changes ()
SMA_PERIOD = 50  # this is the longer duration moving average that reacts more slowly to price changes

# ORDER PARAMETERS
# When testing this trading bot, please use a low leverage multiple to reduce your risk. This number determines the amount of leverage position contracts you would go long or short with.
LEVERAGE_MULTIPLE = 0.5
STOP_LOSS = 0.0025  # keep your losses to a maximum of 0.25% price movement unfavorably. This number determines the price gap on your the trailing stop order. The higher the number, the more you could lose but increases the odds of hitting profitable trades without being stopped out unnecessarily.
SECONDS_BETWEEN_TRADE = 5  # self explainatory

# End Strategy Parameters


if LIVE_EXCHANGE:
    BITMEX_WS_ENDPOINT = "https://www.bitmex.com/api/v1"
else:
    BITMEX_WS_ENDPOINT = "https://testnet.bitmex.com/api/v1"

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")

# PUSHOVER_API_KEY = os.getenv("PUSHOVER_API_KEY")
# PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")
