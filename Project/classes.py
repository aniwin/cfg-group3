# we need:
#
# name
# gender
# happiness level =
# hunger level
# find snow level

class Pet():
    def __init__(self, name, gender, sleep):
        self.name = name
        self.gender = gender
        self.sleep = sleep

    def update_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def update_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender

    def is_asleep(self):
        self.sleep = True

    def is_not_asleep(self):
        self.sleep = False

# functions to update int values for happiness and hunger
# understand how to return a True value for find snow
# working sleep function to return True

        # self.happiness = 0
        # self.hunger = 0
        # self.findsnow = False
