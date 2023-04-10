from base.base_api import BaseApi


class Users(BaseApi):
    endpoint = "public/v2/users/"

    def get_users(self, url,  expected_status_code, headers=None):
        response = self.get_request(url+self.endpoint, headers=headers)
        self.check_status_code(response, expected_status_code)
        return response

    def get_user(self, url, user_id, expected_status_code, headers=None):
        response = self.get_request(url+self.endpoint+str(user_id), headers=headers)
        self.check_status_code(response, expected_status_code)
        return response

    def create_user(self, url, data, expected_status_code, headers=None):
        response = self.post_request(url+self.endpoint, data, headers=headers)
        self.check_status_code(response, expected_status_code)
        return response

    def update_user(self, url, data, expected_status_code, headers=None):
        response = self.put_request(url+self.endpoint+str(id), data, headers=headers)
        self.check_status_code(response, expected_status_code)
        return response

    def delete_user(self, url, expected_status_code, headers=None):
        response = self.delete_request(url+self.endpoint+str(id), headers=headers)
        self.check_status_code(response, expected_status_code)
        return response




