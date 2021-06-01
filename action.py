
import boto3
def action(dynamodb,region,table_name):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name = region)
    

    table = dynamodb.Table(table_name)
    table.delete()

