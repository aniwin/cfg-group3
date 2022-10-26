from pet_object import *

def thanks(func):
    def wrapper():
        func()
        print(f"Thanks for play with {my_pet.get_name()}")
    return wrapper