import smtplib
from email.mime.text import MIMEText
import linebot
import telegram
from linebot.models import TextSendMessage
import decimal
import boto3
import json
from botocore.exceptions import ClientError
from database_access import find_user_info, respond

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table("user_info")


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


message = "[넘어지지마세요]\n  넘어진 사람을 감지했습니다."


def send_alert_by_info(info):
    if info.get('mail') is not None:
        send_email(info['mail'])
    if info.get('line_bot') is not None:
        send_line_bot(info['line_bot'])
    if info.get('telegram_bot') is not None:
        send_telegram_bot(info['telegram_bot'])
    if info.get("phone") is not None:
        send_sms(info['phone'])

    return "SUCCESS"


# 메일주소, 위치(기기명)
def send_email(address):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요

    sender_id = "falldowndetector"
    password = "FallDownDetector"

    smtp.login(sender_id, password)

    msg = MIMEText("contents", "html", _charset="utf-8")

    msg['Subject'] = message
    msg['From'] = sender_id
    msg['To'] = address
    smtp.sendmail(sender_id, address, msg.as_string())

    smtp.quit()


def send_line_bot(user_id):
    line_bot_api = linebot.LineBotApi('Access_token')
    line_bot_api.push_message(user_id, TextSendMessage(text=message))


def send_telegram_bot(chat_id):
    token = ''
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=message)


def send_sms(phone_number):
    client = boto3.client("sns", region_name="us-east-1")
    client.publish(PhoneNumber=phone_number.replace("010", "+8210", 1).replace("-", ""),
                   Message="[넘어지지마세요]\n 넘어진 사람을 감지했습니다.")


def lambda_handler(event, context):
    operation = event['httpMethod']

    if operation == "GET":
        info = event['queryStringParameters']
        try:
            return respond(None, send_alert_by_info(find_user_info(info['user_id'])))
        except Exception as e:
            return respond(e)
    else:
        return respond(Exception("unsupported method"))
