from cardhand import *

class Player:

    def __init__(self, hand = CardHand(), budget = 0):
        self.hand = hand
        self.budget = budget
    
    def get_hand(self):
        return self.hand
    
    def get_budget(self):
        return self.budget     
        
