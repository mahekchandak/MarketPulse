from sklearn.ensemble import IsolationForest
import pandas as pd
import logging

def detect_anomalies(stock_data):
    """Detects anomalies using Isolation Forest. Supports both historical and single live prices."""
    
    # If stock_data is a single price (scalar), convert it to a DataFrame
    if isinstance(stock_data, (int, float)):  
        stock_data = pd.DataFrame({"Return": [stock_data]})  # Convert scalar to DataFrame

    if "Return" not in stock_data.columns:
        logging.error("Missing 'Return' column in stock data.")
        return stock_data  # Return unchanged data if format is incorrect
    
    logging.info("Training Isolation Forest model...")
    model = IsolationForest(contamination=0.01, random_state=42)
    stock_data["Anomaly"] = model.fit_predict(stock_data[["Return"]])

    return stock_data
