import pickle
from classes import Car

def load():
    try:
        with open("cars.pickle", "rb") as f:
            cars=pickle.load(f)
            return cars
    except:
        return [Car()]

def save(contacts:list):
    with open("contacts.pickle", "wb") as f:
        pickle.dump(contacts, f)