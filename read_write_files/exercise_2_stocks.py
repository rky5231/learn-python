import pandas as pd

df = pd.read_csv("stocks.csv")
for data in df["Company Name"]:
    print(data[0])
# print(df)