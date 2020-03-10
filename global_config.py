import os
from dotenv import load_dotenv
load_dotenv()

PLACE_TRADES = True
IS_TESTNET = os.getenv("BITMEX_IS_TESTNET") == 'yes'
# LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")

if IS_TESTNET:
    BITMEX_WS_ENDPOINT = "wss://testnet.bitmex.com/realtime"
else:
    BITMEX_WS_ENDPOINT = "wss://www.bitmex.com/realtime"

BITMEX_API_KEY = os.getenv("BITMEX_API_KEY")
BITMEX_API_SECRET = os.getenv("BITMEX_API_SECRET")
