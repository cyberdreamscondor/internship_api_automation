from base.base_api import BaseApi
import json

get_posts_endpoint = "/public/v2/posts"
get_post_by_id = "/public/v2/posts/"


class Posts(BaseApi):
    def get_posts(self, url, expected_status_code):
        response = self.get_request(url + get_posts_endpoint)
        self.check_status_code(response, expected_status_code)

    def get_post_by_id(self, url, expected_status_code, post_id):
        response = self.get_request(url+get_post_by_id + post_id)
        self.check_status_code(response, expected_status_code)
        response_body = response.json()
        return response_body

    def get_post_id(self, url, expected_status_code, expected_id):
        response = self.get_request(url + get_posts_endpoint)
        self.check_status_code(response, expected_status_code)
        id_list = self.get_json_value_by_key(response, "$.[id]")
        assert expected_id in id_list

    def get_post_user_id(self, url, expected_status_code):
        response = self.get_request(url + get_posts_endpoint)
        self.check_status_code(response, expected_status_code)
        user_id_list = self.get_json_value_by_key(response, "$.[user_id]")
        return user_id_list


    def get_posts_by_page(self, url, expected_status_code, params):
        response = self.get_request(url+get_posts_endpoint, params=params)
        self.check_status_code(response, expected_status_code)
        response_body = response.json()
        return response_body

    def check_posts_data_by_length(self, data, length):
        assert len(data) == length



