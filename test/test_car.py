from dataclasses import asdict
from faker import Faker
import random
import pytest
from config import *

fake = Faker()

class TestCars:
    @pytest.mark.smoke
    def test_add_new_car_positive(self, session, add_new_car_url, auth_headers, random_car):
        response = session.post(
            add_new_car_url,
            headers=auth_headers,
            json=asdict(random_car)
        )

        print("REQUEST:", asdict(random_car))
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        assert response.status_code == 200
        assert "Car added successfully" in response.json()["message"]

    @pytest.mark.smoke
    def test_get_all_cars_positive(self, session, get_user_car_url, auth_headers):
        response = session.get(
            get_user_car_url,
            headers=auth_headers
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        assert response.status_code == 200
        assert isinstance(response.json()["cars"], list)


    def test_get_all_cars_negative_wrong_token(self, session, get_user_car_url):
        headers = {"Authorization": "Lorem Ipsum"}
        response = session.get(
            get_user_car_url,
            headers=headers
        )
        print("REQUEST:", response)
        # Как я могу узнать, что запрашивает get?
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        assert response.status_code == 401
        assert response.json()["error"] == "Unauthorized"

    @pytest.mark.smoke
    def test_get_all_cities_positive(self, session, get_all_cities_url, auth_headers):
        response = session.get(
            get_all_cities_url,
            headers=auth_headers
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        assert response.status_code == 200
        assert isinstance(response.json()["cities"], list)

    def test_get_all_cities_negative_wrong_token(self, session, get_all_cities_url):
        headers = {"Authorization": "Lorem Ipsum"}
        response = session.get(
            get_all_cities_url,
            headers=headers
        )
        print(response)
        assert response.status_code == 401
        assert response.json()["error"] == "Unauthorized"

    @pytest.mark.smoke
    def test_delete_contact_positive(self, session, add_new_car_url, auth_headers, create_car_serial_number):
        car_serial_number = create_car_serial_number
        response = session.delete(f"{add_new_car_url}/{car_serial_number}", headers=auth_headers)
        print(">> ONLY MESSAGE" , response.json())
        assert response.status_code == 200
        assert "Car deleted successfully" in response.json()["message"]

    def test_delete_contact_negative(self, session, add_new_car_url, auth_headers):
        car_serial_number = "HJK-56789"
        response = session.delete(f"{add_new_car_url}/{car_serial_number}", headers=auth_headers)
        print(">> ONLY MESSAGE" , response.json())
        assert response.status_code == 400
        assert "not found" in response.json()["message"]