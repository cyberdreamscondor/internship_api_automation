import json


def create_post_json(user_id, title, body):

    data = {
        "user_id": user_id,
        "title": title,
        "body": body
    }

    json_data = json.dumps(data)
    return json_data


def update_product_json(user_id, title, body):
    data = {
        "user_id": user_id,
        "title": title,
        "body": body
    }

    json_data = json.dumps(data)
    return json_data


