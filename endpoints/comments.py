from base.base_api import BaseApi
import json

get_comments_endpoint = "/public/v2/comments"


class Comments(BaseApi):
    def get_comments(self, url, expected_status_code):
        response = self.get_request(url + get_comments_endpoint)
        self.check_status_code(response, expected_status_code)





