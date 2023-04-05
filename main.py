import facebook_helper
import wordpress_helper
from dotenv import load_dotenv
import os

load_dotenv()

facebook = facebook_helper(os.getenv('FB_USER_ID'), os.getenv(
    'FB_PAGE_ID'))
wordpress = wordpress_helper(os.getenv('WP_BASE_URL'), os.getenv(
    'WP_APP_USER'), os.getenv('WP_APP_PASS'))


def save_latest_post_id_to_file(post_id):
    file = open("latest_post_id.txt", "w+")
    file.write(post_id)
    file.close()


def get_latest_id_from_file():
    file = open("latest_post_id.txt", "r")
    id = file.readlines()[0]
    file.close()
    return id


fb_post = facebook.get_latest_facebook_page_post()

last_post_id = get_latest_id_from_file()

if last_post_id is not fb_post['id']:
    message = wordpress.post_message_to_wordpress("Test", fb_post['message'])

    save_latest_post_id_to_file(fb_post['id'])
    print(message.json())
