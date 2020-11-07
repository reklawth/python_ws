# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
df = pd.read_csv('flights.csv.gz')
df

# %%
# Determine mean delay by month
mean_delay_by_month = df.groupby(['month'])['arr_delay'].mean()
mean_delay_by_month

# %%
mean_month_plt = mean_delay_by_month.plot(kind='bar', title="Mean Delay By Month")
mean_month_plt

# %%
# Determine if flight delays correspond to destination
mean_delay_by_month_ord = df[(df.dest == 'ORD')].groupby(['month'])['arr_delay'].mean()
print("Flights to Chicago (ORD)")
print(mean_delay_by_month_ord)

mean_month_plt_ord = mean_delay_by_month_ord.plot(kind='bar', title="Mean Delay By Month (Chicago)")
mean_month_plt_ord

# %%
# Determine if flight delays correspond to destination
mean_delay_by_month_lax = df[(df.dest == 'LAX')].groupby(['month'])['arr_delay'].mean()
print("Flights to Los Angeles (LAX)")
print(mean_delay_by_month_lax)

mean_month_plt_ord = mean_delay_by_month_lax.plot(kind='bar', title="Mean Delay By Month (Los Angeles)")
mean_month_plt_ord

# %%
# Examine if a specific carrier will create different delay impact
df[['carrier', 'arr_delay']].groupby('carrier').mean().plot(kind='bar', figsize =(12,8))
plt.xticks(rotation=0)
plt.xlabel('Carrier')
plt.ylabel('Average Delay in Min')
plt.title('Average Arrival Delay by Carrier in 2008, All airports')

df[['carrier', 'dep_delay']].groupby('carrier').mean().plot(kind='bar', figsize =(12,8))
plt.xticks(rotation=0)
plt.xlabel('Carrier')
plt.ylabel('Average Delay in Min')
plt.title('Average Departure Delay by Carrier in 2008, All airports')

# %%
# Perform Joins with other tables in our dataset
weather = pd.read_csv('weather.csv.gz')
weather

# %%
df_withweather = pd.merge(df, weather, how='left', on=['year', 'month', 'day', 'hour'])
df_withweather

# %%
airports = pd.read_csv('airports.csv.gz')
airports

df_withairport = pd.merge(df_withweather, airports, how='left', left_on='dest', right_on='faa')
df_withairport

# %%
