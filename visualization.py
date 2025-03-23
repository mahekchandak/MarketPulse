import matplotlib.pyplot as plt

def plot_trading_signals(stock_data, ticker):
    """Plots stock prices with Buy/Sell signals."""
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data["Adj Close"], label="Stock Price", color="blue")

    plt.scatter(stock_data.index[stock_data["Decision"] == "BUY"], stock_data["Adj Close"][stock_data["Decision"] == "BUY"], 
                color="green", label="Buy Signal", marker="^", s=100)

    plt.scatter(stock_data.index[stock_data["Decision"] == "SELL"], stock_data["Adj Close"][stock_data["Decision"] == "SELL"], 
                color="red", label="Sell Signal", marker="v", s=100)

    plt.title(f"{ticker} Stock Price & Anomaly Trading Signals")
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.legend()
    plt.grid()
    
    plt.show()  
