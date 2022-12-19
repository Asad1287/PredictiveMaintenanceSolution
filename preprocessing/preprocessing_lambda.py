
#python function to read the data from s3 bucket
import os
import boto3 
import pandas as pd
from dotenv import load_dotenv

# load environment variables
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

BUCKET_NAME = 'amplify-blogfinal-dev-231714-deployment'
file_name = 'rul_hrs.csv'
#load data from s3 into pandas dataframe
def load_data_from_s3(BUCKET_NAME, file_name):
    """
    load data from s3 into pandas dataframe
    """
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    dataframe = pd.read_csv(obj['Body'])
    return dataframe
df = load_data_from_s3(BUCKET_NAME, file_name)

