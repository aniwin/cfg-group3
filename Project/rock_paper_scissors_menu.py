from game_menu import *
from home_page import *
from pet_object import *

import random
from datetime import datetime
import os

def rock_paper_scissors_menu():

    print("ROCK👊 PAPER✋ SCISSORS✌")
    choice = input("1: PLAY\n2: RULES\n3: Return to GAMES MENU\nPlease choose an option: ")

    if choice == "1":
        rock_paper_scissors()

    elif choice == "2":
        print("""
                Rock👊 Paper✋ Scissors✌ rules:
                If you choose Rock👊, you will win against Scissors✌ but lose against Paper✋.
                If you choose Scissors✌, you will win against Paper✋ but lose against Rock👊.
                If you choose Paper✋, you will win against Rock👊 but lose against Scissors✌.
                The game ends when somebody gets 3 wins. """)
        rock_paper_scissors()

    elif choice == "3":
        menu_games()
    else:
        print("Choose 1, 2, or 3!")
        rock_paper_scissors()

def rock_paper_scissors():
    level = 0
    available_levels = {
        0: "□ □ □ □ □ □ □ □ □ □",
        1: "■ □ □ □ □ □ □ □ □ □",
        2: "■ ■ □ □ □ □ □ □ □ □",
        3: "■ ■ ■ □ □ □ □ □ □ □",
        4: "■ ■ ■ ■ □ □ □ □ □ □",
        5: "■ ■ ■ ■ ■ □ □ □ □ □",
        6: "■ ■ ■ ■ ■ ■ □ □ □ □",
        7: "■ ■ ■ ■ ■ ■ ■ □ □ □",
        8: "■ ■ ■ ■ ■ ■ ■ ■ □ □",
        9: "■ ■ ■ ■ ■ ■ ■ ■ ■ □",
        10: "■ ■ ■ ■ ■ ■ ■ ■ ■ ■"
    }


    time_now = datetime.now()
    reset_time = (time_now.strftime("%H:%M"))
    if reset_time == "00:00":
        level = 0
        with open("daily_scores_rock_paper_scissors.txt", 'w+') as text_file:
            pass


    user_score = int(0)
    pet_score = int(0)
    score_limit = 3

    while user_score != score_limit or pet_score != score_limit:

        user_guess = input(str("Enter rock👊/paper✋/scissors✌: ")).lower()

        if user_guess == "rock":
            user_guess = "rock👊"
        elif user_guess == "paper":
            user_guess = "paper✋"
        elif user_guess == "scissors":
            user_guess = "scissors✌"
        else:
            print("invalid input")
            break

        my_list = "rock👊", "paper✋", "scissors✌"
        pet_guess = random.choice(my_list)
        print(f"YOU played: {user_guess} VS {my_pet.get_name()} played: {pet_guess}")

        if pet_guess == "rock👊" and user_guess == "rock👊":
            print("Tie!")
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "paper✋" and user_guess == "paper✋":
            print("Tie!")
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "scissors✌" and user_guess == "scissors✌":
            print("Tie!")
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "paper✋" and user_guess == "rock👊":
            print(f"{my_pet.get_name()} scored!")

            pet_score = int(pet_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "rock👊" and user_guess == "paper✋":
            print("You scored!")

            user_score = int(user_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "rock👊" and user_guess == "scissors✌":
            print(f"{my_pet.get_name()} scored!")

            pet_score = int(pet_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "scissors✌" and user_guess == "rock👊":
            print("You scored!")

            user_score = int(user_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "paper✋" and user_guess == "scissors✌":
            print("You scored!")

            user_score = int(user_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

        if pet_guess == "scissors✌" and user_guess == "paper✋":
            print(f"{my_pet.get_name()} scored!")

            pet_score = int(pet_score) + 1
            print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")


        if user_score == score_limit:
            with open("daily_scores_rock_paper_scissors.txt", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences < 10:
                    with open("daily_scores_rock_paper_scissors.txt", 'a+') as text_file:
                        text_file.write("*")

        if pet_score == score_limit:
            with open("daily_scores_rock_paper_scissors.txt", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences >= 1:
                    with open("daily_scores_rock_paper_scissors.txt", 'rb+') as delete_score:
                        delete_score.seek(-1, os.SEEK_END)
                        delete_score.truncate()


        if user_score == score_limit:

            print("""
                    ██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ 
                     ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ 
                      ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ 
                       ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██ 
                       ██     ██████   ██████       ███ ███  ██ ██   ████ 
                """)
            with open("daily_scores_rock_paper_scissors.txt", 'r') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences in available_levels.keys():
                    print("-H A P P I N E S S-")
                    print(available_levels[(occurrences)])

            play_again = input("Play again? y/n: ").lower()
            if play_again == "y":
                rock_paper_scissors()
            else:
                menu_games()

        elif pet_score == score_limit:
            print("""  
                    ██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
                     ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
                      ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██    
                       ██    ██    ██ ██    ██     ██      ██    ██      ██    ██    
                       ██     ██████   ██████      ███████  ██████  ███████    ██    
                """)
            with open("daily_scores_rock_paper_scissors.txt", 'r') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences in available_levels.keys():
                    print("-H A P P I N E S S-")
                    print(available_levels[(occurrences)])

            play_again = input("Play again? y/n: ").lower()
            if play_again == "y":
                rock_paper_scissors()
            else:
                main_menu()

if __name__ == "__main__":
    rock_paper_scissors_menu()