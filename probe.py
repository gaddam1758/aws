import boto3
from botocore.exceptions import ClientError


def probe(dynamodb,primary_region,secondary_region,table_name):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name = primary_region)

    table = dynamodb.Table('students')
    client = boto3.client('dynamodb',region_name = primary_region)

    try:
        response = client.describe_table(TableName=table_name)

    except ClientError as ce:

        if ce.response['Error']['Code'] == 'ResourceNotFoundException':
            print ("Table " + table_name + " does not exist. Create the table first and try again.")
            print("connecting to secondary region")

            dynamodb = boto3.resource('dynamodb',region_name = secondary_region)
            
            table = dynamodb.Table('students')
            table.put_item(
                Item={
                'role_no': '3',
                'name': 's3'
                }
            )
            print("transaction continues")

        else:
            print("unknown error")