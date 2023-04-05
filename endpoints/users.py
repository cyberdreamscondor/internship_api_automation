from base.base_api import BaseApi


class Users(BaseApi):
    endpoint = "/public/v2/users/"

    def get_users(self, url, expected_status_code):
        response = self.get_request(url+self.endpoint)
        self.check_status_code(response, expected_status_code)

    def get_user(self, url, user_id, expected_status_code):
        response = self.get_request(url+self.endpoint+str(user_id), expected_status_code)
        self.check_status_code(response, expected_status_code)

    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass






