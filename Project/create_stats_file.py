
from opening_menu import *
import time
def create_score_records():
    with open('daily_scores_rock_paper_scissors.csv', 'w') as file:
        pass
    with open('daily_scores_feed_pet.csv', 'w') as file:
        pass
    with open('daily_scores_weather_guess.csv', 'w') as file:
        pass
    opening_menu()


if __name__ == "__main__":
    create_score_records()

# PROBLEM - struggling to connect the file as part of the rolling program. Runs fine on its own, can we do this?
# it solves the incorrect looping of the program if we do it as its own save file.
