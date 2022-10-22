from game_menu import *
from main_menu import *
from datetime import datetime
import requests

def weather_advisor(): # depending on the weather code returned for a certain city the pet will give advice
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

    weather_dict = {
        1: "Hide under the bed 🌩️", # Thunderstorms
        2: "Wear raincoat 🌧️", # drizzle
        3: "Wear raincoat 🌧️ & Take umbrella! ☔", # rain
        4: "Build a snowman! ⛄", # snow
        5: "Strange weather! Stay indoors! 🌪️", # mist, smoke, haze, dust, fog, sand, ash, squall, tornado
        6: "Enjoy the clear skies! 🌞", # clear
        7: "Cloudy with a chance of meatballs ☁!" # clouds
        }

    time_now = datetime.now()
    reset_time = (time_now.strftime("%H:%M"))
    if reset_time == "00:00":
        level = 0
        with open("daily_scores_weather_guess.txt", 'w+') as text_file:
            pass

    with open("daily_scores_feed_pet.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("❄F I N D-S N O W❄")
            print(available_levels[(occurrences)])

    apiKey = "1969ff8fbf12db1aa43981ac976e2c9b" # api key for openweatherapi

    baseURL = "https://api.openweathermap.org/data/2.5/weather?q=" # base URL for endpoint

    print("I can help you with the weather!")
    cityName = input("Tell me what city are you in?: ")

    completeURL = baseURL + cityName + "&appid=" + apiKey # forms full URL based on user input

    response = requests.get(completeURL) # response from endpoint
    x = response.json()

    if x["cod"] != "404":
        z = x["weather"]
        weather_code = int(z[0]["id"]) # this saves the weather_code returned from the api to variable weather_code
        weather_description = z[0]["description"] # the saves the weather description as returned from api
        print(f"Right now you have...{weather_description}")

        # these lines of code take the weather_code returned by the api and return advice based on the code from the
        # dictionary defined above.
        if weather_code >= 801:
            print(f"My advice is...{(weather_dict[7])}")
        elif weather_code == 800:
            print(f"My advice is...{(weather_dict[6])}")
        elif weather_code >= 701 and weather_code <= 781: # 701 or 711 or 721 or 731 or 741 or 751 or 761 or 762 or 771 or 781
            print(f"My advice is...{(weather_dict[5])}")
        elif weather_code >= 600 and weather_code <= 622: # 600 or 601 or 602 or 611 or 612 or 613 or 615 or 616 or 620 or 621 or 622
            print(f"My advice is...{(weather_dict[4])}")
        elif weather_code == 500:
            print(f"My advice is...{(weather_dict[3])}")
        elif weather_code >= 300 and weather_code <= 321: # 300 or 301 or 302 or 310 or 311 or 312 or 313 or 314 or 321
            print(f"My advice is...{(weather_dict[2])}")
        elif weather_code >=200 and weather_code <= 232: # 200 or 201 or 202 or 210 or 211 or 212 or 221 or 230 or 231 or 232
            print(f"My advice is...{(weather_dict[1])}")
        else:
            print(f"I don't have any advice for today!")
    else:
        print("City Not Found")
        weather_advisor()

    with open("daily_scores_weather_guess.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")

    if occurrences == 10:
        print("You have already guessed where it is snowing today! Guess again tomorrow!")
    else:
        guess_city_snowing = input("If you can tell me a city that has snow (my favourite weather) I'll give you full "
                                   "finding snow happiness: ")

        completeURL = baseURL + guess_city_snowing + "&appid=" + apiKey # forms full URL based on user input

        response = requests.get(completeURL) # response from endpoint
        x = response.json()

        if x["cod"] != "404":
            z = x["weather"]
            weather_code_for_guess = int(z[0]["id"]) # this saves the weather_code returned from the api to variable weather_code

            if weather_code_for_guess >= 600 and weather_code_for_guess <= 622: # 600 or 601 or 602 or 611 or 612 or 613 or 615 or 616 or 620 or 621 or 622
                print(f"You guessed correctly! It is snowing in {guess_city_snowing} ⛄") # snow

                with open("daily_scores_weather_guess.txt", 'a+') as text_file:
                    text_file.write("**********")

                with open("daily_scores_weather_guess.txt", 'r') as file:
                    data = file.read()
                    occurrences = data.count("*")
                    if occurrences in available_levels.keys():
                        print("❄F I N D-S N O W❄")
                        print(available_levels[(occurrences)])
            else:
                print(f"You guessed wrong! 😥 It's not snowing in {guess_city_snowing}")
        else:
            print("City Not Found")

    replay = input(str("Play again? y/n: ")).lower()
    if replay == "y":
        weather_advisor()
    elif replay == "n":
         menu_games()
    else:
        print("invalid input! You will be redirected to the Games Menu")
        menu_games()



if __name__ == "__main__":
    weather_advisor()