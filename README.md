### Getting started

**Install dependencies**

1. This project was developed and tested on Python 3.7.6
1. This project uses TA-LIB, a C library. Install the dependency https://github.com/mrjbq7/ta-lib#dependencies
1. `pip install -r requirements.txt`

**Running the code**

1. Majority of the configurations are set in configurations.py
1. This project uses python-dotenv to manage environment variables, the following env variables are required:
   ```
   BITMEX_IS_TESTNET="yes"
   BITMEX_API_KEY=""
   BITMEX_API_SECRET=""
   STRATEGY_NAME="short1x"
   ```

  By set `BITMEX_IS_TESTNET` to `"yes"` or "`no"`, the websocket will connect to the respective testnet/live URL.

#### Strategies Available:

`short1x`: Negative target leverage. Short to increase leverage.
`long1x`: Positive target leverage. Long to increase leverage.
`ma-cross`: Toggle between short1x and long1x when MA20/50 crosses.