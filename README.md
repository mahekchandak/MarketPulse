# MarketPulse: AI-Driven Stock Anomaly Detection
MarketPulse is a **real-time stock anomaly detection system** that uses **Yahoo Finance API & Machine Learning (Isolation Forest)** to identify unusual price movements and generate **Buy/Sell/Hold signals**.  

### **Features**  
✅ Fetches **real-time stock prices** from Yahoo Finance  
✅ Detects **anomalous price movements** using ML  
✅ Assigns **trading signals** based on historical trends  
✅ **Automated pipeline** with logging & CSV storage  
✅ **Interactive visualization** of stock trends & anomalies  

### **Tech Stack**  
- **Python** (Pandas, NumPy, Scikit-Learn, Matplotlib)  
- **Yahoo Finance API** (Real-time stock data)  
- **Machine Learning** (Isolation Forest for anomaly detection)  

### **Installation & Usage**  
```bash
git clone https://github.com/your-username/MarketPulse-Anomaly-Detection.git
cd MarketPulse-Anomaly-Detection
pip install -r requirements.txt
python main.py AAPL --period 5d --interval 1d
```
*(Replace `AAPL` with any stock ticker like `NVDA`, `TSLA`.)*  
