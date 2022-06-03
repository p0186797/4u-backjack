from player import *
from random import *

class Dealer(Player):

    # In most casino blackjack games, a dealer must take a card if he hits 16 or below 
    # and stand at 17 or above.
    def play(self):
        if self.hand.total() <= 16:
            return "hit"
        else:
            return choice(["stand", "hit"])
