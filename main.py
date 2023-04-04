import json
from requests.auth import HTTPBasicAuth
import requests
from dotenv import load_dotenv
import os

load_dotenv()


def get_facebook_page_access_token(user_id, user_access_token):
    page_access_token_url = "https://graph.facebook.com/{0}/accounts?access_token={1}".format(
        user_id, user_access_token)
    response = requests.get(page_access_token_url)


def get_latest_facebook_page_post(fb_page_id, fb_access_token):
    fb_post_url = "https://graph.facebook.com/v16.0/{0}/feed?access_token={1}".format(
        fb_page_id, fb_access_token)
    response = requests.get(fb_post_url)
    if not 'data' in response.json():
        raise KeyError('Could not get facebook posts')
    return response.json()['data'][0]


def save_latest_post_id_to_file(post_id):
    file = open("latest_post_id.txt", "w+")
    file.write(post_id)
    file.close()


def get_latest_id_from_file():
    file = open("latest_post_id.txt", "r")
    id = file.readlines()[0]
    file.close()
    return id


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
        "Content-Type": "application/json",
        "Authorization": "Basic {0}:{1}".format(wp_app_user, wp_app_pass)
    }
    response = requests.post(wp_post_url, data=payload,
                             headers=headers, auth=auth)

    return response


fb_post = get_latest_facebook_page_post(
    os.getenv('FB_PAGE_ID'), os.getenv('FB_ACCESS_TOKEN'))

last_post_id = get_latest_id_from_file()

if last_post_id is not fb_post['id']:
    message = post_message_to_wordpress(
        os.getenv('WP_BASE_URL'), os.getenv('WP_APP_USER'), os.getenv('WP_APP_PASS'), "Test", fb_post['message'])

    save_latest_post_id_to_file(fb_post['id'])
    print(message.json())
