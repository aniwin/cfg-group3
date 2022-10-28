import random
import time

from home_page import *
from pet_object import *


import random
from datetime import datetime
from home_page import *
from pet_object import *

# birthday decorator
def birthday(func):
    '''Log the time and date your pet was born'''

    def wrapper():
        func()
        now = datetime.now()
        bday = now.strftime("%H:%M:%S on %B %d, %Y")
        print(f"{my_pet.get_name()} was born at {bday}")
    return wrapper

# @birthday
def character_name():
    # using random for the computer to randomly choose a gender
    def random_gender():
        gender_list = ["male", "female"]
        pet_gender = my_pet.update_gender(random.choice(gender_list))
        print(f"Congratulations, {my_pet.get_name()} is {my_pet.get_gender()}!")
        time.sleep(1.5)
        main_menu()

    # for the user to choose a gender
    def choose_gender():
        try:
            gender_choice = my_pet.update_gender(str(input(f"Would you like {my_pet.get_name()} to be male or female? male/female:")).lower())

            if my_pet.get_gender() == "male":
                print(f"Congratulations, {my_pet.get_name()} is {my_pet.get_gender()}!")
                time.sleep(1.5)
                main_menu()
            elif my_pet.get_gender() == "female":
                print(f"Congratulations, {my_pet.get_name()} is {my_pet.get_gender()}!")
                time.sleep(1.5)
                main_menu()
            else:
                raise Exception()
        except:
            print("Invalid input!")
            choose_gender()

    # asking the user if they want to choose the gender or randomly have a gender assigned
    def decide_gender():
        try:
            gender_choose_or_random = input(f"""Would you like to choose your {my_pet.get_name()}'s gender or have it randomly assigned?
            Respond with 'choose' or 'random':
             """)
            if gender_choose_or_random == "random":
                random_gender()
            elif gender_choose_or_random == "choose":
                choose_gender()
            else:
                raise Exception()
        except:
            print("Invalid input!")
            decide_gender()

    # confirm that the user wishes to call their pet a certain name
    def confirm_name():
        try:
            confirm = input("Are you sure you would like to call your pet {}? y/n:".format(my_pet.get_name()))
            if confirm == "y":
                print(f"It's time to meet {(my_pet.get_name())}!")
                decide_gender()
            elif confirm == "n":
                character_name()
            else:
                raise Exception()
        except:
            print("Invalid input!")
            confirm_name()

    # updates the my_pet object with the pet name
    my_pet.update_name(input("What would you like to call your pet?:").title())

    if my_pet.get_name() == "":
        print("Invalid input! You didn't give your pet a name!")
        character_name()
    else:
        confirm_name()


if __name__ == "__main__":
    character_name()