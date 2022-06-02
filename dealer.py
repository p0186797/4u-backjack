from player import *

class Dealer(Player):
    def __init__(self, hand = CardHand()):
        self.hand = hand
    
    