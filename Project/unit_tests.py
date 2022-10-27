from unittest import TestCase
from food_menu import *
from character_menu import *
from home_page import *
from rock_paper_scissors_game import *
from rock_paper_scissors_menu import *
from sleep_function import *
from view_stats_menu import *
from weather_menu import *

# F E E D  P E T
# within feed_pet, user must enter number 1 - 10
class Test_Feed_Pet(TestCase):
    # if user enters nothing to feed pet
    def test_feed_pet_blank_input(self):
        with self.assertRaises(Exception):
            feed_pet("")

    # if user enters a number out of range with options 1 - 10 to feed pet
    def test_feed_pet_number_out_of_range(self):
        with self.assertRaises(Exception):
            feed_pet("11")

    # if user enters a letter when they should enter 1 - 10 to feed pet
    def test_feed_pet_text_input(self):
        with self.assertRaises(Exception):
            feed_pet("h")

    # if user enters a number and letter when they should enter 1 - 10 to feed pet
    def test_feed_pet_number_and_letter(self):
        with self.assertRaises(Exception):
            feed_pet("1b")

    # if user enters nothing to respond yes or no for replay
    def test_replay_blank_input(self):
        with self.assertRaises(Exception):
            replay("")

    # if user enters a number instead of y/n
    def test_replay_number_input(self):
        with self.assertRaises(Exception):
            replay("1")

# C H A R A C T E R  M E N U
# within character_menu user must give pet a name
class Test_Character_Name(TestCase):
    # if user enters blank name
    def test_character_name_blank_input(self):
        with self.assertRaises(Exception):
            character_name("")

    # if user enters nothing for choose/random
    def test_decide_gender_blank_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("")

    # if user enters number for when they should input choose/random
    def test_decide_gender_number_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("1")

    # if user enters invalid text when they should input choose/random
    def test_decide_gender_invalid_text_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("hello")

    # if user enters blank instead of y/n to confirm character name
    def test_confirm_name_blank(self):
        with self.assertRaises(Exception):
            confirm_name("")

    # if user enters number instead of y/n to confirm character name
    def test_confirm_name_number(self):
        with self.assertRaises(Exception):
            confirm_name("6")

    # Choose gender if user enters nothing when they should type male/female
    def test_choose_gender_nil(self):
        with self.assertRaises(Exception):
            choose_gender("")

    # Choose gender if user enters number when they should type male/female
    def test_choose_gender_number(self):
        with self.assertRaises(Exception):
            choose_gender("199")

    # Choose gender if user enters character when they should type male/female
    def test_choose_gender_character(self):
        with self.assertRaises(Exception):
            choose_gender("s")

# H O M E P A G E
# within home_page user must input 1 or 2 to end the game
class Test_Home_Page(TestCase):
    # if user enters blank when they need to answer 1/2
    def test_eng_game_blank_input(self):
        with self.assertRaises(Exception):
            end_game_final("")

    # if user enters number out of range when they need to answer 1/2
    def test_end_game_number_input_blank(self):
        with self.assertRaises(Exception):
            end_game_final("3")

    # if user enters character when they need to answer 1/2
    def test_end_game_character_input_char(self):
        with self.assertRaises(Exception):
            end_game_final("f")

    # user must enter a number from the main menu when pet is asleep
    # if user enters blank
    def test_main_menu_asleep_blank(self):
        with self.assertRaises(Exception):
            main_menu_asleep("")

    # if user enters number out of range
    def test_main_menu_asleep_number_out_of_range(self):
        with self.assertRaises(Exception):
            main_menu_asleep("44")

    # if user enters character
    def test_main_menu_asleep_character_input(self):
        with self.assertRaises(Exception):
            main_menu_asleep("h")

    # user must enter a number from the main menu when pet is awake
    # if user enters blank
    def test_main_menu_awake_blank_input(self):
        with self.assertRaises(Exception):
            main_menu_awake("")

    # if user enters number out of range
    def test_main_menu_awake_number_out_of_range(self):
        with self.assertRaises(Exception):
            main_menu_awake("44")

    # if user enters character
    def test_main_menu_awake_character(self):
        with self.assertRaises(Exception):
            main_menu_awake("h")

# V I E W  S T A T S
class Test_View_Stats_Menu(TestCase):
    # if user enters blank instead of 1 or 2
    def test_view_stats_inner_menu_blank(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("")

    # if user enters number out of range instead of 1 or 2
    def test_view_stats_inner_menu_number_out_of_range(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("4")

    # if user enters character instead of 1 or 2
    def test__view_stats_inner_menu_character(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("s")

# W E A T H E R  M E N U
class Test_Weather_Menu(TestCase):
    # if user enters blank instead of y/n
    def test_play_again_blank_input(self):
        with self.assertRaises(Exception):
            play_again("")

    # if user enters number instead of y/n
    def test_play_again_number_input(self):
        with self.assertRaises(Exception):
            play_again("11")

    # if user enters character other than y/n
    def test_play_again_character_input(self):
        with self.assertRaises(Exception):
            play_again("p")

    # if user enters a city that doesn't exist, just a letter
    def test_game_part_one_invalid_input_character(self):
        with self.assertRaises(Exception):
            game_part_one("p")

    # if user enters a number instead of a city
    def test_game_part_one_invalid_input_number(self):
        with self.assertRaises(Exception):
            game_part_one("77")

    # if user enters a city that doesn't exist, several characters
    def test_game_part_one_invalid_input_character_code_first_girls(self):
        with self.assertRaises(Exception):
            game_part_one("codefirstgirls")

    # if user enters a city that doesn't exist, several characters
    def test_game_part_two_invalid_input_character_code_first_girls_2(self):
        with self.assertRaises(Exception):
            game_part_two("codefirstgirls")

    # if user enters a city that doesn't exist, just a letter
    def test_game_part_two_invalid_input_character_2(self):
        with self.assertRaises(Exception):
            game_part_two("p")

    # if user enters a number instead of a city
    def test_game_part_two_invalid_input_number_2(self):
        with self.assertRaises(Exception):
            game_part_two("77")

# R O C K  P A P E R  S C I S S O R S  M E N U
# class Test_RPS_Menu(TestCase):
#     # if user enters blank instead of y/n
#     def test_blank_input_RPS(self):
#         with self.assertRaises(Exception):
#             rock_paper_scissors_menu("")

# R O C K  P A P E R  S C I S S O R S
class Test_RPS(TestCase):
    # if user enters blank instead of y/n
    def test_repeat_game_blank_input(self):
        with self.assertRaises(Exception):
            repeat_game("")

    # if user enters number instead of y/n
    def test_repeat_game_number_input(self):
        with self.assertRaises(Exception):
            repeat_game("456")

    # if user enters character other than y/n
    def test_repeat_game_character_input(self):
        with self.assertRaises(Exception):
            repeat_game("456")

    # if user enters blank for guessing rock paper scissors
    def test_user_guess_blank_input(self):
        with self.assertRaises(Exception):
            user_guess("")

    # if user enters character other than 'r' 'p' or 's'
    def test_user_guess_char_input(self):
        with self.assertRaises(Exception):
            user_guess("x")

    # if user enters number instead of 'r' 'p' or 's'
    def test_user_guess_number_input(self):
        with self.assertRaises(Exception):
            user_guess("115")

