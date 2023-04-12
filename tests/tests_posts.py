from endpoints.posts import Posts
from utils.jsonmodels import posts_json

posts = Posts()

# GET REQUESTS


def test_get_posts(app_config):
    posts.get_posts(app_config.base_url, 200)


def test_get_user_id(app_config):
    user_id = "938855"
    json = posts_json.create_post_json(int(user_id), "New project", "New post")
    posts.create_post(app_config.base_url, 201, json)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['user_id'] == int(user_id)
    post_id = response_body[0]['id']
    posts.delete_user_post(app_config.base_url, 204, str(post_id))


def test_get_post_title(app_config):
    user_id = "936238"
    title = "New project"
    json = posts_json.create_post_json(int(user_id), title, "New post")
    posts.create_post(app_config.base_url, 201, json)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['title'] == title
    post_id = response_body[0]['id']
    posts.delete_user_post(app_config.base_url, 204, str(post_id))


def test_get_post_body(app_config):
    user_id = "939307"
    body = "New body"
    json = posts_json.create_post_json(int(user_id), "The best title", body)
    posts.create_post(app_config.base_url, 201, json)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['body'] == body
    post_id = response_body[0]['id']
    posts.delete_user_post(app_config.base_url, 204, str(post_id))


def test_user_id_in_list(app_config):
    user_id = "936653"
    json = posts_json.create_post_json(int(user_id), "New project", "New post")
    posts.create_post(app_config.base_url, 201, json)
    user_id_list = posts.get_post_user_id(app_config.base_url, 200)
    assert int(user_id) in user_id_list
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    post_id = response_body[0]['id']
    posts.delete_user_post(app_config.base_url, 204, str(post_id))


#DELETE REQUESTS


def test_delete_user_post(app_config):
    user_id = "941127"
    json = posts_json.create_post_json(int(user_id), "New project", "New post")
    posts.create_post(app_config.base_url, 201, json)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['user_id'] == int(user_id)
    post_id = response_body[0]['id']
    posts.delete_user_post(app_config.base_url, 204, str(post_id))
    new_user_id_list = posts.get_post_user_id(app_config.base_url, 200)
    assert post_id not in new_user_id_list



