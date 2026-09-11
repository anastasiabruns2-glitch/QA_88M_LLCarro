# Bibliotheken:
import pytest
import requests
import time
import random

from config import *
from faker import Faker

from models.car_dto import Car
from models.user_dto import User

fake = Faker()

# Fixtures:
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
    s.close()

@pytest.fixture(scope="function")
def random_user():
    username = f"qa_¨{int(time.time())}_{fake.email()}"
    password = fake.password(
        length=random.randint(8, 15),
        special_chars=False,
        digits=True,
        upper_case=True,
        lower_case=True,)+"$"
    firstName = fake.first_name()
    lastName = fake.last_name()
    return User(
        username=username,
        password=password,
        firstName=firstName,
        lastName=lastName)

@pytest.fixture(scope="session")
def add_new_car_url():
    return BASE_URL + API_VERSION + ADD_NEW_CAR_URL

@pytest.fixture(scope="session")
def get_user_car_url():
    return BASE_URL + API_VERSION + GET_USER_CARS_URL

@pytest.fixture(scope="session")
def delete_user_car_by_id_url():
    return BASE_URL + API_VERSION + DELETE_CAR_BY_ID

@pytest.fixture(scope="function")
def create_a_car():
        serialNumber= f"FGH-{random.randint(1, 100)}"
        manufacture = fake.company()
        model= "Nimbus2000"
        year= str(random.randint(0, 2026))
        fuel= random.choice(["Diesel", "Gas", "XXX"]) # prüfen
        seats = random.randint(2, 20)  #
        carClass= "HJ"
        pricePerDay = round(random.uniform(0.0, 1000.0), 2) # float  # как отобразить number($double)
        about = f"{fake.text(max_nb_chars=25)}"
        city = "Haifa"
        return Car(
            serialNumber=serialNumber,
            manufacture=manufacture,
            model=model,
            year=year,
            fuel=fuel,
            seats=seats,
            carClass=carClass,
            pricePerDay=pricePerDay,
            about=about,
            city=city)
