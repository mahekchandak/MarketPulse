import time
import logging
import argparse
from fetch_data import fetch_live_stock_price
from anomaly_detection import detect_anomalies
from trading_signals import assign_trading_signals

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_realtime_pipeline(ticker, period, interval, duration=180):
    """Runs the real-time stock anomaly detection & trading signal assignment."""
    start_time = time.time()
    while time.time() - start_time < duration:
        logging.info(f"Fetching live data for {ticker} (Period: {period}, Interval: {interval})...")
        live_price = fetch_live_stock_price(ticker, period, interval)  # Pass period & interval
        
        if live_price is not None:
            logging.info(f"Live {ticker} Price: ${live_price}")
            
            # Detect anomalies
            stock_data = detect_anomalies(live_price)  
            stock_data = assign_trading_signals(stock_data)
            
            # Get latest Buy/Sell signal
            latest_decision = stock_data["Decision"].iloc[-1]
            logging.info(f"Latest Decision: {latest_decision}")

        time.sleep(60)  # Wait 1 minute before checking again

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stock Market Anomaly Detector")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol (e.g., NVDA, TSLA, GME)")
    parser.add_argument("--period", type=str, default="5d", help="Data period (e.g., '1d', '5d', '1mo')")
    parser.add_argument("--interval", type=str, default="1d", help="Data interval (e.g., '1m', '5m', '1d')")
    args = parser.parse_args()

    run_realtime_pipeline(args.ticker, args.period, args.interval)  # Now uses user-defined period & interval
