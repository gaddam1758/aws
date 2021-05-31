import boto3

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
    put_tabel()