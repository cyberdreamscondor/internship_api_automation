import pytest
import json
from endpoints.users import Users
import utils.jsonmodels.users_json as mock_data
from jsonmodel.validators import jsonModel
import requests


class UsersTests(Users):
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "gender": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["name", "email", "gender", "status"]
    }

    def test_create_user(self, app_config):
        user_data = mock_data.create_users_data()
        # mock data being deleted before POSTed again
        with open('..utils/jsonmodels/mock_users_ids.json', 'r') as file:
            user_ids = json.load(file)["user_ids"]


        url = "https://gorest.co.in/public/v2/users"
        for user_id in user_ids:
            response = requests.delete(f"{url}/{user_id}")

        for user in user_data:
            user_json = json.dumps(user)
            response = self.create_user(app_config.base_url, user_json, 201, app_config.token)
            # creating an id list for POSTed users
            response_data = json.loads(response.text)
            extracted_id = response_data["id"]

            with open('..utils/jsonmodels/mock_users_ids.json', 'w') as file:
                json.dump({"user_ids": [extracted_id]}, file)

            assert jsonModel(response, schema=self.schema)









