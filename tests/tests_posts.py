from endpoints.posts import Posts

posts = Posts()
headers = {'Authorization': 'Token c8816a6b5a1ce16041be702d5b0640ed4ba524d18bd27eb35b0f09eed255845f'}


def test_get_posts(app_config):
    posts.get_posts(app_config.base_url, 200)


def test_get_post_id(app_config):
    posts.get_post_id(app_config.base_url, 200, 7445)


def test_get_posts_by_page(app_config, params= {'page':1,'per_page': 1}):
    response_body = posts.get_posts_by_page(app_config.base_url, 200, params=params)
    assert response_body[0]['user_id'] == 663589
    assert response_body[0]['title'] == "Recusandae vetus et tendo ab peior canis repellendus spes."


def test_get_post_by_id(app_config):
    response_body = posts.get_post_by_id(app_config.base_url, 200, "7385")
    assert response_body['user_id'] == 642255
    assert response_body['title'] == "Benigne eveniet trado defungo campana depereo tamisium caelestis."


def test_get_posts_user_id_list(app_config):
    data = posts.get_post_user_id(app_config.base_url, 200)
    posts.check_posts_data_by_length(data, 10)


def test_get_post_by_incorrect_id(app_config):
    posts.get_post_by_id(app_config.base_url, 404, "7320")



