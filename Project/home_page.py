import sys
import time
from rock_paper_scissors_menu import *
from weather_menu import *
from food_menu import *
from view_stats_menu import *
from pet_object import *
from midnight_reset import *
from sleep_function import *
from ascii_text import *
from decorator import *
from closing_scores import *
from mysql_save_file import *

# message to user that pet cannot perform their chosen task while it is sleeping
def cant_do_whilst_sleeping():
    print(f'''
    This cannot be done while {my_pet.get_name()} is asleep
    We will refresh this page.
                ''')
    time.sleep(3)
    main_menu()

# # exit the game completely
# def exit_final():
#     print(f"Thanks for playing with {(my_pet.get_name())}")
#     os._exit(0)
#
# def thanks_for_playing():
#     return exit_final()

# confirm whether the user wants to end the game
def end_game_final():
    try:
        end_game = input('''
                           1. End Game
                           2. Return to Main Menu

                   Please enter your choice:
                   ''')
        if end_game == "1":
            print('''
                       Exiting Game in 3
                       ''')
            time.sleep(1)
            print('''
                       Exiting Game in 2
                       ''')
            time.sleep(1)
            print('''
                       Exiting Game in 1
                       ''')
            time.sleep(1)
            closing_scores()
            insert_new_record(save_data)
            # return thanks_for_playing()

        elif end_game == "2":
            main_menu()
        else:
            raise Exception()
    except:
        print("You need to select 1 or 2!")
        end_game_final()

# menu choices for when the pet is asleep
def main_menu_asleep():
    try:
        main_menu_choice = input(f"""
                1: {my_pet.get_name()} is asleep and cannot play
                2: {my_pet.get_name()} is asleep and discuss the weather
                3: {my_pet.get_name()} is asleep and cannot eat
                4: Do you want to wake {my_pet.get_name()}?
                5: View {my_pet.get_name()}'s current stats
                6: End Game

        Please enter your choice: """)

        if main_menu_choice == "1":
            cant_do_whilst_sleeping()
        if main_menu_choice == "2":
            cant_do_whilst_sleeping()
        if main_menu_choice == "3":
            cant_do_whilst_sleeping()
        elif main_menu_choice == "4":
            print('''
            This will redirect to the sleep menu
                        ''')
            time.sleep(3)
            sleep_menu(main_menu)
        elif main_menu_choice == "5":
            print('''
            This will redirect to the stats menu
            ''')
            time.sleep(3)
            stats_menu(main_menu)
        elif main_menu_choice == "6":
            print('''
            Continuing will end all current progress
            ''')
            time.sleep(1.5)
            print('''
            Are you sure you would like to end this game?
            ''')
            end_game_final()
        else:
            raise Exception()
    except:
        print("Invalid input!")
        main_menu_asleep()

# menu choices for when the pet is awake
def main_menu_awake():
    try:
        main_menu_choice = input(f"""
                1: Play a game of Rock, Paper, Scissors with {my_pet.get_name()}
                2: Guess the weather with {my_pet.get_name()}
                3: Feed {my_pet.get_name()}
                4: Put {my_pet.get_name()} to sleep
                5: View {my_pet.get_name()}'s current stats
                6. End Game

        Please enter your choice: """)
        if main_menu_choice == "1":
            print('''
            This will redirect to the game menu
            ''')
            time.sleep(3)
            rock_paper_scissors_menu(main_menu)
        elif main_menu_choice == "2":
            print('''
            This will redirect to the weather menu
             ''')
            time.sleep(3)
            weather_advisor(main_menu)
        elif main_menu_choice == "3":
            print('''
            This will redirect to the food menu
                        ''')
            time.sleep(3)
            feed_pet(main_menu)
        elif main_menu_choice == "4":
            print('''
            This will redirect to the sleep menu
                        ''')
            time.sleep(3)
            sleep_menu(main_menu)
        elif main_menu_choice == "5":
            print('''
            This will redirect to the stats menu
            ''')
            time.sleep(3)
            stats_menu(main_menu)
        elif main_menu_choice == "6":
            print('''
            Continuing will end all current progress
            ''')
            time.sleep(1.5)
            print('''
            Are you sure you would like to end this game?
            ''')
            end_game_final()
        else:
            raise Exception()
    except:
        print("Invalid input!")
        main_menu_awake()

# main program
def main_menu():
    midnight_reset()

    print('''
                                        loading...
    ''')
    name_of_game()
    time.sleep(1.5)

    if my_pet.get_sleep() == True:
        main_menu_asleep()

    elif my_pet.get_sleep() == False:
        main_menu_awake()

if __name__ == "__main__":
    main_menu()