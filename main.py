import json
from requests.auth import HTTPBasicAuth
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def post_message_to_wordpress(wp_base_url, wp_app_user, wp_app_pass, title, body):
    wp_post_url = wp_base_url + "/wp-json/wp/v2/posts"
    payload = json.dumps({
        "status": "publish",
        "title": title,
        "content": body,
    })
    auth = HTTPBasicAuth(wp_app_user, wp_app_pass)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(wp_post_url, data=payload,
                             headers=headers, auth=auth)
    print(response.request.method)

    return response


message = post_message_to_wordpress(
    os.getenv('WP_BASE_URL'), os.getenv('WP_APP_USER'), os.getenv('WP_APP_PASS'), "Test", "Hallo")
print(message)
