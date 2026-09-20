from core import forecast_demand,generate_demand,inventory_policy

def test_forecast_and_policy():
    data=generate_demand(180,2)
    future=forecast_demand(data,14)
    safety,reorder=inventory_policy(data,7)
    assert len(future)==14
    assert (future.forecast_demand>=0).all()
    assert reorder>safety>0
