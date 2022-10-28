from rock_paper_scissors_menu import *
from pet_object import *
from ascii_text import *

from available_levels import *
import random
from datetime import datetime
import os
from retrieve_daily_scores import *

# get the user guess for rock/paper/scissors
def get_user_guess():
    try:
        guess = input(str("Enter rock👊(r)/paper✋(p)/scissors✌(s): ")).lower()

        if guess == "r":
            return "rock👊"
        elif guess == "p":
            return "paper✋"
        elif guess == "s":
            return "scissors✌"
        else:
            raise Exception()
    except:
        print("Input must be r/p/s")
        get_user_guess()

# rock paper scissors game
def rock_paper_scissors(return_to_games_menu):
    # level = 0
    available_levels

    user_score = int(0)
    pet_score = int(0)
    score_limit = 3

    # message to say what you played vs the pet
    def who_played_what():
        print(f"YOU played: {user_guess} VS {my_pet.get_name()} played: {pet_guess}")

    # message to inform user of the current score
    def current_score():
        print(f"YOU: {user_score} VS {my_pet.get_name()}: {pet_score}")

    def user_scored():
        print("You scored!")

    def pet_scored():
        print(f"{my_pet.get_name()} scored!")

    def tie():
        print("Tie!")

    # if user wins add a * to the csv file if there are less than 10 * already
    def user_won_game():
        if user_score == score_limit:
            with open("daily_scores_rock_paper_scissors.csv", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences < 10:
                    with open("daily_scores_rock_paper_scissors.csv", 'a+') as text_file:
                        text_file.write("*")

    def user_won_message():
        you_win_ascii()
        get_daily_rock_paper_scissors_score()
        repeat_game()


    # if user loses remove a * from the csv file as long as the csv already contains at least 1 *
    def pet_won_game():
        if pet_score == score_limit:
            with open("daily_scores_rock_paper_scissors.csv", 'r+') as file:
                data = file.read()
                occurrences = data.count("*")
                if occurrences >= 1:
                    with open("daily_scores_rock_paper_scissors.csv", 'rb+') as delete_score:
                        delete_score.seek(-1, os.SEEK_END)
                        delete_score.truncate()

    def pet_won_message():
        you_lost_ascii()
        get_daily_rock_paper_scissors_score()
        repeat_game()

    # ask user if they want to play aain
    def repeat_game():
        try:
            play_again = input("Play again? y/n: ").lower()
            if play_again == "y":
                rock_paper_scissors(return_to_games_menu)
            elif play_again == "n":
                return_to_games_menu()
            else:
                raise Exception()
        except:
            print('Invalid choice!')
            repeat_game()

    # keep playing until the score limit of 3 is reached by either user or pet
    while user_score != score_limit or pet_score != score_limit:
        try:
            user_guess = get_user_guess()
        except:
            print("Invalid input! try again")
            user_guess = get_user_guess()

        # list of available choices
        my_list = ["rock👊", "paper✋", "scissors✌"]
        # pet guesses at random from the list
        pet_guess = random.choice(my_list)
        # current score is displayed
        current_score()

        # If pet and user guess the same, then tie
        if pet_guess == user_guess:
            who_played_what()
            tie()
            current_score()

        # if user wins
        if (pet_guess == "rock👊" and user_guess == "paper✋") \
                or (pet_guess == "scissors✌" and user_guess == "rock👊") \
                or (pet_guess == "paper✋" and user_guess == "scissors✌"):
            user_score = int(user_score) + 1
            who_played_what()
            user_scored()
            current_score()

            if user_score == score_limit:
                user_won_game()
                user_won_message()

        # if pet wins
        if (pet_guess == "rock👊" and user_guess == "scissors✌") \
                or (pet_guess == "paper✋" and user_guess == "rock👊") \
                or (pet_guess == "scissors✌" and user_guess == "paper✋"):
            pet_score = int(pet_score) + 1
            who_played_what()
            pet_scored()
            current_score()

            if pet_score == score_limit:
                pet_won_game()
                pet_won_message()