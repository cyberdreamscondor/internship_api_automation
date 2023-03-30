from base.base_api import BaseApi
import json

get_users_endpoint = "/public/v2/users"


class Users(BaseApi):
    def get_users(self, url, expected_status_code):
        response = self.get_request(url + get_users_endpoint)
        self.check_status_code(response, expected_status_code)

