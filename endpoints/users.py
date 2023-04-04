from base.base_api import BaseApi
import json

get_users_endpoint = "/public/v2/users"
get_user_endpoint = "/public/v2/users/"
create_user_endpoint = "/public/v2/users"
update_user_endpoint = "/public/v2/users"
delete_user_endpoint = "/public/v2/users/"


class Users(BaseApi):
    def get_users(self, url, expected_status_code, user_id):
        response = self.get_request(url + get_users_endpoint)
        self.check_status_code(response, expected_status_code)

    def get_user_by_id(self, url, expected_status_code, id):
        response = self.get_request(url + get_user_endpoint + id)
        print(response.text)


    def get_user(self, url, expected_status_code, expected_category):
        response = self.get_request(url + get_users_endpoint)
        self.check_status_code(response, expected_status_code)
        list = self.get_json_value_by_key(response, "$.[id]")
        actual_value = self.get_value_from_list(list, expected_category)
        assert actual_value == expected_category, f"Actual Value {actual_value} not much Expected {expected_category}"

