from dataclasses import asdict
from faker import Faker
import random

fake = Faker()

class TestCars:
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

# >> Не совсем понятно, проверяет ли последнее Assert правильное значение, ведь список возвращается пустым
    def test_get_all_cars_positive(self, session, get_user_car_url, auth_headers):
        response = session.get(
            get_user_car_url,
            headers=auth_headers
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        assert response.status_code == 200
        #assert response.json()["cars"] == []
        assert isinstance(response.json()["cars"], list)

# >> Здесь много вопросов:
    def test_get_all_cars_negative_wrong_token(self, session, get_user_car_url, auth_headers):
        # почему headers отображаются серым цветом
        headers = {"Authorization": "Lorem Ipsum"}
        response = session.get(
            get_user_car_url,
            headers=auth_headers
        )
        print("REQUEST:", response.json()["cars"])
        # Как я могу узнать, что запрашивает get?
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        # >> Я не понимаю, почему здесь возвращается значение 200 и
        assert response.status_code == 401
        #assert response.json()["message"] == "Invalid token"


    def test_get_all_cities_positive(self, session, get_all_cities_url, auth_headers):
        response = session.get(
            get_all_cities_url,
            headers=auth_headers
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        assert response.status_code == 200
        assert isinstance(response.json()["cities"], list)

# Здесь та же ошибка, что и в def test_get_all_cars_negative_wrong_token
    def test_get_all_cities_negative_wrong_token(self, session, get_all_cities_url, auth_headers):
        headers = {"Authorization": "Lorem Ipsum"}
        response = session.get(
            get_all_cities_url,
            headers=auth_headers
        )
        print(response.json())
        assert response.status_code == 401
        #assert response.json()["error"] == "Unauthorized"



