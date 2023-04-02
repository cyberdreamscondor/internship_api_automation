from endpoints.posts import Posts

posts = Posts()


def test_get_posts(app_config):
    posts.get_posts(app_config.base_url, 200)


def test_get_post_id(app_config):
    id_list = posts.get_post_id(app_config.base_url, 200)
    first_id = id_list[0]
    new_id_list = posts.get_post_id(app_config.base_url, 200)
    assert first_id in new_id_list


def test_get_posts_by_page(app_config, params={'page': 1, 'per_page': 20}):
    response_body = posts.get_posts_by_page(app_config.base_url, 200, params=params)
    assert response_body is not None


def test_get_post_by_id(app_config):
    id_list = posts.get_post_id(app_config.base_url, 200)
    first_id = id_list[0]
    response_body = posts.get_post_by_id(app_config.base_url, 200, str(first_id))
    assert response_body is not None


def test_get_posts_user_id_list(app_config):
    data = posts.get_post_user_id(app_config.base_url, 200)
    posts.check_posts_data_by_length(data, 10)


def test_get_post_by_incorrect_id(app_config):
    posts.get_post_by_id(app_config.base_url, 404, "0000")
