import json


def create_users_data():
    with open('../utils/jsonmodels/users_data.json', 'r') as file:
        users_data = json.load(file)
        return users_data