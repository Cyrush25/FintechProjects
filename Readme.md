# RSI Trading Strategy
This is a Python script that uses the Relative Strength Index (RSI) to identify overbought and oversold conditions in a list of tickers and outputs the tickers that meet the criteria.

## Installation and Setup
To run this script, you will need to install the following Python libraries:

yfinance
pandas_ta
You can install them using pip by running:

pip install yfinance pandas_ta
After installing the libraries, download or clone the script to your local machine.

## Usage
To use this script, simply run it using a Python interpreter. The tickers to be analyzed are imported from tickers_nifty500.py file.

The script will output the tickers that meet the overbought or oversold conditions.

## Strategy
The strategy implemented in this script is based on the RSI. If the RSI is above 70, the ticker is considered to be in an overbought condition and if it is below 25, the ticker is considered to be in an oversold condition.

## Disclaimer
This script is for educational and informational purposes only. It should not be used as a basis for making investment decisions. Please consult with a licensed investment professional before making any investment decisions.
