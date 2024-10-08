import time
from available_levels import *
from pet_object import *
from available_levels import *
from ascii_text import *
from home_page import *

def stats_menu(redirect_to_home):
    available_levels

    def stats_inner_menu():
        try:
            stats_menu_choice = input(f"""
                    1: View {my_pet.get_name()}'s current stats
                    2: Return to Main Menu


            Please enter your choice: """)

            if stats_menu_choice == "1":
                print('This will reload the View Stats page')
                time.sleep(3)
                stats_menu(redirect_to_home)
            elif stats_menu_choice == "2":
                print('This will redirect to the Main Menu')
                time.sleep(3)
                redirect_to_home()
            else:
                raise Exception()
        except:
            print('Choose 1 or 2!')
            stats_inner_menu()

    print(f"Let's check in with {(my_pet.get_name())} and see how they're doing!")
    time.sleep(2)
    overall_ascii()

    # calculate the average from feed pet, rock paper scissors, and weather guess scores to give an overall
    with open("daily_scores_feed_pet.csv", 'r') as file:
        data = file.read()
        hunger = data.count("*")
    with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
        data = file.read()
        happy = data.count("*")
    with open("daily_scores_weather_guess.csv", 'r') as file:
        data = file.read()
        find_snow = data.count("*")
    average = round((hunger+happy+find_snow) / 3)

    if average in available_levels.keys():
        print(available_levels[average])

    with open("daily_scores_feed_pet.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            hunger_ascii()
            time.sleep(2)
            print(available_levels[(occurrences)])

    with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            happiness_ascii()
            time.sleep(2)
            print(available_levels[(occurrences)])
            time.sleep(2)



    with open("daily_scores_weather_guess.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            find_snow_ascii()
            time.sleep(2)
            print(available_levels[(occurrences)])
            time.sleep(2)

    stats_inner_menu()
