import pandas as pd
import boto3
import botocore
from pyspark.sql import SparkSession

s3 = boto3.resource('s3',
                    aws_access_key_id='AKIA42PHH6MGDWGRIMAO',
                    aws_secret_access_key='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'
                    )

def download_file(bucket_name, object_name, download_path):
    try:
        s3.Bucket(bucket_name).download_file(object_name, download_path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_file('dataengineeringprojectbucket2796', 'IOT-temp.csv',
                  'IOT-temp.csv')