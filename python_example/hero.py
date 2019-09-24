
class Hero():
    # Class to create Hero
    def __init__(self, name, level, race):
        # Initial Hero
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    
    def show_hero(self):
        # Print parameters Hero
        discription = (self.name + " level is " + str(self.level) + ", race is " + self.race + ", health is " + str(self.health))
        print(discription)

    def level_up(self):
        # Upgrade level Hero
        self.level += 1

    def move(self):
        # Hero moving
        print("Hero " + self.name + " start moving ...")

    def set_health(self, new_healt):
        self.health = new_healt

# -------------------------------------------------------------------------
class SuperHero(Hero):
    # Class to create SuperHero
    def __init__(self, name, level, race, magiclevel):
        # Initial SuperHero
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        # Use magic
        self.magic -= 10

    def show_hero(self):
        # Print parameters Hero
        discription = (self.name + " level is " + str(self.level) + ", race is " + self.race + ", health is " + str(self.health) + ", magiclevel is " + str(self.magiclevel) + ", magic is " + str(self.magic))
        print(discription)