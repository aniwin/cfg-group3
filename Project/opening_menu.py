import time
from character_menu import *
def opening_menu():
    print('loading...')
    time.sleep(2)
    print('ready to play!')
    time.sleep(1.5)
    print(
        '''
        ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗ 
        ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗
        ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║
        ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║
        ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝
         ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ 
        ''')
    time.sleep(2)
    print(
        '''
        ███╗   ██╗ █████╗ ███╗   ███╗███████╗     ██████╗ ███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
        ████╗  ██║██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
        ██╔██╗ ██║███████║██╔████╔██║█████╗      ██║   ██║█████╗      ██║  ███╗███████║██╔████╔██║█████╗  
        ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
        ██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝██║         ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
        ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝ ╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        ''')
    print(
        '''
                        .        .   .          .---.     ,_ .                      ,---     ,---.                    ,--. 
        ,-. ,-. ,-. ,-. |- ,-. ,-|   |-. . .    \___  ,-. |_ |- . , , ,-. ,-. ,-.   |__      |  -'  ,-. ,-. . . ,-.    __| 
        |   |   |-' ,-| |  |-' | |   | | | |        \ | | |  |  |/|/  ,-| |   |-'      \     |  ,-' |   | | | | | |      | 
        `-' '   `-' `-^ `' `-' `-'   `-' `-|    `---' `-' |  `' ' '   `-^ '   `-'   `--'     `---|  '   `-' `-' |-'   `--' 
                                          /|              '                                   ,-.|              |          
                                         `-'                                                  `-+'              '          
        '''
    )
    time.sleep(2)
    print('lets start by creating a character.')
    print(input('please enter any key to proceed:'))
    character_menu()

if __name__ == "__main__":
    opening_menu()
