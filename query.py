import boto3
from boto3.dynamodb.conditions import Key

def query_address(channel_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', aws_access_key_id='',
                              aws_secret_access_key='', region_name='us-east-1')

    table = dynamodb.Table('')
    response = table.query(
        KeyConditionExpression=Key('').eq(channel_name)
    )
    return response['Items'][0]['recording_s3_key_prefix']


if __name__ == '__main__':
    channel_name = ''
    cdn_prefix = ''
    media_suffix = ''
    print(f"address from {channel_name}")
    address = query_address(channel_name)
    address = cdn_prefix + address + media_suffix
    print(address)
