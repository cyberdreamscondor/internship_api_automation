import pytest
import json
from endpoints.users import Users
import utils.jsonmodels.users_json as mock_data
import jsonschema
import xml.etree.ElementTree as ET


class UsersTests(Users):
    schema = mock_data.get_user_json_schema() # get schema of a correct user record returned by server

    def test_create_user(self, app_config):
        """
        This particular public API functions in a way that introduces some unexpected bugs.
        In order to mitigate the pain :)
        ! Each test-run first deletes mock data if any present,
        POST it to the server again.
        ! Third parties are allowed to change and repost our data that sometimes lead to failures.
        """
        mock_data.delete_mock_data(app_config)
        user_data = mock_data.create_users_data() # get mock data from a file
        for user in user_data:
            user_json = json.dumps(user)  # replaces single quotes with double ones
            user_json = json.loads(user_json)  # probably no longer relevant. Recheck, delete if so.

            response = self.create_user(app_config.base_url, user_json, 201, app_config.token)
            mock_data.store_response_ids(response) # writes users' records ids from response to the file

            assert jsonschema.validate(response.json(), self.schema) is None

    def test_get_user(self, app_config):
        """
        Gets all mock users and validates response json schema.
        """
        id_list = mock_data.get_mock_user_ids()

        for user_id in id_list:
            response = self.get_user(app_config.base_url, user_id, 200, app_config.token)
            assert jsonschema.validate(response.json(), self.schema) is None

    def test_pagination(self, app_config):
        """
        Set a limit of 5 records per page. API default is 10.
        Checks 2 pages of user records to contain exactly 5 records
        and that a default page of 10 records' data doesn't differ from
        these 2 pages.
        """
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
        """
        Gets user record ids form the file. For the sake of learning project speed selects 1 record only.
        Updates email, PUTs to the server.
        Checks response to contain updated email.
        """
        id_list = mock_data.get_mock_user_ids()
        user_id = id_list[0]
        user_data = self.get_user(app_config.base_url, user_id, 200, app_config.token).json()
        user_data["email"] = "updated@email.com"
        update_response = self.update_user(app_config.base_url, user_id, user_data, 200, app_config.token)
        assert update_response.json()["email"] == "updated@email.com"

    def test_invalid_create_user(self, app_config):
        """
        POST user with invalid data.
        Simple actual/expected response comparison.
        """
        invalid_data = {
            "email": "test_12wdf@testdsf.com",
            "name": "5",
            "gender": "female",
            "status": "active"
        }

        # There's no such message, let us suppose it has to be
        # actually what is the best way? Mark as failing, raise error?

        expected_response = [{
            "field": "name",
            "message": "can't be a number"
        }]
        response = self.create_user(app_config.base_url, invalid_data, 422, app_config.token)
        assert expected_response == response.json()


    def test_xml_create_user(self, app_config):
        """
        Tests whether xml data is accepted
        """
        headers = {
            **app_config.token,
            "Content-Type": "application/xml"
        }

        user_data = mock_data.create_user_xml_data("Dave", "emailmeplease@fortest.com", "male", "active")
        response = self.post_request('https://gorest.co.in/public/v2/users.xml', user_data, headers=headers)
        root = ET.fromstring(response.content)
        #ET.dump(root) prints just like you wanna see it

        assert response.status_code == 201
        assert response.headers["Content-Type"] == "application/xml"
        assert root.find("data/name").text == "Dave"






































