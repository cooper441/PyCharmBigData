import pandas as pd
import numpy as np

base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
confirmed = base + '/time_series_covid19_confirmed_global.csv'
deaths = base + '/time_series_covid19_deaths_global.csv'
recovers = base + '/time_series_covid19_recovered_global.csv'

dfConfirmed = pd.read_csv(confirmed)
dfDeaths = pd.read_csv(deaths)
dfRecovers = pd.read_csv(recovers)

# A: Showing first 10 rows of dataframes
# print(dfRecovers.head(10))
# print(dfConfirmed.head(10))
# print(dfDeaths.head(10))

# B: Check for missing values for the dataframe storing deaths and various countries - dfDeaths

print(dfDeaths.isnull().sum())  # Showing how many missing values

dfDeathsMissingValues = dfDeaths.dropna(axis=0, how='any', inplace=False)
print(dfDeaths.shape)  # Previous DF
print(dfDeathsMissingValues.shape)  # After removing missing data

# C: Show summary statistics

print(dfDeaths.describe())


