# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sklearn
from sklearn.cluster import KMeans
from sklearn import linear_model, model_selection, cluster
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit
from sklearn.preprocessing import StandardScaler

# %%
flights = pd.read_csv('flights.csv.gz')
weather = pd.read_csv('weather.csv.gz')
airports = pd.read_csv('airports.csv.gz')

df_withweather = pd.merge(flights, weather, how='left', on=['year', 'month', 'day', 'hour'])
df = pd.merge(df_withweather, airports, how='left', left_on='dest', right_on='faa')

df = df.dropna()

# %%
# Create a Feature Vector
pred = 'dep_delay'
features = ['month', 'day', 'dep_time', 'arr_time', 'carrier', 'dest', 'air_time', 'distance',
            'lat', 'lon', 'alt', 'dewp', 'humid', 'wind_speed', 'wind_gust',
            'precip', 'pressure', 'visib' ]

features_v = df[features]
pred_v = df[pred]

# %%
features_v

# %%
how_late_is_late = 15.0

pd.options.mode.chained_assignment = None # defaulat='warn'

# %%
# carrier is not a number, so transform it into a number
features_v['carrier'] = pd.factorize(features_v['carrier'])[0]

# %%
# dest is not a number, so transform it into a number
features_v['dest'] = pd.factorize(features_v['dest'])[0]

# %%
# Scale the feature vector
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features_v)

features_train, features_test = train_test_split(
    features_scaled,  test_size=0.30, random_state=0)


# %%
# fit the model
cluster = sklearn.cluster.KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)
cluster.fit(features_train)

# %%
# Predict test features
result = cluster.predict(features_test)

# %%
result

# %%
# Perform a plot of the clusters
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# %% 
# Use Principal Component Analysis (PCA) to reduce the dimensions
reduced_data = PCA(n_components=2).fit_transform(features_train)
kmeans = KMeans(init='k-means++', n_clusters=8, n_init=10)
kmeans.fit(reduced_data)

# %%
# Step size of the mesh.  Decrease to increase the quality of the VQ.
h = .02 # point in the mesh [x_min, x_max]x[y_min, y_max].

# %%
# Plot the decision boundary.  For that assign a colour to each.
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# %%
# Obtain labels for each point in mesh.  Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# %%
# Put the result into a color plot, this may take time
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap=plt.cm.Paired,
           aspect='auto', origin='lower')

plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)

# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1],
            marker='x', s=169, linewidths=3,
            color='w', zorder=10)
plt.title('K-means clustering on the dataset (PCA-reduced data)\n'
          'Centroids are marked with white cross')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
# %%
