import json
import os

import boto3


def handler(event, context):
    print(event)
    print(context)

    client = boto3.client('sns')

    response = client.publish(
        TopicArn=os.environ['SNS_TOPIC_ARN'],
        Message='Milo at the door',
    )

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        raise RuntimeError

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS'
        },
        'body': json.dumps('ACK')
    }
