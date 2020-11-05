# %%
import numpy as np
import pandas as pd

# %%
# Make a series, including one field with NaN (Not a Number - empty value)
s = pd.Series([1,3,5,np.nan, 6, 8])
s

# %%
# Accessing a member of the series:
s[4]

# %%
# Define Dataframes
df = pd.DataFrame({'date' : ['2016-01-01', '2016-01-02', '2016-01-03'], 'qty' : [20, 30, 40]})
df

# %%
# Load larger data from file...
rain = pd.read_csv('rainfall.csv')
rain

# %%
# Load a column
rain['City']

# %%
# Load a row
rain.loc[1]

# %%
# Load first 2 rows
rain.loc[0:1]

# %%
# Filter some rows
rain[rain['Rainfall'] < 10]

# %%
# Find all reading for Apr in all Cities?
rain[rain['Month'] == 'Apr']

# %%
# Find all readings for Los Angeles
rain[rain['City'] == 'Los Angeles']

# %%
# Give rows names instead of numbers to use as index
rain.set_index(rain['City'] + rain['Month'])

# %%
# Try to reference by row name
#rain.loc['San FranciscoJan'] # KeyError!
# This does not work because python returned a mutated dataframe not a change to the original

# %%
# overwrite the original dataframe with the mutated dataframe
rain = rain.set_index(rain['City'] + rain['Month'])
rain

# %%
# Try to reference by row name
rain.loc['San FranciscoJan']

# %%
