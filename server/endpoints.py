from alert import send_alert_by_info


def register_user(event, context):
    user_id = event.get("user_id")
    email = event.get("email", None)


def register_email(event, context):
    pass


def register_linebot(event, context):
    pass


def send_alert(event, context):
    # user_id로 비상연락망을 조회하고, 넘어짐이 발생한 위치와 함께 알림 발송
    user_id = event.get("user_id")
    user_info = find_user_info(user_id)
    send_alert_by_info(user_info)


def find_user_info(user_id):
    return None
