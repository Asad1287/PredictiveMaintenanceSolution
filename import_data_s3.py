import boto3 
# get data from s3
s3 = boto3.resource('s3')
bucket = s3.Bucket('mybucket')
