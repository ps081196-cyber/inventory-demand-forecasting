# Inventory Demand Forecasting

An interactive forecasting tool for SKU-level demand planning. It creates a future demand forecast, estimates safety stock and recommends a reorder point.

## Business value
- Reduces stock-out risk
- Avoids excess inventory
- Supports weekly replenishment reviews
- Makes forecast error visible through backtesting

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

The demo uses reproducible synthetic daily sales with trend, weekly seasonality and promotions. Users can upload their own CSV containing `date` and `demand`.

## Technology
Python · pandas · statsmodels · Streamlit · Plotly · pytest

Original portfolio project built for supply-chain analytics.
