import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

base = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
confirmed = base + '/time_series_covid19_confirmed_global.csv'
deaths = base + '/time_series_covid19_deaths_global.csv'
recovers = base + '/time_series_covid19_recovered_global.csv'

dfConfirmed = pd.read_csv(confirmed)
dfDeaths = pd.read_csv(deaths)
dfRecovers = pd.read_csv(recovers)

print(dfRecovers)

# A: Use group by of all three DF's

grouped_conf = dfConfirmed.groupby(by='Country/Region').sum()
print(grouped_conf)
sorted_grouped_conf = grouped_conf.sort_values(by='1/24/23', ascending=False)
last_col = dfConfirmed.iloc[-1]
last_day = last_col.index[-1]
plt.figure(figsize=(12, 8))
plt.title('Top 10 countries with highest cases', fontsize=14)
x = sorted_grouped_conf[last_day].index[:10]
y = sorted_grouped_conf[last_day].head(10)
plt.barh(np.flip(x), np.flip(y))
plt.xlabel('Total cases by ' + last_day)
plt.grid()
plt.show()

# B: Same as A but with recovery and death

# Deaths
grouped_deaths = dfDeaths.groupby(by='Country/Region').sum()
print(grouped_deaths)
sorted_grouped_deaths = grouped_deaths.sort_values(by='1/24/23', ascending=False)
last_col = dfDeaths.iloc[-1]
last_day = last_col.index[-1]
plt.figure(figsize=(12, 8))
plt.title('Top 10 countries with highest deaths', fontsize=14)
x = sorted_grouped_deaths[last_day].index[:10]
y = sorted_grouped_deaths[last_day].head(10)
plt.barh(np.flip(x), np.flip(y))
plt.xlabel('Total cases by ' + last_day)
plt.grid()
plt.show()

# Recovery
grouped_recover = dfRecovers.groupby(by='Country/Region').sum()
print(grouped_recover)
sorted_grouped_recover = grouped_recover.sort_values(by='1/24/23', ascending=False)
last_col = dfRecovers.iloc[-1]
last_day = last_col.index[-1]
plt.figure(figsize=(12, 8))
plt.title('Top 10 countries with highest recoveries', fontsize=14)
x = sorted_grouped_recover[last_day].index[:10]
y = sorted_grouped_recover[last_day].head(10)
plt.barh(np.flip(x), np.flip(y))
plt.xlabel('Total cases by ' + last_day)
plt.grid()
plt.show()



