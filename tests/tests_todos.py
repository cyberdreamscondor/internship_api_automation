from endpoints.todos import Todos


def test_get_todos(app_config):
    todos = Todos()
    todos.get_todos(app_config.base_url, 200)