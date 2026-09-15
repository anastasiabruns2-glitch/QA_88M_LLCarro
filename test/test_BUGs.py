import pytest
from conftest import *
from faker import Faker
from models.user_dto import UserRegistr

class TestRegistrationBug:
    def test_registration_negative_invalid_email_BUG(self, session, registration_url):
        user = UserRegistr("gh@gfghcom", "Qwerty123$", "Bob", "Blalbla")
        body = {
            "username": user.username,
            "password": user.password,
            "firstName": user.firstName,
            "lastName": user.lastName,
        }
        response = session.post(registration_url, json=body)
        print(response.json()) #um zu sehen, welche message kommt
        data = response.json()
        assert response.status_code == 400#
        assert "must be a well-formed" in data["message"]["username"] # BUG: 'User already exists'

    def test_registration_negative_invalid_password_BUG(self, session, registration_url, invalid_password):
        user = UserRegistr(fake.email(), "Qwert y123!", "Bob", "Blalbla")
        body = {
            "username": user.username,
            "password": user.password,
            "firstName": user.firstName,
            "lastName": user.lastName,
        }
        response = session.post(registration_url, json=body)
        print(response.json())  # um zu sehen, welche message kommt
        data = response.json()
        assert response.status_code == 400  #
        assert "must be a well-formed" in data["message"]["username"]