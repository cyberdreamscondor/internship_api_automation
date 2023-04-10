import pytest
from config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="local",
        help="Environment to run tests against"
    )


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")



@pytest.fixture(scope='session')
def app_config(env):
    conf = Config(env)
    return conf

