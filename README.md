# 📈 Stock Forecasting AI

A Streamlit web application that forecasts stock prices using an LSTM neural network. Enter a Yahoo Finance ticker, select the historical data range and forecast settings, then view the predicted closing-price chart and results table.

## 🌐 Live Demo

[Open the deployed Stock Forecasting AI application](https://web-production-8e7d1da2.up.railway.app/)

## ✨ Features

- Search stocks using any valid Yahoo Finance ticker
- Download historical market data automatically
- Scale closing prices with `MinMaxScaler`
- Train a TensorFlow LSTM forecasting model
- Generate customizable 1–60 day forecasts
- Display actual and predicted prices in an interactive Streamlit interface
- Export or review forecasts in a table
- Ready-to-deploy Railway configuration

## 🖥️ Demo Inputs

| Setting | Example |
|---|---|
| Ticker | `AAPL`, `TMPV.NS`, `MSFT`, `TSLA` |
| Start date | `2020-01-01` |
| Forecast days | `30` |
| Training epochs | `2` |

## 🧰 Technology Stack

- **Frontend:** Streamlit
- **Machine learning:** TensorFlow / Keras
- **Data source:** yfinance
- **Data processing:** pandas, NumPy, scikit-learn
- **Visualization:** Matplotlib
- **Deployment:** Railway, Nixpacks

## 📂 Project Structure

```text
.
├── app.py              # Streamlit interface and LSTM forecasting logic
├── requirements.txt    # Python dependencies
├── Procfile            # Streamlit process command
├── railway.json        # Railway deployment configuration
├── runtime.txt         # Python runtime
├── .streamlit/
│   └── config.toml     # Streamlit server settings
└── notebooks/
    └── Copy_of_stockforecastingaibatch (1).ipynb
```

## 🚀 Run Locally

### 1. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Start the application

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## 📊 How to Use

1. Enter a Yahoo Finance ticker in the sidebar.
2. Select a historical start date.
3. Choose the number of forecast days.
4. Choose the number of training epochs.
5. Click **Generate forecast**.
6. Review the forecast chart and predicted closing-price table.

A ticker that includes an exchange suffix is generally required for international shares. For example:

- India: `TMPV.NS`, `TCS.NS`, `RELIANCE.NS`
- United States: `AAPL`, `MSFT`, `TSLA`

## Railway Deployment

### 1. Push the project to GitHub

```bash
git add .
git commit -m "Deploy stock forecasting app"
git push origin main
```

### 2. Deploy on Railway

1. Open [Railway](https://railway.com/) and create a project.
2. Select **Deploy from GitHub repo**.
3. Choose this repository.
4. Railway will read `railway.json` and install dependencies from `requirements.txt`.
5. Open **Settings → Networking** and generate a public domain.

The deployment command is:

```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=$PORT
```

## ⚙️ Railway Configuration

The app uses:

- Python 3.11
- CPU-only TensorFlow
- Streamlit health check at `/_stcore/health`
- Automatic restart after failed deployments

## ⚠️ Limitations

- Stock forecasts are based on historical closing prices only.
- LSTM predictions can be unstable for short training periods or highly volatile markets.
- Training is performed on the server for each request.
- Weekdays and market holidays are not modeled explicitly.
- Results are for educational and demonstration purposes only.

## ⚖️ Disclaimer

This application does not provide financial advice. Do not use its predictions as the sole basis for investment decisions.

## 📜 License

Add a license of your choice before publishing this project publicly.
