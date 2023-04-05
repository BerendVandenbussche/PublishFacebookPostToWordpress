import requests


class facebook_helper:
    def __init__(self, user_id, fb_page_id,):
        self.user_id = user_id
        self.fb_page_id = fb_page_id
        self.fb_api_base_url = "https://graph.facebook.com"

    # Todo get correct access tokens from api to make the calls

    def get_facebook_page_access_token(self):
        page_access_token_url = "{0}/{1}/accounts?access_token={2}".format(
            self.fb_api_base_url, self.user_id, self.user_access_token)
        response = requests.get(page_access_token_url)
        return response.json()

    def get_latest_facebook_page_post(self):
        fb_post_url = "{0}/v16.0/{1}/feed?access_token={2}".format(
            self.fb_api_base_url, self.fb_page_id, self.fb_access_token)
        response = requests.get(fb_post_url)
        if not 'data' in response.json():
            raise KeyError('Could not get facebook posts')
        return response.json()['data'][0]
