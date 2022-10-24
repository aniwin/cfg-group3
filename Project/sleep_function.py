from pet_object import *


# def run_sleep_menu():
#     sleep_menu(sleep_menu)

def sleep_menu(redirect_to_home): # this allows us to redirect the user back to the main page,
                                  # this is to avoid a circular import error
    while not my_pet.sleep:
        sleep = (input('would you like to put pet to sleep? y/n:'))
        if sleep == 'y':
            my_pet.is_asleep()
            redirect_to_home()
        elif sleep == 'n':
            my_pet.is_not_asleep()
            redirect_to_home()
        else:
            print('unsure of your option, please try again')
            sleep_menu(redirect_to_home)
    else:
        sleep = (input('would you like to wake your pet up? y/n:'))
        if sleep == 'y':
            my_pet.is_not_asleep()
            redirect_to_home()
        elif sleep == 'n':
            my_pet.is_asleep()
            redirect_to_home()
        else:
            print('unsure of your option, please try again')
            sleep_menu(redirect_to_home)


