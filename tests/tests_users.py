import pytest
import json
from endpoints.users import Users
import utils.jsonmodels.users_json as mock_data
import jsonschema
import requests


class UsersTests(Users):
    schema = mock_data.get_user_json_schema()

    def test_create_user(self, app_config):
        mock_data.delete_mock_data(app_config)
        user_data = mock_data.create_users_data()
        for user in user_data:
            user_json = json.dumps(user)  # replaces single quotes with double ones
            user_json = json.loads(user_json)

            response = self.create_user(app_config.base_url, user_json, 201, app_config.token)
            mock_data.store_response_ids(response)

            assert jsonschema.validate(response.json(), self.schema) is None

    def test_get_user(self, app_config):
        id_list = mock_data.get_mock_user_ids()

        for user_id in id_list:
            response = self.get_user(app_config.base_url, user_id, 200, app_config.token)
            assert jsonschema.validate(response.json(), self.schema) is None

    def test_pagination(self, app_config):
        response = self.get_users(app_config.base_url, 200, app_config.token)
        page1 = self.get_users(app_config.base_url, 200, app_config.token, page=1, limit=5)
        page2 = self.get_users(app_config.base_url, 200, app_config.token, page=2, limit=5)
        response_data = response.json()
        page1_users = page1.json()
        page2_users = page2.json()
        assert len(page1_users) == len(page2_users) and\
            len(response_data) == len(page1_users) + len(page2_users)
        assert page1_users.update(page2_users) == response_data

    def test_update_user(self, app_config):
        id_list = mock_data.get_mock_user_ids()
        user_id = id_list[0]
        user_data = self.get_user(app_config.base_url, user_id, 200, app_config.token).json()
        user_data["email"] = "updated@email.com"
        update_response = self.update_user(app_config.base_url, user_id, user_data, 200, app_config.token)
        assert update_response.json()["email"] == "updated@email.com"


































