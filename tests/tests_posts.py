from endpoints.posts import Posts


def test_get_posts(app_config):
    posts = Posts()
    posts.get_posts(app_config.base_url, 200)