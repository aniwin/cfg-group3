
### to run this file type this into your terminal: pip install requests
import time

from home_page import *
from pet_object import *


from datetime import datetime
import os

def feed_pet():
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

    time_now = datetime.now()
    reset_time = (time_now.strftime("%H:%M"))
    if reset_time == "00:00":
        level = 0
        with open("daily_scores_feed_pet.txt", 'w+') as text_file:
            pass

    with open("daily_scores_feed_pet.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("""
                    ----H U N G E R----""")
            time.sleep(2)
            print(available_levels[(occurrences)])

    print(f"""
                    {my_pet.get_name()}has these foods available.
                    Try and choose something {my_pet.get_name()} will like!: """)
    def merge(foods_i_like, foods_i_dislike):
        list_all_foods = {**foods_i_like, **foods_i_dislike}
        return list_all_foods

    all_foods = merge(foods_i_like, foods_i_dislike)
    print(all_foods)
    chosen_food = input("""
                    What do you want to feed me? Input number 1 - 10: """)
    chosen_food_int = int(chosen_food)

    if chosen_food_int in foods_i_like.keys():
        print(f"""
                    YUM YUM!...I like {(foods_i_like[chosen_food_int])}""")
        with open("daily_scores_feed_pet.txt", 'r+') as file:
            data = file.read()
            occurrences = data.count("*")
            if occurrences < 10:
                with open("daily_scores_feed_pet.txt", 'a+') as text_file:
                    text_file.write("*")
            elif occurrences == 10:
                print("""
                    You overfed me and I was sick! 🤢""")
                with open("daily_scores_feed_pet.txt", 'rb+') as delete_score:
                    delete_score.seek(-5, os.SEEK_END)
                    delete_score.truncate()

    elif chosen_food_int in foods_i_dislike.keys():
        print(f"""
                    YUCK!...I hate {(foods_i_dislike[chosen_food_int])}""")
        with open("daily_scores_feed_pet.txt", 'r+') as file:
            data = file.read()
            occurrences = data.count("*")
            if occurrences >= 1:
                with open("daily_scores_feed_pet.txt", 'rb+') as delete_score:
                    delete_score.seek(-1, os.SEEK_END)
                    delete_score.truncate()
            elif occurrences == 0:
                print("""
                    You fed me a food I don't like!""")

    with open("daily_scores_feed_pet.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("""
                    ----H U N G E R----""")
            print(available_levels[(occurrences)])

    play_again = input(str("""
                    Play again? y/n: """)).lower()

    if play_again == "y":
        feed_pet()
    elif play_again == "n":
        main_menu()
    else:
        print("""
                    Invalid input!""")


if __name__ == "__main__":
    feed_pet()