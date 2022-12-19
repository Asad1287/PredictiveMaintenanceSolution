import mlflow
import mlflow.pyfunc
import mlflow.sklearn
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import roc_auc_score
from mlflow.models.signature import infer_signature
from mlflow.utils.environment import _mlflow_conda_env
import cloudpickle
import time
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

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


 
class SklearnModelWrapper(mlflow.pyfunc.PythonModel):
  def __init__(self, model):
    self.model = model
    
  def predict(self, context, model_input):
    return self.model.predict(model_input)
 

with mlflow.start_run(run_name='untuned_random_forest'):
  n_estimators = 10
  model = RandomForestRegressor(n_estimators=n_estimators, random_state=np.random.RandomState(123))
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  rmse_score = mean_squared_error(y_test, y_pred, squared=False)
  mlflow.log_param('n_estimators', n_estimators)
  mlflow.log_metric('rmse', rmse_score)
  wrappedModel = SklearnModelWrapper(model)
  signature = infer_signature(X_test, wrappedModel.predict(None, X_test))
   
