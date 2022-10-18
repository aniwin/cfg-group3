from main_menu import *

def create_score_records():
    with open('daily_scores_rock_paper_scissors.txt', 'w') as file:
        pass
    with open('daily_scores_feed_pet.txt', 'w') as file:
        pass
create_score_records()
main_menu()

if __name__ == "__main__":
    create_score_records()

