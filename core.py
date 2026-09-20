import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def generate_demand(days=540,seed=42):
    r=np.random.default_rng(seed)
    date=pd.date_range(end=pd.Timestamp.today().normalize(),periods=days)
    trend=np.linspace(40,65,days)
    weekly=10*np.sin(2*np.pi*np.arange(days)/7)
    promo=(r.random(days)<.08)*r.uniform(15,40,days)
    demand=np.maximum(0,trend+weekly+promo+r.normal(0,7,days)).round()
    return pd.DataFrame({"date":date,"demand":demand.astype(int)})

def forecast_demand(df,horizon=30):
    clean=df.copy()
    clean["date"]=pd.to_datetime(clean["date"])
    series=clean.sort_values("date").set_index("date")["demand"].asfreq("D").interpolate()
    model=ExponentialSmoothing(series,trend="add",seasonal="add",seasonal_periods=7,initialization_method="estimated").fit(optimized=True)
    future=model.forecast(horizon).clip(lower=0)
    return pd.DataFrame({"date":future.index,"forecast_demand":future.values.round(1)})

def inventory_policy(df,lead_time_days=7,service_factor=1.65):
    demand=df["demand"].astype(float)
    safety=service_factor*demand.std()*(lead_time_days**.5)
    reorder=demand.mean()*lead_time_days+safety
    return round(safety),round(reorder)
