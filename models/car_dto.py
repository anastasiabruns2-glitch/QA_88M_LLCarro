from dataclasses import dataclass

@dataclass
class Car:
    serialNumber : str
    manufacture : str
    model : str
    year : str
    fuel : str
    seats : int # Что означает ($int32)?
    carClass : str
    pricePerDay: float # как отобразить number($double) ?
    about : str
    city : str
