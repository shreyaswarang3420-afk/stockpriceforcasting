# Stock Forecasting AI

A Streamlit application that downloads stock data with `yfinance`, trains an LSTM model, and displays a future price forecast.

## Run locally

```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown by Streamlit, enter a ticker such as `TMPV.NS` or `AAPL`, and generate a forecast.

## Deploy to Railway

1. Push this project to GitHub.
2. Create a new Railway project and choose **Deploy from GitHub repo**.
3. Select this repository.
4. Railway will use `railway.json` and start the app with Streamlit.
5. Generate a public domain from Railway's **Networking** settings.

The deployment uses Python 3.11 and the CPU-only TensorFlow package to keep the image compatible with Railway.

Forecasting is for educational use only and should not be treated as financial advice.
