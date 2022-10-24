from game_menu import *
from home_page import *
from pet_object import *
from ascii_art import *
from available_levels import *
import random
from datetime import datetime
import os
from retrieve_daily_scores import *

def rock_paper_scissors(return_to_games):
    level = 0
    available_levels #= {
    #     0: "□ □ □ □ □ □ □ □ □ □",
    #     1: "■ □ □ □ □ □ □ □ □ □",
    #     2: "■ ■ □ □ □ □ □ □ □ □",
    #     3: "■ ■ ■ □ □ □ □ □ □ □",
    #     4: "■ ■ ■ ■ □ □ □ □ □ □",
    #     5: "■ ■ ■ ■ ■ □ □ □ □ □",
    #     6: "■ ■ ■ ■ ■ ■ □ □ □ □",
    #     7: "■ ■ ■ ■ ■ ■ ■ □ □ □",
    #     8: "■ ■ ■ ■ ■ ■ ■ ■ □ □",
    #     9: "■ ■ ■ ■ ■ ■ ■ ■ ■ □",
    #     10: "■ ■ ■ ■ ■ ■ ■ ■ ■ ■"
    # }


    # time_now = datetime.now()
    # reset_time = (time_now.strftime("%H:%M"))
    # if reset_time == "00:00":
    #     level = 0
    #     with open("daily_scores_rock_paper_scissors.csv", 'w+') as text_file:
    #         pass


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
            with open("daily_scores_rock_paper_scissors.csv", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences < 10:
                    with open("daily_scores_rock_paper_scissors.csv", 'a+') as text_file:
                        text_file.write("*")

        if pet_score == score_limit:
            with open("daily_scores_rock_paper_scissors.csv", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences >= 1:
                    with open("daily_scores_rock_paper_scissors.csv", 'rb+') as delete_score:
                        delete_score.seek(-1, os.SEEK_END)
                        delete_score.truncate()


        if user_score == score_limit:
            you_win_ascii()
            # print("""
            #         ██    ██  ██████  ██    ██     ██     ██ ██ ███    ██
            #          ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██
            #           ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██
            #            ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██
            #            ██     ██████   ██████       ███ ███  ██ ██   ████
            #     """)
            get_daily_rock_paper_scissors_score()
            # with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
            #     data = file.read()
            #     occurrences = data.count("*")
            #     if occurrences in available_levels.keys():
            #         print("-H A P P I N E S S-")
            #         print(available_levels[(occurrences)])

            play_again = input("Play again? y/n: ").lower()
            if play_again == "y":
                rock_paper_scissors(return_to_games)
            else:
                return_to_games()

        elif pet_score == score_limit:
            you_lost_ascii()
            # print("""
            #         ██    ██  ██████  ██    ██     ██       ██████  ███████ ████████
            #          ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██
            #           ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██
            #            ██    ██    ██ ██    ██     ██      ██    ██      ██    ██
            #            ██     ██████   ██████      ███████  ██████  ███████    ██
            #     """)
            get_daily_rock_paper_scissors_score()
            # with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
            #     data = file.read()
            #     occurrences = data.count("*")
            #     if occurrences in available_levels.keys():
            #         print("-H A P P I N E S S-")
            #         print(available_levels[(occurrences)])

            play_again = input("Play again? y/n: ").lower()
            if play_again == "y":
                rock_paper_scissors(return_to_games)
            else:
                print('unsure of your choice. you will be redirected to the rock paper scissors menu')
                return_to_games()


