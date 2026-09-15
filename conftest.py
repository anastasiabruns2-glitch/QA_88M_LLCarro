# Bibliotheken:
import pytest
import requests
import time
import random

from config import *
from faker import Faker

from models.car_dto import Car
from models.user_dto import UserRegistr, UserLogin

fake = Faker()

# Fixtures:
@pytest.fixture(scope="session")
def registration_url():
    return BASE_URL + API_VERSION + REGISTRATION_URL

@pytest.fixture(scope="session")
def login_url():
    return BASE_URL + API_VERSION + LOGIN_URL

@pytest.fixture(scope="session")
def add_new_car_url():
    return BASE_URL + API_VERSION + ADD_NEW_CAR_URL

@pytest.fixture(scope="session")
def get_user_car_url():
    return BASE_URL + API_VERSION + GET_USER_CARS_URL

@pytest.fixture(scope="session")
def delete_user_car_by_id_url():
    return BASE_URL + API_VERSION + DELETE_CAR_BY_ID

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    yield s
    s.close()

@pytest.fixture(scope="function")
def random_user():
    username = f"qa_¨{int(time.time())}_{fake.email()}"
    password = fake.password(
        length=random.randint(8, 15),
        special_chars=False,
        digits=True,
        upper_case=True,
        lower_case=True,
    )+"$"
    firstName = fake.first_name()
    lastName = fake.last_name()
    return UserRegistr(
        username=username,
        password=password,
        firstName=firstName,
        lastName=lastName,)

@pytest.fixture(scope="function")
def registered_user(session, registration_url): #
    return UserLogin(TEST_EMAIL, TEST_PASSWORD)

@pytest.fixture(scope="function")
def auth_token(session, registration_url, random_user):
    user_data = {
        "username": random_user.username,
        "password": random_user.password,
    }
    response = session.post(registration_url, json=user_data)
    assert response.status_code == 200, (
        f"Failed registration {response.status_code} {response.text}"
    )
    return response.json()["accessToken"]

@pytest.fixture(scope="function")
def auth_headers(auth_token):
    return {"Authorization": auth_token}

@pytest.fixture(scope="function")
def random_car():
    return Car(
        serialNumber=f"FGH-{random.randint(1, 100)}",
        manufacture=fake.company(),
        model="Nimbus2000",
        year=str(random.randint(0, 2026)),
        fuel=random.choice(["Diesel", "Petrol", "Hybrid", "Electric", "Gas"]),
        seats=random.randint(2, 20)  ,
        carClass="HJ",
        pricePerDay=round(random.uniform(0.0, 1000.0), 2), # float  # как отобразить number($double),
        about=f"{fake.text(max_nb_chars=25)}",
        city="Haifa",
    )