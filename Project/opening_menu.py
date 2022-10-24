import time
from character_menu import *
from ascii_art import *
def opening_menu():
    print('Loading...')
    time.sleep(2)
    print('Ready to play!')
    time.sleep(1.5)
    welcome_to()
    time.sleep(3)
    name_of_game()
    time.sleep(2)
    group_name()
    time.sleep(3)

    print('''
                     .        .   .          .---.     ,_ .                      ,---     ,---.                    ,--. 
     ,-. ,-. ,-. ,-. |- ,-. ,-|   |-. . .    \___  ,-. |_ |- . , , ,-. ,-. ,-.   |__      |  -'  ,-. ,-. . . ,-.    __| 
     |   |   |-' ,-| |  |-' | |   | | | |        \ | | |  |  |/|/  ,-| |   |-'      \     |  ,-' |   | | | | | |      | 
     `-' '   `-' `-^ `' `-' `-'   `-' `-|    `---' `-' |  `' ' '   `-^ '   `-'   `--'     `---|  '   `-' `-' |-'   `--' 
                                       /|              '                                   ,-.|              |          
                                      `-'                                                  `-+'              '          
    ''')
    time.sleep(3)
    print('Lets start by creating a character...')
    time.sleep(3)
    character_name()

if __name__ == "__main__":
    opening_menu()
