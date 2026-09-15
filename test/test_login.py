import pytest
from config import TEST_PASSWORD

class TestLogin:
    def test_login_positiv(self, session, login_url, registered_user):
        body = {
            "username": registered_user.username,
            "password": registered_user.password,
        }
        response = session.post(login_url, json=body)
        assert response.status_code == 200
        assert "accessToken" in response.json().keys()

    @pytest.mark.parametrize("invalid_username", [
        "",
        "dfg@ghj.com",
    ])

    def test_login_negativ_wrong_email(self, session, login_url, invalid_username):
        body = {
            "username": invalid_username,
            "password": TEST_PASSWORD,
        }
        response = session.post(login_url, json=body)
        print(response.json())
        assert response.status_code == 401
        assert "Login or Password incorrect" in response.json().values()

    @pytest.mark.parametrize("invalid_password", [
        "",
        "Qwerty123!$",
    ])

    def test_login_negativ_wrong_password(self, session, login_url, invalid_password):
        body = {
            "username": TEST_PASSWORD,
            "password": invalid_password,
        }
        response = session.post(login_url, json=body)
        print(response.json())
        assert response.status_code == 401
        assert "Login or Password incorrect" in response.json().values()