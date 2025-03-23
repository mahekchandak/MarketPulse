import logging

def assign_trading_signals(stock_data):
    """Assigns Buy/Sell/Hold signals based on past anomaly behavior."""
    logging.info("Assigning trading signals...")
    stock_data["Decision"] = "HOLD"  # Default action

    for i in range(1, len(stock_data)):
        if stock_data["Anomaly"].iloc[i] == -1:  # If anomaly detected
            prev_return = stock_data["Return"].iloc[i - 1]
            if prev_return > 0:
                stock_data.loc[stock_data.index[i], "Decision"] = "BUY"
            elif prev_return < 0:
                stock_data.loc[stock_data.index[i], "Decision"] = "SELL"

    return stock_data
