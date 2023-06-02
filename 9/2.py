import pickle
from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Person:
    name: str
    age: int
    address: str

    @classmethod
    def save_obj(cls, lst, filename):
       with open(filename, "wb") as f:
            pickle.dump(lst, f)

    @classmethod
    def load_obj(cls,filename):
        with open(filename, "rb") as f:
            lst = pickle.load(f)
            for person in lst:
                print(person)



lst = [
    Person("reza", 30, "iran"),
    Person("ali", 22, "iran"),
    Person("alireza", 28, "iran"),
    Person("Rana", 24, "iran")
    ]

filename="log.pickle"
Person.save_obj(lst, filename)
Person.load_obj(filename)
