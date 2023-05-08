import json
import boto3
glue=boto3.client('glue');

def lambda_handler(event, context):
    # TODO implement
    response = glue.start_crawler(
    Name='Enter a Glue Crawler Name Here'
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
