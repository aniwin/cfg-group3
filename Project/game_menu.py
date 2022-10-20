from weather_menu import *
from rock_paper_scissors_menu import *
from main_menu import *

def game_menu():
    print("GAMES")
while True:
    try:
        choice = int(input("1: Rock👊 Paper✋ Scissors✌\n2: Get my weather advice\n3: Return to main menu\nPlease choose an option: "))

        if choice == "1":
            rock_paper_scissors_menu()
        elif choice == "2":
            weather_advisor()
        elif choice == "3":
            main_menu()     # link back to main menu
    except:
        print("invalid input")
    else:
        if 1 <= choice <= 3:
            break
        else:
            print("Number out of range")
if __name__ == "__main__":
    game_menu()