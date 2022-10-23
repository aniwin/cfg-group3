from datetime import datetime

def midnight_reset():
    time_now = datetime.now()
    reset_time = (time_now.strftime("%H:%M"))
    if reset_time == "00:00":
        level = 0
        with open("daily_scores_weather_guess.csv", 'w+') as text_file:
            pass
        with open("daily_scores_rock_paper_scissors.csv", 'w+') as text_file:
            pass
        with open("daily_scores_feed_pet.csv", 'w+') as text_file:
            pass