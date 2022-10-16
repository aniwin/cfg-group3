from main_menu import *

import random

def game_menu():
    print("GAMES")
    choice = input("1: Rock👊 Paper✋ Scissors✌\n2: x\n3: Return to main menu\nPlease choose an option: ")

    if choice == "1":
        rock_paper_scissors()
    elif choice == "2":
        another_game()
    elif choice == "3":
        main_menu()     # link back to main menu
    else:
        print("Invalid input. Enter 1, 2 or 3!")
        game_menu()

def rock_paper_scissors():
    print("ROCK👊 PAPER✋ SCISSORS✌")
    choice = input("1: PLAY\n2: RULES\n3: Return to GAMES MENU\nPlease choose an option: ")

    if choice == "1":
        user_score = int(0)
        pet_score = int(0)
        score_limit = 3

        while user_score != score_limit or pet_score != score_limit:

            user_guess = input(str("Enter rock👊/paper✋/scissors✌: ")).lower()
            game_options = ["rock", "paper", "scissors"]
            while user_guess not in game_options:
                user_guess = input(str("invalid input, try again")).lower()

            if user_guess == "rock":
                user_guess = "rock👊"
            elif user_guess == "paper":
                user_guess = "paper✋"
            elif user_guess == "scissors":
                user_guess = "scissors✌"
            else:
                print("invalid input, try again")


            my_list = "rock👊", "paper✋", "scissors✌"
            pet_guess = random.choice(my_list)
            print(f"YOU played: {user_guess} VS PET played: {pet_guess}")

            if pet_guess == "rock👊" and user_guess == "rock👊":
                print("Tie!")
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "paper✋" and user_guess == "paper✋":
                print("Tie!")
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "scissors✌" and user_guess == "scissors✌":
                print("Tie!")
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "paper✋" and user_guess == "rock👊":
                print("Pet scored!")

                pet_score = int(pet_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "rock👊" and user_guess == "paper✋":
                print("You scored!")

                user_score = int(user_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "rock👊" and user_guess == "scissors✌":
                print("Pet scored!")

                pet_score = int(pet_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "scissors✌" and user_guess == "rock👊":
                print("You scored!")

                user_score = int(user_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "paper✋" and user_guess == "scissors✌":
                print("You scored!")

                user_score = int(user_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if pet_guess == "scissors✌" and user_guess == "paper✋":
                print("Pet scored!")

                pet_score = int(pet_score) + 1
                print(f"YOU: {user_score} VS Pet: {pet_score}")

            if user_score == score_limit:
                print("""
                        ██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ 
                         ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ 
                          ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ 
                           ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██ 
                           ██     ██████   ██████       ███ ███  ██ ██   ████ 
                    """)

                play_again = input("Play again? y/n: ").lower()
                if play_again == "y":
                    rock_paper_scissors()
                else:
                    game_menu()

            elif pet_score == score_limit:
                print("""  
                        ██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
                         ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
                          ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██    
                           ██    ██    ██ ██    ██     ██      ██    ██      ██    ██    
                           ██     ██████   ██████      ███████  ██████  ███████    ██    
                    """)

                play_again = input("Play again? y/n: ").lower()

                if play_again == "y":
                    rock_paper_scissors()
                elif play_again == "n":
                    game_menu()
                play_again_options = ["y", "n"]
                while play_again not in play_again_options:
                    play_again = input(str("invalid input, try again")).lower()
    elif choice == "2":
        print("""
                Rock👊 Paper✋ Scissors✌ rules:
                If you choose Rock👊, you will win against Scissors✌ but lose against Paper✋.
                If you choose Scissors✌, you will win against Paper✋ but lose against Rock👊.
                If you choose Paper✋, you will win against Rock👊 but lose against Scissors✌.
                The game ends when somebody gets 3 wins. """)
        rock_paper_scissors()

    elif choice == "3":
        game_menu()
    else:
        print("Choose 1, 2, or 3!")
        rock_paper_scissors()

game_menu()