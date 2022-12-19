import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import joblib
import ingestion_training.ingest_data_into_s3 as ingest_data_into_s3

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
#fig = plt.figure(figsize = (20,20))
#ax = fig.gca()
#df.hist(ax=ax)

from sklearn.pipeline import make_pipeline

num_pipeline = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())

#fit numerical pipeline
num_pipeline = num_pipeline.fit(df)

joblib.dump(num_pipeline, 'num_pipeline.pkl')


BUCKET_NAME = 'amplify-blogfinal-dev-231714-deployment'

ingest_data_into_s3.upload_file_to_s3('num_pipeline.pkl', BUCKET_NAME, 'num_pipeline.pkl')


