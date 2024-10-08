import csv
from pet_object import *
import os
import sys

def closing_scores():

    with open("daily_scores_weather_guess.csv", 'r') as file:
        data = file.read()
        occurrences_weather = int(data.count("*"))

    with open("daily_scores_feed_pet.csv", 'r') as file:
        data = file.read()
        occurrences_feed_pet = int(data.count("*"))

    with open("daily_scores_rock_paper_scissors.csv", 'r') as file:
        data = file.read()
        occurrences_rock_paper_scissors = int(data.count("*"))

    data = [(occurrences_weather),(occurrences_feed_pet),(occurrences_rock_paper_scissors)]
    with open("daily_scores.csv", "w+") as file:
        writer = csv.writer(file)
        writer.writerow(data)

    return thanks_for_playing()
def exit_final():
    print(f"Thanks for playing with {(my_pet.get_name())}")
    os._exit(0)

def thanks_for_playing():
    return exit_final()
