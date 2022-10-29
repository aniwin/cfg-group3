# IMPORTANT!
# need to run pip install maskpass otherwise won't work!
# also for some reason this only works if you run python sql_username_password.py

import maskpass

localhost_confirmed = []
username_confirmed = []
password_confirmed = []

def get_local_host():

    def confirm_local_host():
        try:
            confirm = input(str(f"You are saving your localhost as {localhost}? y/n: ")).lower()
            if confirm == "y":
                localhost_confirmed.append(localhost)
                print(f"Your localhost has been saved as {localhost}")
            elif confirm == "n":
                get_local_host()
            else:
                raise Exception()
        except:
            print("Invalid input!")
            confirm_local_host()

    localhost = input("Enter your localhost: ")
    if localhost == "":
        print("You need to input your localhost!")
        get_local_host()
    else:
        confirm_local_host()

def get_username():

    def confirm_username():
        try:
            confirm = input(str(f"You are saving your localhost username as {username}? y/n: "))
            if confirm == "y":
                username_confirmed.append(username)
                print(f"Your localhost username has been saved as {username}")
            elif confirm == "n":
                get_username()
            else:
                raise Exception()
        except:
            print("Invalid input!")
            confirm_username()

    username = input("Enter your localhost username: ")
    if username == "":
        print("You need to input your localhost username!")
        get_username()
    else:
        confirm_username()

def get_password_for_localhost(): # needs a redirect

    def confirm_password():
        password_retype = maskpass.askpass(prompt="Re-type your localhost password: ", mask="*")
        if password_retype == password:

            with open('config.py', 'w+') as file:
                file.writelines(f'HOST = "{(localhost_confirmed[0])}"\n')
                file.writelines(f'USER = "{(username_confirmed[0])}"\n')
                # file.writelines(f'PASSWORD = "{(password_confirmed[0])}"\n')

            print("Success your credentials have been saved!") # redirect to....
        else:
            print("Passwords don't match")
            get_password_for_localhost()

    password = maskpass.askpass(prompt="Enter your localhost password: ", mask="*")
    if password == "":
        print("You need to input your localhost password!")
        get_password_for_localhost()
    else:
        confirm_password()

def sql_credentials():
    print("Please enter your SQL credentials")
    get_local_host()
    get_username()
    get_password_for_localhost()
    print(localhost_confirmed)
    print(username_confirmed)
    print(password_confirmed)


sql_credentials()