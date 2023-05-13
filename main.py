# importing all the libraries required
import yfinance as yf
import pandas_ta as ta
from tickers_nifty500 import tickers

# Enter the ticker symbols (if you want to use any other tickers in case)


for ticker in tickers:
    # Download historical data
    data = yf.download(ticker, period="max", progress=False)

    # Calculate RSI using pandas_ta
    rsi = ta.rsi(data["Close"])

    # Output the most recent RSI value
    # print(ticker,"=", rsi[-1])

    # Strategy application
    if rsi[-1] >= 70:
        print("Over-bought Condition", ticker)

    elif rsi[-1] <= 25:
        print("Over-sold Condition", ticker)

# end of the code