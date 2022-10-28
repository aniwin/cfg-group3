# defining our Pet class, with it's attributes and methods
class Pet:
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

    def update_sleep(self, sleep):
        self.sleep = sleep

    def get_sleep(self):
        return self.sleep