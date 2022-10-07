import random

class Card:
    """A card to play hilo game. 
    A card can have a value from 1 to 13.

    Attributes:
        value(int): The number of possible values (1 - 13)
    """
    def __init__(self):
        self.individual_card = 0
        self.guessed = ""

    def random_card(self):
        self.individual_value = random.randint(1 , 14)
        