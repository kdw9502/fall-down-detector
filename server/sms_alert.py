import boto3

from database_access import find_user_info, respond


def send_sms(user_id):
    info = find_user_info(user_id)
    phone_number = info["phone"]

    client = boto3.client("sns", region_name="us-east-1")
    client.publish(PhoneNumber=phone_number.replace("010", "+8210", 1).replace("-", ""),
                   Message="[넘어지지마세요]\n 넘어진 사람을 감지했습니다.")

    return "success"


def lambda_handler(event, context):
    operation = event['httpMethod']

    if operation == "GET":
        info = event['queryStringParameters']
        try:
            return respond(None, send_sms(info['user_id']))
        except Exception as e:
            return respond(e)
    else:
        return respond(Exception("unsupported method"))
