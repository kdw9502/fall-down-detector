import smtplib
from email.mime.text import MIMEText

import linebot
import telegram
from linebot.models import TextSendMessage

message = "%s 위치에 넘어진 사람이 있습니다."


def send_alert_by_info(info):
    device = info['device']
    if info.get('mail') is not None:
        send_email(info['mail'], device)
    if info.get('line_bot') is not None:
        send_line_bot(info['line_bot'], device)
    if info.get('telegram_bot') is not None:
        send_telegram_bot(info['telegram_bot'], device)
    if info.get("phone") is not None:
        send_sms(info['phone'], device)


# 메일주소, 위치(기기명)
def send_email(address, device):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # say Hello
    smtp.starttls()  # TLS 사용시 필요

    sender_id = ""
    password = ""

    smtp.login(sender_id, password)

    msg = MIMEText("contents", "html", _charset="utf-8")

    msg['Subject'] = message % device
    msg['From'] = sender_id
    msg['To'] = address
    smtp.sendmail(sender_id, address, msg.as_string())

    smtp.quit()


def send_line_bot(user_id, device):
    line_bot_api = linebot.LineBotApi('Access_token')
    line_bot_api.push_message(user_id, TextSendMessage(text=message % device))


def send_telegram_bot(chat_id, device):
    token = ''
    bot = telegram.Bot(token=token)

    bot.send_message(chat_id=chat_id, text=message % device)


def send_sms(phone_number, device):
    pass
