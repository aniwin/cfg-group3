import random
from home_page import *
from pet_object import *


def character_name():

    pet_name = my_pet.update_name(input("""
                            What would you like to call your pet?: 
    """).title())
    confirm = input("""
                            Are you sure you would like to call your pet {}? y/n:
    """.format(my_pet.get_name()))
    while confirm != 'y' and confirm != 'n':
        confirm = input("""
                            Not a valid input. 
                            Please press 'y' if you would like to name your pet {}, or 'n' if you would like to try a new name:
        """.format(my_pet.get_name()).lower())
    while confirm == 'n':
        pet_name = my_pet.update_name(input("""
                            What would you like to call your pet?:
        """))
        confirm = input("""
                            Are you sure you would like to call your pet {}? y/n:
        """.format(my_pet.get_name()).lower())
        while confirm != 'y' and confirm != 'n':
            confirm = input("""
                            Not a valid input. 
                            Please press 'y' if you would like to name your pet {}, or 'n' if you would like to try a new name:
            """.format(pet_name).lower())
    if confirm == 'y':

        print(f"""
                            It's time to meet {(my_pet.get_name())}!
        """)
        main_menu()


    pet_gender = "unknown"
    gender_choose_or_random = input(f"""
                            Would you like to choose your {my_pet.get_name()}'s gender or have it randomly assigned? 
                            Respond with 'choose' or 'random':
    """)
    while gender_choose_or_random != "choose" and gender_choose_or_random != "random":
        print("""
                            Sorry that is not a valid input.
        """)
        gender_choose_or_random = input(f"""
                            Would you like to choose your {my_pet.get_name()}'s gender or have it randomly assigned? 
                            Respond with 'choose' or 'random':
        """)
    if gender_choose_or_random == "choose":
        while pet_gender != "male" and pet_gender != "female":
            gender_choice = my_pet.update_gender(input(f"""
                            Would you like {my_pet.get_name()} to be male or female? m/f:
            """))
            if gender_choice == "m":
                pet_gender = "male"
                print(f"""
                            Congratulations, {my_pet.get_name()} is male!
                """)

                main_menu()
            elif gender_choice == "f":
                pet_gender = "female"
                print(f"""
                            Congratulations, {my_pet.get_name()} is female!
                """)
                main_menu()
            else:
                print("""
                            Sorry that gender isn't currently available, please select from the available options.
                """)
    elif gender_choose_or_random == "random":
        gender_list = ["male", "female"]
        pet_gender = (random.choice(gender_list))
        if pet_gender == "male":
            my_pet.update_gender(pet_gender)
            print(f"""
                            Congratulations, {my_pet.get_name()} is male!
            """)

            main_menu()
        elif pet_gender == "female":
            my_pet.update_gender(pet_gender)
            print(f"""
                            Congratulations, {my_pet.get_name()} is female!
            """)

            main_menu()







if __name__ == "__main__":
    character_name()
