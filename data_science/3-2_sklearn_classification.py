# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sklearn
from sklearn import linear_model, model_selection, metrics, svm, ensemble
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score, ShuffleSplit
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# %%
flights = pd.read_csv('flights.csv.gz')
weather = pd.read_csv('weather.csv.gz')
airports = pd.read_csv('airports.csv.gz')

df_withweather = pd.merge(flights, weather, how='left', on=['year', 'month', 'day', 'hour'])
df = pd.merge(df_withweather, airports, how='left', left_on='dest', right_on='faa')

df = df.dropna()

# %%
df

# %%
# Create a Feature Vector
pred = 'dep_delay'
features = ['month', 'day', 'dep_time', 'arr_time', 'carrier', 'dest', 'air_time', 'distance',
            'lat', 'lon', 'alt', 'dewp', 'humid', 'wind_speed', 'wind_gust',
            'precip', 'pressure', 'visib' ]

features_v = df[features]
pred_v = df[pred]

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
scaled_features_v = scaler.fit_transform(features_v)

scaled_features_train, scaled_features_test, pred_train, pred_test = train_test_split(
    scaled_features_v, pred_v, test_size=0.30, random_state=0
)

# %%
# Perform logistic regression for classification
clf_lr = sklearn.linear_model.LogisticRegression(penalty='l2',
                                                class_weight='balanced')

logistic_fit=clf_lr.fit(scaled_features_train,
                        np.where(pred_train >= how_late_is_late,1,0))
                        
predictions = clf_lr.predict(scaled_features_test)

# Summary Report
# %%
# Confusion Matrix
cm_lr = confusion_matrix(np.where(pred_test >= how_late_is_late,1,0), predictions)

print("Confusion matrix")
print(pd.DataFrame(cm_lr))

# %%
# Get accuracy
report_lr = precision_recall_fscore_support(
    list(np.where(pred_test >= how_late_is_late,1,0)),
    list(predictions), average='binary'
)

# %%
# Print Accuracy
print("\nprecision = %0.2f, recall = %02.f, F1 = %0.2f, accuracy = %0.2f"
     % (report_lr[0], report_lr[1], report_lr[2],
     accuracy_score(list(np.where(pred_test >= how_late_is_late,1,0)), list(predictions))))

# %%
