from pet_object import *

def thanks(func):
    def wrapper(*args):
        func(*args)
        print(f"Thanks for playing with {my_pet.get_name()}")
    return wrapper

def birthday(func):
    '''Log the time and date your pet was born'''

    def wrapper():
        func()
        now = datetime.now()
        bday = now.strftime("%H:%M:%S on %B %d, %Y")
        print(f"{my_pet.get_name()} was born at {bday}")
    return wrapper