from endpoints.users import Users


def test_get_users(app_config):
    users = Users()
    users.get_users(app_config.base_url, 200)