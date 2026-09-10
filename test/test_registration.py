import pytest
from conftest import *

class TestRegistration:

    #positiven Test erzeugen
    def test_registration_positive(self, session, registration_url, random_user):
        print(random_user)
        body = {
            "username": random_user.username,
            "password": random_user.password,
            "firstName": random_user.firstName,
            "lastName": random_user.lastName,
        }
        headers = {
            "Content-Type": "application/json",
        }
        response = session.post(registration_url, json=body, headers=headers)
        assert response.status_code == 200
        assert "accessToken" in response.json().keys()

    def test_registration_negative_duplicate_user(self, session, registration_url, random_user):
        body = {
            "username": random_user.username,
            "password": random_user.password,
            "firstName": random_user.firstName,
            "lastName": random_user.lastName,
        }
        headers = {
            "Content-Type": "application/json",
        }
        session.post(registration_url, json=body, headers=headers)
        response = session.post(registration_url, json=body, headers=headers)
        print(response.json())
        assert response.status_code == 400
        assert "User already exists" in response.json().values()

    @pytest.mark.parametrize("invalid_email", [
        "fgh123.ghj.hjk",
        "fdsdf234@",
        "@ghj.com",
        "gh@ghjcom",
        "fgh@ghj",
        "ghjjkghj@@ghj.com",
        "fghj @hjk.com",
    ])
    def test_registration_negative_invalid_email(self, session, registration_url, invalid_email):
        user = User(invalid_email, "Qwerty123$", "Bob", "Blalbla")
        body = {
            "username": user.username,
            "password": user.password,
            "firstName": user.firstName,
            "lastName": user.lastName,
        }
        headers = {
            "Content-Type": "application/json",
        }
        session.post(registration_url, json=body, headers=headers)
        response = session.post(registration_url, json=body, headers=headers)
        print(response.json()) #um zu sehen, welche message kommt
        assert response.status_code == 400