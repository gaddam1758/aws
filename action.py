
import boto3
def action(dynamodb,region):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name = region)
    

    
    tables = list(dynamodb.tables.all())

    for table in tables:
        table.delete()


