import logging
import pandas as pd
from datetime import datetime

def save_results(stock_data, ticker):
    """Saves processed stock data with trading signals to a CSV file."""
    filename = f"{ticker}_anomaly_signals_{datetime.today().strftime('%Y-%m-%d')}.csv"
    stock_data.to_csv(filename)
    logging.info(f"Results saved to {filename}")
