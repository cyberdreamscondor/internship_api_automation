from endpoints.comments import Comments


def test_get_comments(app_config):
    comments = Comments()
    comments.get_comments(app_config.base_url, 200)




