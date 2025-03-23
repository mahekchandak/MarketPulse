import yfinance as yf
import pandas as pd
import logging

def fetch_live_stock_price(ticker, period="1d", interval="1m"):
    try:
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period=period, interval=interval)

        if stock_data.empty:
            raise ValueError(f"{ticker}: No stock data available. Try again later.")

        latest_price = stock_data["Close"].dropna().iloc[-1]
        latest_row = pd.DataFrame({"Close": [latest_price], "Return": [None]}, index=[stock_data.index[-1]])

        stock_data = pd.concat([stock_data, latest_row])

        return stock_data

    except Exception as e:
        logging.error(f"Error fetching stock data for {ticker}: {e}")
        return None
