from base.base_api import BaseApi
import json

get_todos_endpoint = "/public/v2/todos"


class Todos(BaseApi):
    def get_todos(self, url, expected_status_code):
        response = self.get_request(url + get_todos_endpoint)
        self.check_status_code(response, expected_status_code)