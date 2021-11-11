import boto3
from boto3.dynamodb.conditions import Key
from flask import Flask
app = Flask(__name__)
app.config.from_object('setting.Config')

def query_address(channel_name, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
                              aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'], region_name=app.config['REGION_NAME'])

    table = dynamodb.Table(app.config['DYNAMODB_TABLE'])
    response = table.query(
        KeyConditionExpression=Key(app.config['DYNAMODB_TABLE_KEY']).eq(channel_name)
    )
    return response['Items'][0]['recording_s3_key_prefix']


if __name__ == '__main__':
    channel_name = app.config['CHANNEL_NAME']
    cdn_prefix = app.config['CDN_PREFIX']
    media_suffix = app.config['MEDIA_SUFFIX']
    print(f"address from {channel_name}")
    address = query_address(channel_name)
    address = cdn_prefix + address + media_suffix
    print(address)
