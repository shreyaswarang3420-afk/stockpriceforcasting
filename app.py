import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

st.set_page_config(page_title="Stock Forecast AI", page_icon="📈", layout="wide")
st.title("📈 Stock Forecasting AI")

with st.sidebar:
    ticker = st.text_input("Stock ticker", value="TMPV.NS")
    start_date = st.date_input("Start date", value=pd.Timestamp("2020-01-01"))
    forecast_days = st.slider("Forecast days", 1, 60, 30)
    epochs = st.slider("Training epochs", 1, 10, 2)
    run = st.button("Generate forecast", type="primary")


@st.cache_data(ttl=3600)
def download_data(symbol, start):
    data = yf.download(symbol, start=start, auto_adjust=True, progress=False)
    if data is None or data.empty:
        return pd.DataFrame()
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)
    data = data[["Close"]].dropna()
    return data


def make_sequences(values, steps):
    x, y = [], []
    for i in range(len(values) - steps):
        x.append(values[i:i + steps, 0])
        y.append(values[i + steps, 0])
    return np.array(x).reshape(-1, steps, 1), np.array(y)


if run:
    with st.spinner("Downloading market data..."):
        df = download_data(ticker.strip().upper(), start_date.strftime("%Y-%m-%d"))

    if df.empty:
        st.error("No data found. Check the ticker symbol and try again.")
    else:
        st.success(f"Loaded {len(df)} trading days for {ticker}")
        steps = 60
        if len(df) <= steps:
            st.error("Not enough historical data. Choose an earlier start date.")
        else:
            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled = scaler.fit_transform(df[["Close"]])
            x, y = make_sequences(scaled, steps)

            model = Sequential([
                LSTM(50, return_sequences=True, input_shape=(steps, 1)),
                Dropout(0.3),
                LSTM(50),
                Dropout(0.3),
                Dense(1),
            ])
            model.compile(optimizer="adam", loss="mse")

            progress = st.progress(0, text="Training the LSTM model...")
            class TrainingProgress(tf.keras.callbacks.Callback):
                def on_epoch_end(self, epoch, logs=None):
                    progress.progress((epoch + 1) / epochs, text=f"Training epoch {epoch + 1}/{epochs}")

            model.fit(x, y, epochs=epochs, batch_size=8, verbose=0,
                      callbacks=[TrainingProgress()])

            last_window = scaled[-steps:].copy()
            forecasts = []
            for _ in range(forecast_days):
                prediction = model.predict(last_window.reshape(1, steps, 1), verbose=0)
                forecasts.append(prediction[0, 0])
                last_window = np.vstack((last_window[1:], prediction))

            forecast_prices = scaler.inverse_transform(np.array(forecasts).reshape(-1, 1)).flatten()
            forecast_dates = pd.date_range(df.index[-1] + pd.Timedelta(days=1), periods=forecast_days)

            fig, ax = plt.subplots(figsize=(12, 4.5))
            ax.plot(df.index, df["Close"], label="Actual", color="#2563eb")
            ax.plot(forecast_dates, forecast_prices, label="Forecast", color="#f97316")
            ax.set_title(f"{ticker} — Actual vs Forecast")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            ax.grid(alpha=0.2)
            ax.legend()
            fig.tight_layout()
            st.pyplot(fig)

            forecast_df = pd.DataFrame({"Date": forecast_dates, "Predicted Close": forecast_prices})
            forecast_df["Predicted Close"] = forecast_df["Predicted Close"].round(2)
            st.subheader("Forecast results")
            st.dataframe(forecast_df.set_index("Date"), use_container_width=True)
else:
    st.info("Enter a ticker in the sidebar, then click **Generate forecast**.")
