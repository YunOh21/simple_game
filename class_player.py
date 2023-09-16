import random


class Player:
    def __init__(self, name):
        self.__idx = 0
        self.__order = None
        self.__name = name


    @property
    def order(self):
        return self.__order
    

    @order.setter
    def order(self, n):
        self.__order = n


    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def icon(self):
        return None  # placeholder

    
    @property
    def idx(self):
        return self.__idx
    

    @idx.setter
    def idx(self, n):
        self.__idx = n


    def show_you(self):
        print("\n")
        print("Let's get started!")
        print("This is you: " + self.icon)
        print("This is where you are now: " + str(self.idx))


    def show_enemy(self):
        print("\n")
        print("FYI, this is your enemy: " + self.icon)
        print("This is where the enemy is now: " + str(self.idx))


    def roll_the_dice(self):
        dice_number = random.randrange(1, 7)
        print("The dice number of " + self.name + ": " + str(dice_number))

        return dice_number


    def move(self, n):
        self.__idx += n


class WhitePlayer(Player):
    def __init__(self, name):
        super().__init__(name)


    @property
    def icon(self):
        return '○'


class BlackPlayer(Player):
    def __init__(self, name):
        super().__init__(name)


    @property
    def icon(self):
        return '●'