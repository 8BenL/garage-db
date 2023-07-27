from classes import Car
import files
import pickle


def add(name:str="name", year:int=0, color:str="color", number:str="0", owner:str="owner", visit_date:str="", service_date:str=""):
    cars=files.load()
    cars.append(Car(name=name, year=year, color=color, number=number, owner=owner, visit_date=visit_date, service_date=service_date))
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)       



def delete(name):
    contacts=files.load()
    for contact in contacts.copy():
        if contact.name==name:
            contacts.remove(contact)
    files.save(contacts)

def update(name, new_phone):
    add(name, new_phone)
    delete(name)

def search(query):
    cars=files.load()
    results=[]
    for car in cars:
        if query in car.name or query in car.number:
            results.append(car)
    return results                

