import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import mlflow 

raw_data_filename = "rul_hrs.csv"
df = pd.read_csv(raw_data_filename, parse_dates=['timestamp'])
df['year'] = df['timestamp'].dt.year
df['month'] = df['timestamp'].dt.month
df['day'] = df['timestamp'].dt.day

#write a pipeline to process numerical data 

df = df.drop(['Unnamed: 0','timestamp'],axis=1)
num_pipeline = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("standardize", StandardScaler()),
])

target = df.pop('rul')
fig = plt.figure(figsize = (20,20))
ax = fig.gca()
df.hist(ax=ax)

from sklearn.pipeline import make_pipeline

num_pipeline = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

prepared_dataset = num_pipeline.fit_transform(df)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(prepared_dataset, target, test_size=0.33, random_state=42)

import seaborn as sns

#plot box whisker plot for each of the features
fig = plt.figure(figsize = (20,20))
ax = fig.gca()
sns.boxplot(data=df, ax=ax)
