import boto3
from action import action


def put_tabel(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',region_name = "us-east-2")

    table = dynamodb.Table('students')
    table.put_item(
        Item={
            'role_no': '2',
            'name': 's2'
        }
    )

if __name__ == '__main__':
    #put_tabel()
    my_session = boto3.session.Session()
    my_region = my_session.region_name
    
    print(my_region)
    
    table_name = 'students'

    dynamodb = boto3.resource('dynamodb')
    action(dynamodb,region=my_region,table_name=table_name)