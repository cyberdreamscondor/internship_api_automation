from base.base_api import BaseApi
import json

get_posts_endpoint = "/public/v2/posts"


class Posts(BaseApi):
    def get_posts(self, url, expected_status_code):
        response = self.get_request(url + get_posts_endpoint)
        self.check_status_code(response, expected_status_code)