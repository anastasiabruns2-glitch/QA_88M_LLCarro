

class TestLogin:

    def test_login_positiv(self, session, login_url, registered_user):
        body = {
            "username": registered_user.username,
            "password": registered_user.password,
        }
        headers = {"Content-Type": "application/json"}
        response = session.post(login_url, json=body, headers=headers)
        assert response.status_code == 200
        assert "accessToken" in response.json().keys()
