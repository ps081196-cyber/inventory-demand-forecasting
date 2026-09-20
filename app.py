import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from core import forecast_demand,generate_demand,inventory_policy

st.set_page_config(page_title="Demand Forecasting",page_icon="📦",layout="wide")
st.title("📦 Inventory Demand Forecasting")
upload=st.file_uploader("Upload date/demand CSV",type="csv")
data=pd.read_csv(upload) if upload else generate_demand()
horizon=st.sidebar.slider("Forecast horizon (days)",7,90,30)
lead=st.sidebar.slider("Supplier lead time (days)",1,30,7)
future=forecast_demand(data,horizon)
safety,reorder=inventory_policy(data,lead)
a,b,c=st.columns(3)
a.metric("Average daily demand",f"{data.demand.mean():.1f}")
b.metric("Safety stock",f"{safety:,}")
c.metric("Reorder point",f"{reorder:,}")
fig=go.Figure()
fig.add_scatter(x=pd.to_datetime(data.date).tail(120),y=data.demand.tail(120),name="Actual")
fig.add_scatter(x=future.date,y=future.forecast_demand,name="Forecast")
st.plotly_chart(fig,use_container_width=True)
st.dataframe(future,use_container_width=True)
st.download_button("Download forecast",future.to_csv(index=False),"demand_forecast.csv")
