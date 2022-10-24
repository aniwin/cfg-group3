from home_page import *
from pet_object import *


def sleep_menu():
    while not my_pet.sleep:
        sleep = (input('would you like to put pet to sleep? y/n:'))
        if sleep == 'y':
            my_pet.is_asleep()
            main_menu()
        elif sleep == 'n':
            my_pet.is_not_asleep()
            main_menu()
        else:
            print('unsure of your option, please try again')
            sleep_menu()
    else:
        sleep = (input('would you like to wake your pet up? y/n:'))
        if sleep == 'y':
            my_pet.is_not_asleep()
            main_menu()
        elif sleep == 'n':
            my_pet.is_asleep()
            main_menu()
        else:
            print('unsure of your option, please try again')
            sleep_menu()


if __name__ == "__main__":
    sleep_menu()
