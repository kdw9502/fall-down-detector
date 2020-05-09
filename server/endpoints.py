from alert import send_alert_by_info
from database_access import find_user_info, set_user_info


def register_user_info(event, context):
    user_id = event.get("user_id")
    set_user_info(user_id, event)


def send_alert(event, context):
    # user_id로 비상연락망을 조회하고, 넘어짐이 발생한 위치와 함께 알림 발송
    user_id = event.get("user_id")
    user_info = find_user_info(user_id)
    send_alert_by_info(user_info)
