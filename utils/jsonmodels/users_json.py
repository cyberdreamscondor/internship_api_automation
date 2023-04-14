import json
import requests
import xml.etree.ElementTree as ET
# Helper functions to fetch mock data to test functions, delete, store response records' ids &
# retrieve it, provide json schema of a correct response.


def create_users_data():
    """
    Returns users mock data loaded from a file
    """
    with open('../utils/jsonmodels/users_data.json', 'r') as file:
        users_data = json.load(file)
        return users_data

def create_user_xml_data(name, email, gender, status):
    root = ET.Element("user")
    name_elem = ET.SubElement(root, "name")
    name_elem.text = name
    email_elem = ET.SubElement(root, "email")
    email_elem.text = email
    gender_elem = ET.SubElement(root, "gender")
    gender_elem.text = gender
    status_elem = ET.SubElement(root, "status")
    status_elem.text = status
    request_body = ET.tostring(root)

    return request_body



def delete_mock_data(app_config):
    """
    Attempts to delete user records by ids found in the file.
    (These ids are stored at the time mock data is POSTed to the server that
    provides id for each record on his own.)
    """
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
    """
    Writes to file POSTed users' ids provided by the server in the response.
    """
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
    """Returns a list of all ids stored in the file"""
    with open('../utils/jsonmodels/mock_users_ids.json', 'r+') as file:
        file_contents = file.read()
        data = {"user_ids": []} # just in case file is empty
        data = json.loads(file_contents)
    return data["user_ids"]


def get_user_json_schema():
    """
    Schema of the correct response user record
    id is provided by the server
    """
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



