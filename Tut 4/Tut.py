import pandas as pd

df = pd.read_csv("Automobile_price_data_Raw.csv")


print(df.describe())
print(df.dtypes)

df.astype(dtype={prices: float64})




df.replace(to_replace="?", value=None, inplace=True)

# print(df.head())

