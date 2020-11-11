# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# %%
flights = pd.read_csv('flights.csv.gz')
weather = pd.read_csv('weather.csv.gz')
airports = pd.read_csv('airports.csv.gz')

df_withweather = pd.merge(flights, weather, how='left', on=['year', 'month', 'day', 'hour'])
df = pd.merge(df_withweather, airports, how='left', left_on='dest', right_on='faa')

df = df.dropna()
# %%
# Examine the data
df

# %%
# Create a Feature Vector
pred = 'dep_delay'
features = ['month', 'day', 'dep_time', 'arr_time', 'carrier', 'dest', 'air_time', 'distance',
            'lat', 'lon', 'alt', 'dewp', 'humid', 'wind_speed', 'wind_gust',
            'precip', 'pressure', 'visib' ]

features_v = df[features]
pred_v = df[pred]

pd.options.mode.chained_assignment = None # default='warn'

# %%
# carrier is not a number, so transform it into a number
features_v['carrier'] = pd.factorize(features_v['carrier'])[0]

# %%
# dest is not a number, so transform it into a number
features_v['dest'] = pd.factorize(features_v['dest'])[0]

# %%
# Look at feature vector
features_v

# %%
# Scale the feature vector
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features_v)

# %%
scaled_features

# %%
# Use Principal Component Analysis (PCA) to reduce dimensions down to two
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(scaled_features).transform(scaled_features)

# %%
X_r

# %%
# Prepare to plot the data
import matplotlib.pyplot as plt

# %%
# Percentage of variance explained for each components, this takes a while to render
print('explained variance ration (first two components): %s'
    % str(pca.explained_variance_ratio_))

plt.figure()
lw = 2

plt.scatter(X_r[:,0], X_r[:,1], alpha=.8, lw=lw)
plt.title('PCA of flights dataset')

# %%
# Additional show commands
# plt.plot
# plt.show
print('finished')