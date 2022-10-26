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
class Test_Feed_Pet_Input(TestCase):
    # if user enters nothing
    def test_blank_input(self):
        with self.assertRaises(Exception):
            feed_pet("")

    # if user enters a number out of range
    def test_number_out_of_range(self):
        with self.assertRaises(Exception):
            feed_pet("11")

    # if user enters a letter
    def test_text_input(self):
        with self.assertRaises(Exception):
            feed_pet("h")

    # if user enters a number and letter
    def test_number_and_letter(self):
        with self.assertRaises(Exception):
            feed_pet("1b")

    # if user enters nothing to respond yes or no
    def test_blank_input_yes_or_no(self):
        with self.assertRaises(Exception):
            replay("")

    # if user enters a number instead of y/n
    def test_number_input(self):
        with self.assertRaises(Exception):
            replay("1")

# C H A R A C T E R  M E N U
# within character_menu user must give pet a name
class Test_Character_Name(TestCase):
    # if user enters blank name
    def test_blank_input(self):
        with self.assertRaises(Exception):
            character_name("")

    # if user enters nothing for choose/random
    def test_blank_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("")

    # if user enters nothing for number
    def test_number_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("1")

    # if user enters invalid text for number
    def test_invalid_text_choose_or_random(self):
        with self.assertRaises(Exception):
            decide_gender("hello")

    # if user enters blank instead of y/n to confirm character name
    def test_blank_confirm_name(self):
        with self.assertRaises(Exception):
            confirm_name("")

    # if user enters number instead of y/n to confirm character name
    def test_number_confirm_name(self):
        with self.assertRaises(Exception):
            confirm_name("6")

# H O M E P A G E
# within home_page user must input 1 or 2 to end the game
class Test_End_Game(TestCase):
    # if user enters blank
    def test_blank_input(self):
        with self.assertRaises(Exception):
            end_game_final("")

    # if user enters number out of range
    def test_number_input(self):
        with self.assertRaises(Exception):
            end_game_final("3")

    # if user enters character
    def test_character_input(self):
        with self.assertRaises(Exception):
            end_game_final("f")

    # user must enter a number from the main menu when pet is asleep
    # if user enters blank
    def test_blank_input_main(self):
        with self.assertRaises(Exception):
            main_menu_asleep("")

    # if user enters number out of range
    def test_number_out_of_range_input_main(self):
        with self.assertRaises(Exception):
            main_menu_asleep("44")

    # if user enters character
    def test_character_input_main(self):
        with self.assertRaises(Exception):
            main_menu_asleep("h")

    # user must enter a number from the main menu when pet is awake
    # if user enters blank
    def test_blank_input_main_awake(self):
        with self.assertRaises(Exception):
            main_menu_awake("")

    # if user enters number out of range
    def test_number_out_of_range_input_main_awake(self):
        with self.assertRaises(Exception):
            main_menu_awake("44")

    # if user enters character
    def test_character_input_main_awake(self):
        with self.assertRaises(Exception):
            main_menu_awake("h")

# V I E W  S T A T S
class Test_View_Stats_Menu(TestCase):
    # if user enters blank instead of 1 or 2
    def test_blank_input_inner_menu(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("")

    # if user enters number out of range instead of 1 or 2
    def test_number_out_of_range_input_inner_menu(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("4")

    # if user enters character instead of 1 or 2
    def test_character_input_inner_menu(self):
        with self.assertRaises(Exception):
            view_stats_inner_menu("s")

# W E A T H E R  M E N U
class Test_Weather_Menu(TestCase):
    # if user enters blank instead of y/n
    def test_blank_input_play_again(self):
        with self.assertRaises(Exception):
            play_again("")

    # if user enters number instead of y/n
    def test_number_input_play_again(self):
        with self.assertRaises(Exception):
            play_again("11")

    # if user enters character other than y/n
    def test_character_input_play_again(self):
        with self.assertRaises(Exception):
            play_again("p")