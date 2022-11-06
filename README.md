### Code First Girls Software 5 Group 3 Project

<img width="413" alt="Screenshot 2022-11-05 at 17 55 06" src="https://user-images.githubusercontent.com/106448997/200134285-af6d0b03-3b65-497f-895b-8df95942b4b6.png">




# **DUMPLING**

## Documentation
[Google Docs Project Documentation](https://docs.google.com/document/d/19PQTlbGiiLJDK4s6xPhei9JLyAA0_1XDn6I9dvttbDI/edit)


# **About The Project** 

### Game Overview

**Dumpling** is a command line virtual pet simulation game. Players of our game will create their own pet and will need to look after them by being able to feed, play and put their pet in sleep/awake modes. This can be done by following text instructions on the command line and inputting relevant values in order to progress in the game. Within the game we have also added features that allow the user to play mini-games with their virtual pet such as rock, paper, scissors, and getting weather advice from their pet with a mini-game feature of guessing a city in the world where it is currently snowing. Upon exiting the game the players scores can be saved into a MySQL database in order to save the game data to the leaderboard. If you want to play a new game then the game will be reset so that a new pet can be created. 

### Target Audiences

**Dumpling** is a fun game and pastime for both adults and children. The main objective of our game is for users to be 
able to raise their virtual pet to the maximum level of happiness and contentment throughout each day. Daily scores for 
games are reset at midnight every day, encouraging the user to keep playing in order to keep their pet happy and 
content.

# Running the Game

### Requirements 

1. Clone the repo.

2. Set up a MySQL database, you can find the .sql file required for this as part of the project directory entitled **sql_pet_database.sql**. 

3. **Dumpling** has a few requirements in order to play the game. These can be found in the **requirements.txt**. Upon
running main.py these requirements will automatically be installed, or alternatively the user can install the manually 
with the following commands:

**pip install requests**

**pip install mysql_connector_python**

4. To run the game, open **main.py** which can be found in the project directory and run the file to start the game. 

5. You will be prompted to enter you **MySQL credentials** in order to allow the game to connect to your local MySQL database and update the leaderboard with your gave scores. This data is saved in a file entitled **config.py**. If you need to alter your credentials before saving your scores to the database then you can override the login information in this file. 

6. When ending the game, your scores will be saved in a .csv file entitled **daily_scores.csv**. If you would like to insert these scores into the Dumpling database then you will need to run the **mysql_save_file.py** which can be located in the project directory. If your SQL credentials are correct and the database exists then your scores will be inserted to the leaderboard via the mysql-connector-python module. 

7. Upon running a new game from **main.py**, your scores will be reset and a new Dumpling pet can be created for more Dumpling game fun!

## Planning Stage

### Tools & Skills required

We will use python to assimilate the logic of our game, including our knowledge of how to effectively use and API.
SQL knowledge will be needed for our back end database which will store name, gender and scores.



### User Stories

```
Story Identifier 001
As a 
User

I need 
To run one main file in order to play the game

So that
I don't have to worry about other dependancies and requirements the game may have in order for me to play

```

```
Story Identifier 002
As a 
User

I need 
To have a simple menu interface

So that
I can interact easily with my pet

```

```
Story Identifier 003
As a 
User

I need 
To be able to view my pet's current happiness and hunger levels

So that
I can interact with my pet and improve these levels to achieve full happiness.

```

```
Story Identifier 004
As a 
User

I need 
Exit the game

So that
when I have finished playing, I can end my session.

```

```
Story Identifier 005
As a 
User

I need 
to be able to exit out of menus to the previous menu/back to the main menu

So that
my game play can run smoothly and if I enter into a menu by accident I can return to the previous screen.

```

### Diagram of user interaction

![img.png](img.png)


## The Team

### People responsible for creation and maintenance of the project and their github usernames

**Anisah** aniwin

**Beth** ejmillard

**Claire** clairelev

**Hani** hanidore

**Julie** juliethomas82
