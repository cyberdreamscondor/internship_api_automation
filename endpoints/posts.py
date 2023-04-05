from base.base_api import BaseApi

get_posts_endpoint = "/public/v2/posts"
get_post_by_id = "/public/v2/posts/"
get_user_post_endpoint = "/public/v2/users/"
posts_endpoint = "/posts"
headers = {'Authorization': 'Bearer c8816a6b5a1ce16041be702d5b0640ed4ba524d18bd27eb35b0f09eed255845f',
           'Content-Type': 'application/json'}


class Posts(BaseApi):
    def get_posts(self, url, expected_status_code):
        response = self.get_request(url + get_posts_endpoint, headers)
        self.check_status_code(response, expected_status_code)

    def get_post_user_id(self, url, expected_status_code):
        response = self.get_request(url + get_posts_endpoint, headers)
        self.check_status_code(response, expected_status_code)
        user_id_list = self.get_json_value_by_key(response, "$.[user_id]")
        return user_id_list

    def get_post_data(self, url, expected_status_code, user_id):
        response = self.get_request(url + get_user_post_endpoint + user_id + posts_endpoint, headers)
        self.check_status_code(response, expected_status_code)
        return response.json()

    def create_post(self, url, json):
        response = self.post_request(url + get_posts_endpoint, json, headers)
        self.check_status_code(response, 201)

    def update_user(self, url, json, post_id):
        response = self.put_request(url + get_post_by_id + post_id, json, headers)
        self.check_status_code(response, 200)

    def delete_user_post(self, url, post_id):
        response = self.delete_request(url + get_post_by_id + post_id, headers)
        self.check_status_code(response, 204)
