import json


def create_post_json(id, user_id, title, body):

    data = {
        "id": id,
        "user_id": user_id,
        "title": title,
        "body": body
    }

    json_data = json.dumps(data)
    return json_data


def update_product_json(id, user_id, title, body):
    data = {
        "id": id,
        "user_id": user_id,
        "title": title,
        "body": body
    }

    json_data = json.dumps(data)
    return json_data


def delete_product_json(id):
    data = {
        "id": id
    }

    return data
