import pandas as pd


def get_data(file):
    data = pd.read_csv(file)
    data2 = data[["Type", "Status"]]
    dic = data2.groupby(["Type"]).value_counts()
    monthly_active = dic["MONTHLY"]["active"]
    weekly_active = dic["WEEKLY"]["active"]
    yearly_active = dic["YEARLY"]["active"]
    return weekly_active, monthly_active, yearly_active
