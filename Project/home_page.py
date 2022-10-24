import sys
import time
from game_menu import *
from food_menu import *
from view_stats_menu import *
from pet_object import *
from midnight_reset import *
from sleep_function import *
from ascii_text import *

midnight_reset()
def main_menu():
    print('''
                                        loading...
    ''')
    name_of_game()
    time.sleep(1.5)

    if my_pet.sleep == True:
        main_menu_choice = input(f"""
                              1: {my_pet.get_name()} is asleep and cannot play
                              2: {my_pet.get_name()} is asleep and cannot eat
                              3: Do you want to wake {my_pet.get_name()}?
                              4: View {my_pet.get_name()}'s current stats
                              5. End Game

                              Please enter your choice: """)

        if main_menu_choice == "1":

            print(f'''
                            This cannot be done while {my_pet.get_name()} is asleep
                            We will refresh this page.
            ''')
            time.sleep(3)
            main_menu()
        elif main_menu_choice == "2":
            print('''
                            This cannot be done while {my_pet.get_name()} is asleep
                            We will refresh this page.
                        ''')
            time.sleep(3)
            main_menu()
        elif main_menu_choice == "3":
            print('''
                                        This will redirect to the sleep menu
                        ''')
            time.sleep(3)
            sleep_menu()
        elif main_menu_choice == "4":
            print('''
                            This will redirect to the stats menu
            ''')
            time.sleep(3)
            stats_menu()
        elif main_menu_choice == "5":
            print('''
                            Continuing will end all current progress
            ''')
            time.sleep(1.5)
            print('''
                            Are you sure you would like to end this game?
            ''')
            time.sleep(1.5)
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
                sys.exit()
            elif end_game == "2":
                main_menu()
            else:
                print('''
                            You have not selected End Game so we will redirect you back to the Main Menu
                ''')
                main_menu()
        else:
            print('''
                            You must only select either 1, 2, 3, or 4
            ''')
            print('''
                            Please try again
            ''')
            main_menu()
    elif my_pet.sleep != True:

        main_menu_choice = input(f"""
                              1: Play a game with {my_pet.get_name()}
                              2: Feed {my_pet.get_name()}
                              3: Put {my_pet.get_name()} to sleep
                              4: View {my_pet.get_name()}'s current stats
                              5. End Game
        
                              Please enter your choice: """)

        if main_menu_choice == "1":

            print('''
                            This will redirect to the game menu
            ''')
            time.sleep(3)
            menu_games()
        elif main_menu_choice == "2":
            print('''
                                        This will redirect to the food menu
                        ''')
            time.sleep(3)
            feed_pet()
        elif main_menu_choice == "3":
            print('''
                                        This will redirect to the sleep menu
                        ''')
            time.sleep(3)
            sleep_menu()
        elif main_menu_choice == "4":
            print('''
                            This will redirect to the stats menu
            ''')
            time.sleep(3)
            stats_menu()
        elif main_menu_choice == "5":
            print('''
                            Continuing will end all current progress
            ''')
            time.sleep(1.5)
            print('''
                            Are you sure you would like to end this game?
            ''')
            time.sleep(1.5)
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
                sys.exit()
            elif end_game == "2":
                main_menu()
            else:
                print('''
                            You have not selected End Game so we will redirect you back to the Main Menu
                ''')
                main_menu()
        else:
            print('''
                            You must only select either 1, 2, 3, or 4
            ''')
            print('''
                            Please try again
            ''')
            main_menu()


if __name__ == "__main__":
    main_menu()