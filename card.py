SUITS = ["hearts", "diamonds", "spades", "clubs"]
VALUES = [str(i) for i in range(2, 11)] +["jack", "queen", "king", "ace"]
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
SUIT_SYMBOL = {"hearts" : HEARTS, "diamonds" : DIAMONDS, "spades" : SPADES, "clubs" : CLUBS}
VALUE_SYMBOL = {"ace" : "A", "jack" : "J", "queen" : "Q", "king" : "K"}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.value == '10':
            str_rep = f' --- \n|{SUIT_SYMBOL[self.suit]}  |\n|{self.value} |\n|  {SUIT_SYMBOL[self.suit]}|\n --- '
        elif len(self.value) > 1:
            str_rep = f' --- \n|{SUIT_SYMBOL[self.suit]}  |\n| {VALUE_SYMBOL[self.value]} |\n|  {SUIT_SYMBOL[self.suit]}|\n --- '
        else:
            str_rep = f' --- \n|{SUIT_SYMBOL[self.suit]}  |\n| {self.value} |\n|  {SUIT_SYMBOL[self.suit]}|\n --- '
        return str_rep
    
    def get_numerical_value(self):
        if self.value.isdigit():
            return int(self.value)
        elif self.value in ["jack", "queen", "king"]:
            return 10
        else:
            return 1
    
    def get_value(self):
        return self.value
