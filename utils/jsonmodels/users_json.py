import json
import requests


def create_users_data():
    with open('../utils/jsonmodels/users_data.json', 'r') as file:
        users_data = json.load(file)
        return users_data


def delete_mock_data(app_config):
    url = "https://gorest.co.in/public/v2/users"
    with open('../utils/jsonmodels/mock_users_ids.json', 'r') as file:
        file_contents = file.read()
        if file_contents:
            json_data = json.loads(file_contents)
            user_ids = json_data["user_ids"]
            for user_id in user_ids:
                response = requests.delete(f"{url}/{user_id}", headers=app_config.token)
    with open('../utils/jsonmodels/mock_users_ids.json', 'w') as file:
        file.truncate(0)


def store_response_ids(response):
    with open('../utils/jsonmodels/mock_users_ids.json', 'r+') as file:
        file_contents = file.read()
        data = {"user_ids": []}
        if file_contents:
            data = json.loads(file_contents)
        data["user_ids"].append(response.json()["id"])
        file.seek(0)
        # json.dump(data, file) same as following line
        file.write(json.dumps(data))
        file.truncate()


def get_mock_user_ids():
    with open('../utils/jsonmodels/mock_users_ids.json', 'r+') as file:
        file_contents = file.read()
        data = {"user_ids": []} # just in case file is empty
        data = json.loads(file_contents)
    return data["user_ids"]


def get_user_json_schema():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "email": {"type": "string"},
            "gender": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["id", "name", "email", "gender", "status"]
    }
    return schema



