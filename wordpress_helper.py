import json
from requests.auth import HTTPBasicAuth
import requests


class wordpress_helper:
    def __init__(self, wp_base_url, wp_app_user, wp_app_pass):
        self.wp_base_url = wp_base_url
        self.wp_app_user = wp_app_user
        self.wp_app_pass = wp_app_pass

    def post_message_to_wordpress(self, title, body):
        wp_post_url = self.wp_base_url + "/wp-json/wp/v2/posts"
        payload = json.dumps({
            "status": "publish",
            "title": title,
            "content": body,
        })
        auth = HTTPBasicAuth(self.wp_app_user, self.wp_app_pass)
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Basic {0}:{1}".format(self.wp_app_user, self.wp_app_pass)
        }
        response = requests.post(wp_post_url, data=payload,
                                 headers=headers, auth=auth)

        return response
