import decimal

import boto3
import json
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table("user_info")


def find_user_info(user_id):
    # db 조회후 정보 리턴
    try:
        response = table.get_item(Key={'user_id': user_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
        return None
    else:
        item = response['Item']
        print("GetItem succeeded:", item)

    return item


def create_user_info(user_info):
    return table.put_item(Item=user_info)


def set_user_info(user_id, infos):
    print(infos)

    infos.pop('user_id', None)

    update_expression = "set " + ", ".join([f"{key} = :{key}" for key in infos.keys()])

    try:
        response = table.update_item(
            Key={'user_id': user_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=infos,
            ReturnValues="UPDATED_NEW"
        )
    except ClientError as e:
        try:
            infos['user_id'] = user_id
            response = create_user_info(infos)
        except ClientError as e:
            print("fail to update or create :", e)
        else:
            print("Insert Item succeeded:", response)
            return response
    else:
        print("Update Item succeeded:", response)
        return response


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': str(err) if err else json.dumps(res, cls=DecimalEncoder),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    operation = event['httpMethod']

    if operation == "GET":
        info = event['queryStringParameters']
        try:
            return respond(None, find_user_info(info['user_id']))
        except Exception as e:
            return respond(e)
    elif operation == "POST":
        info = json.loads(event['body'])
        print(info)
        try:
            return respond(set_user_info(info['user_id'], info))
        except Exception as e:
            return respond(e)


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)
