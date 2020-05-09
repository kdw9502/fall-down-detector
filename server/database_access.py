import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table("table_name")


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
    else:
        print("Update Item succeeded:", response)

