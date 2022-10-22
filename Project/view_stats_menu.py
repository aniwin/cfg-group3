import time
from home_page import *
from pet_object import *
def stats_menu():

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



    print(f"Let's check in with {(my_pet.get_name())} and see how they're doing!")
    time.sleep(2)
    print("""
                      _______  __   __  _______  ______    _______  ___      ___                          
                     |       ||  | |  ||       ||    _ |  |   _   ||   |    |   |                         
 ____   ____   ____  |   _   ||  |_|  ||    ___||   | ||  |  |_|  ||   |    |   |     ____   ____   ____  
|____| |____| |____| |  | |  ||       ||   |___ |   |_||_ |       ||   |    |   |    |____| |____| |____| 
                     |  |_|  ||       ||    ___||    __  ||       ||   |___ |   |___                      
                     |       | |     | |   |___ |   |  | ||   _   ||       ||       |                     
                     |_______|  |___|  |_______||___|  |_||__| |__||_______||_______|                    
                     """)
    with open("daily_scores_feed_pet.txt", 'r') as file:
        data = file.read()
        hunger = data.count("*")
    with open("daily_scores_rock_paper_scissors.txt", 'r') as file:
                data = file.read()
                happy = data.count("*")
    average = round((hunger+happy) / 2)

    if average in available_levels.keys():
        print(available_levels[average])


    with open("daily_scores_feed_pet.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("""
                      __   __  __   __  __    _  _______  _______  ______                        
                     |  | |  ||  | |  ||  |  | ||       ||       ||    _ |                       
 ____   ____   ____  |  |_|  ||  | |  ||   |_| ||    ___||    ___||   | ||   ____   ____   ____  
|____| |____| |____| |       ||  |_|  ||       ||   | __ |   |___ |   |_||_ |____| |____| |____| 
                     |       ||       ||  _    ||   ||  ||    ___||    __  |                     
                     |   _   ||       || | |   ||   |_| ||   |___ |   |  | |                     
                     |__| |__||_______||_|  |__||_______||_______||___|  |_|                     
            
            
            
            """)
            time.sleep(2)
            print(available_levels[(occurrences)])

    with open("daily_scores_rock_paper_scissors.txt", 'r') as file:
        data = file.read()
        occurrences = data.count("*")
        if occurrences in available_levels.keys():
            print("""
                      __   __  _______  _______  _______  ___   __    _  _______  _______  _______                      
                     |  | |  ||   _   ||       ||       ||   | |  |  | ||       ||       ||       |                     
 ____   ____   ____  |  |_|  ||  |_|  ||    _  ||    _  ||   | |   |_| ||    ___||  _____||  _____| ____   ____   ____  
|____| |____| |____| |       ||       ||   |_| ||   |_| ||   | |       ||   |___ | |_____ | |_____ |____| |____| |____| 
                     |       ||       ||    ___||    ___||   | |  _    ||    ___||_____  ||_____  |                     
                     |   _   ||   _   ||   |    |   |    |   | | | |   ||   |___  _____| | _____| |                     
                     |__| |__||__| |__||___|    |___|    |___| |_|  |__||_______||_______||_______|                      
            
            """)
            time.sleep(2)
            print(available_levels[(occurrences)])
            time.sleep(2)
    stats_menu_choice = input(f"""
                          1: View {my_pet.get_name()}'s current stats
                          2: Return to Main Menu


                          Please enter your choice: """)

    if stats_menu_choice == "1":
        print('This will reload the View Stats page')
        time.sleep(3)
        stats_menu()
    elif stats_menu_choice == "2":
        print('This will redirect to the Main Menu')
        time.sleep(3)
        main_menu()
    else:
        print('Unsure of your choice, you will be redirected to the Main Menu')
        time.sleep(3)
        main_menu()

if __name__ == "__main__":
    stats_menu()