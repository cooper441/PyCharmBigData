import pandas as pd

# Print First 10 rows and import
df = pd.read_csv("police.csv")
print("Printing first 10 rows of data")
print(df.head(10))

# Show all missing values
print("Showing all missing values")
print(df.isnull())

# Drop column country name, get list of columns first
listOfColoumns = [df.columns.values]
print(listOfColoumns)
df.drop(columns="county_name")

# Drop all rows that have missing data
for i in df.iterrows():
    if i is df.isnull():
        df = df.drop(i)
print("Printing DF with dropped rows")
print(df.head)
