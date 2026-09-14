from dataclasses import dataclass

@dataclass
class UserRegistr:
    username: str
    password: str
    firstName: str
    lastName: str

@dataclass
class UserLogin:
    username: str
    password: str