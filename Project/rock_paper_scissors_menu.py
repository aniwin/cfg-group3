from game_menu import *
from home_page import *
from pet_object import *
from available_levels import *
import random
from datetime import datetime
import os
from retrieve_daily_scores import *
from rock_paper_scissors_game import *
def rock_paper_scissors_menu(redirect_to_games):

    print("ROCK👊 PAPER✋ SCISSORS✌")
    choice = input("1: PLAY\n2: RULES\n3: Return to GAMES MENU\nPlease choose an option: ")

    if choice == "1":
        rock_paper_scissors(rock_paper_scissors_menu)
    elif choice == "2":
        print("""
                Rock👊 Paper✋ Scissors✌ rules:
                If you choose Rock👊, you will win against Scissors✌ but lose against Paper✋.
                If you choose Scissors✌, you will win against Paper✋ but lose against Rock👊.
                If you choose Paper✋, you will win against Rock👊 but lose against Scissors✌.
                The game ends when somebody gets 3 wins. """)
        rock_paper_scissors_menu(redirect_to_games)

    elif choice == "3":
        redirect_to_games()
    else:
        print("Choose 1, 2, or 3!")
        rock_paper_scissors_menu(redirect_to_games)

