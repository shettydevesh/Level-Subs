import pandas as pd


def get_data(file):
    if file.endswith(".xlsx"):
        data = pd.read_excel(file)
    elif file.endswith(".csv"):
        data = pd.read_csv(file)
    data2 = data[["Type", "Status"]]
    dic = data2.groupby(["Type"]).value_counts()
    monthly_active = dic["MONTHLY"]["active"]
    weekly_active = dic["WEEKLY"]["active"]
    yearly_active = dic["YEARLY"]["active"]
    return weekly_active, monthly_active, yearly_active
