from datetime import datetime

def midnight_reset():
    with open("date.csv", 'r') as text_file:
        data = text_file.read()
        # read the line in the file
        # if it is not equal to today's date then reset the file
        now = datetime.now()
        today = now.strftime("%B %d, %Y")
        if data != today:
            with open("date.csv", 'w+') as text_file:
                text_file.write(today)
            with open("daily_scores_weather_guess.csv", 'w+') as text_file:
                pass
            with open("daily_scores_rock_paper_scissors.csv", 'w+') as text_file:
                pass
            with open("daily_scores_feed_pet.csv", 'w+') as text_file:
                pass
            with open("daily_scores.csv", 'w+') as text_file:
                pass
