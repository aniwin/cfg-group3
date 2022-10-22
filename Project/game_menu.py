from home_page import *
from weather_menu import *
from rock_paper_scissors_menu import *
from pet_object import *

def menu_games():
    print("GAMES")
    choice = input(f"1: Rock👊 Paper✋ Scissors✌\n2: Get weather advice from {my_pet.get_name()}\n3: Return to main menu\nPlease choose an option: ")

    if choice == "1":
        rock_paper_scissors_menu()
    elif choice == "2":
        weather_advisor()
    elif choice == "3":
        main_menu()     # link back to main menu
    else:
        print("Invalid input. Enter 1, 2 or 3!")
        menu_games()

if __name__ == "__main__":
    menu_games()

