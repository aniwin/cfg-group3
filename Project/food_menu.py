
### to run this file type this into your terminal: pip install requests
import time

from pet_object import *
from available_levels import *
from retrieve_daily_scores import *

from datetime import datetime
import os

foods_i_like = {
    1: "Chicken 🍗",
    2: "Chocolate 🍫",
    3: "Casserole 🍲",
    4: "Pickled egg 🥚",
    5: "Kiwi 🥝"
}
foods_i_dislike = {
    6: "Hotdog 🌭",
    7: "Cheese 🧀",
    8: "Pizza 🍕",
    9: "Salad 🥗",
    10: "Custard 🍮"
}


def feed_pet(return_to_main):
    available_levels

    get_daily_hunger_score()

    def replay():
        try:
            play_again = input(str("""Play again? y/n: """)).lower()
            if play_again == "y":
                feed_pet(return_to_main)
            elif play_again == "n":
                return_to_main()
            else:
                raise Exception()
        except:
            print("""Invalid input!""")
            replay()

    print(f"""
    {my_pet.get_name()} has these foods available.
    Try and choose something {my_pet.get_name()} will like!: 
    """)
    def merge(foods_i_like, foods_i_dislike):
        list_all_foods = {**foods_i_like, **foods_i_dislike}
        return list_all_foods

    # all_foods = merge(foods_i_like, foods_i_dislike)
    # print(all_foods)
    # chosen_food = input("""What do you want to feed me? Input number 1 - 10: """)
    # chosen_food_int = int(chosen_food)

    all_foods = merge(foods_i_like, foods_i_dislike)
    print(all_foods)
    while True:
        try:
            chosen_food = input("What do you want to feed me? Input number 1 - 10: ")
            chosen_food_int = int(chosen_food)
        except ValueError:
            print("Oops! That wasn't a valid number. Try again.")
        else:
            if 1 <= chosen_food_int <= 10:
                break
            else:
                print("Number out of range. Please try again")

    if chosen_food_int in foods_i_like.keys():
        print(f"""YUM YUM!...I like {(foods_i_like[chosen_food_int])}""")
        with open("daily_scores_feed_pet.csv", 'r+') as file:
            data = file.read()
            occurrences = data.count("*")
            if occurrences < 10:
                with open("daily_scores_feed_pet.csv", 'a+') as text_file:
                    text_file.write("*")
            elif occurrences == 10:
                print("""You overfed me and I was sick! 🤢""")
                with open("daily_scores_feed_pet.csv", 'rb+') as delete_score:
                    delete_score.seek(-5, os.SEEK_END)
                    delete_score.truncate()

    elif chosen_food_int in foods_i_dislike.keys():
        print(f"""YUCK!...I hate {(foods_i_dislike[chosen_food_int])}""")
        with open("daily_scores_feed_pet.csv", 'r+') as file:
            data = file.read()
            occurrences = data.count("*")
            if occurrences >= 1:
                with open("daily_scores_feed_pet.csv", 'rb+') as delete_score:
                    delete_score.seek(-1, os.SEEK_END)
                    delete_score.truncate()
            elif occurrences == 0:
                print("""You fed me a food I don't like!""")

    get_daily_hunger_score()
    replay()
