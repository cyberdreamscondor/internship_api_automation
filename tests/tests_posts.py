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

# CREATE A POST USING POST REQUEST
def test_create_user_post(app_config):
    user_id = "1178225"
    json = posts_json.create_post_json(int(user_id), "New project", "New body")
    posts.create_post(app_config.base_url, 201, json)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['user_id'] == int(user_id), "Post created successfully."


# UPDATE CREATED POST USING PUT REQUEST
def test_edit_user_post(app_config):
    user_id = "1178225"
    json = posts_json.update_post_json(int(user_id), "Latest version of title", "Latest version of body")
    post_id = "14963"
    posts.update_user(app_config.base_url, 200, json, post_id)
    response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    assert response_body[0]['title'] == "Latest version of title"
    assert response_body[0]['body'] == "Latest version of body"
    print("Post edited successfully.")


#  DELETE UPDATED POST USING DELETE REQUEST
def test_delete_edited_user_post(app_config):
    post_id = "14963"
    posts.delete_user_post(app_config.base_url, 204, post_id)
    # user_id = "1028036"
    # response_body = posts.get_post_data(app_config.base_url, 200, user_id)
    new_user_id_list = posts.get_post_user_id(app_config.base_url, 200)
    assert post_id not in new_user_id_list
    print("Post deleted successfully.")


#  DELETE ALREADY DELETED POST
def test_delete_deleted_user_post(app_config):
    post_id = "14964"
    posts.delete_user_post(app_config.base_url, 204, post_id)
    response_status = posts.delete_user_post(app_config.base_url, 404, post_id)
    assert response_status == 404, "Delete request did not return a 404 status code"
    new_user_id_list = posts.get_post_user_id(app_config.base_url, 200)
    assert post_id not in new_user_id_list, "Post still appears in the list of user posts"
    print("Test passed successfully.")


