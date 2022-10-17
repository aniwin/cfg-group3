import random
from main_menu import *

class CharacterCreation:
    def __init__(self):

        self.name = "unknown"
        self.confirm = "n"
        self.gender = "unknown"
        self.gender_choice = "n"


    def character_name(self):
        name = input("What would you like to call your pet? ")
        confirm = input("Are you sure you would like to call your pet {}? y/n".format(name))
        while confirm != 'y' and confirm != 'n':
            confirm = input("Not a valid input. Please press 'y' if you would like to name your pet {}, or n if you would like to try a new name".format(name))
        while confirm == 'n':
            name = input("What would you like to call your pet? ")
            confirm = input("Are you sure you would like to call your pet {}? y/n".format(name))
            while confirm != 'y' and confirm != 'n':
                confirm = input(
                    "Not a valid input. Please press 'y' if you would like to name your pet {}, or n if you would like to try a new name".format(
                        name))
        if confirm == 'y':
            print("It's time to meet {}!".format(name))
        return name

    def character_gender(self):
        gender_choose_or_random = input("Would you like to choose your pet's gender or have it randomly assigned? Respond with 'choose' or 'random'")
        while gender_choose_or_random != "choose" and gender_choose_or_random != "random":
            print("Sorry that is not a valid input.")
            gender_choose_or_random = input("Would you like to choose your pet's gender or have it randomly assigned? Respond with 'choose' or 'random'")
        if gender_choose_or_random == "choose":
            while self.gender != "male" and self.gender != "female":
                gender_choice = input("Would you like your pet to be male or female? m/f")
                if gender_choice == "m":
                    gender = "male"
                    print("Congratulations, your new pet is male!")
                    main_menu()
                elif gender_choice == "f":
                    gender = "female"
                    print("Congratulations, your new pet is female!")
                    main_menu()
                else:
                    print("Sorry that gender isn't currently available, please select from the available options.")
        elif gender_choose_or_random == "random":
            gender_list = ["male", "female"]
            gender = (random.choice(gender_list))
            if gender == "male":
                print("Congratulations, your new pet is male!")
                main_menu()
            elif gender == "female":
                print("Congratulations, your new pet is female!")
                main_menu()
        return gender


character = CharacterCreation()
character.character_name()
character.character_gender()

if __name__ == "__main__":
    character_menu()
