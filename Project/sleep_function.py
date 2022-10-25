import time

from pet_object import *


def sleep_menu(redirect_to_home):   # avoiding a circular import error
    if not my_pet.get_sleep():
        sleep = (input(f'Would you like to put {my_pet.get_name()} to sleep? y/n:'))
        if sleep == 'y':
            my_pet.update_sleep(True)
            print(f"Sssshhh.... let's not make too much noise, {my_pet.get_name()} is asleep")
            time.sleep(2)
            redirect_to_home()
        elif sleep == 'n':
            print(f"For now, {my_pet.get_name()} is still awake. Come back here if you change your mind")
            time.sleep(2)
            redirect_to_home()
        else:
            print('Unsure of your option, please try again')
            sleep_menu(redirect_to_home)
    else:
        wake = (input(f"Would you like to wake {my_pet.get_name()} up from their sleep? y/n:"))
        if wake == 'y':
            my_pet.update_sleep(False)
            print(f"{my_pet.get_name()} is awake and happy to see you!")
            time.sleep(2)
            redirect_to_home()
        elif wake == 'n':
            print(f"Ssshhh.... {my_pet.get_name()} is still asleep")
            time.sleep(2)
            redirect_to_home()
        else:
            print('Unsure of your option, please try again')
            sleep_menu(redirect_to_home)



