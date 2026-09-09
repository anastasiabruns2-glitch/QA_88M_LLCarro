
import pytest
import requests
from config import *

@pytest.fixture(scope="session")
def registration_url():
    return BASE_URL + API_VERSION + REGISTRATION_URL

@pytest.fixture(scope="session")
def login_url():
    return BASE_URL + API_VERSION + LOGIN_URL

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    yield s