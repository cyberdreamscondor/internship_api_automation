from endpoints.users import Users


def test_get_users(app_config):
    users = Users()
    users.get_users(app_config.base_url, 200)

def test_get_user(app_config):
    users = Users()
    users.get_user_by_id(app_config.base_url, 200, "Mukesh Kocchar")

def test_get_user(app_config):
    users = Users()
    users.get_user(app_config.base_url, 200, 642255)