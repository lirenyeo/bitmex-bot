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
   ```

  By set `BITMEX_IS_TESTNET` to `"yes"` or "`no"`, the websocket will connect to the respective testnet/live URL.