from available_levels import *

# open all the score CSV files and retrieve the current score
def get_daily_weather_score():
    with open("daily_scores_weather_guess.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("❄F I N D-S N O W❄")
            print(available_levels[(occurrences)])

def get_daily_rock_paper_scissors_score():
    with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("-H A P P I N E S S-")
            print(available_levels[(occurrences)])

def get_daily_hunger_score():
    with open("daily_scores_feed_pet.csv", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("""----H U N G E R----""")
            print(available_levels[(occurrences)])
