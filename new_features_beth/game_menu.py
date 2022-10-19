from weather_menu import *
from rock_paper_scissors_menu import *
from main_menu import *

def game_menu():
    print("GAMES")
    choice = input("1: Rock👊 Paper✋ Scissors✌\n2: Get my weather advice\n3: Return to main menu\nPlease choose an option: ")

    if choice == "1":
        rock_paper_scissors_menu()
    elif choice == "2":
        weather_advisor()
    elif choice == "3":
        main_menu()     # link back to main menu
    else:
        print("Invalid input. Enter 1, 2 or 3!")
        game_menu()

if __name__ == "__main__":
    game_menu()