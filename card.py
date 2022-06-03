import os, random
from window import *
from tkinter import *
from PIL import Image, ImageTk



SUITS = ["hearts", "diamonds", "spades", "clubs"]
VALUES = [str(i) for i in range(2, 11)] +["jack", "queen", "king", "ace"]
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
SUIT_SYMBOL = {"hearts" : HEARTS, "diamonds" : DIAMONDS, "spades" : SPADES, "clubs" : CLUBS}


class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
        
        path_name = value + "_" + "of" + "_" + suit + ".png"
        self.image_location = os.path.join("PNG-cards", path_name)

    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
    
    def get_numerical_value(self):
        if self.value.isdigit():
            return int(self.value)
        elif self.value in ["jack", "queen", "king"]:
            return 10
        else:
            return 1

    def get_image_location(self):
        return self.image_location

    def set_image_location(self, new_location):
        self.image_location = new_location

    def get_image(self):
        image = Image.open(self.image_location)
        image = image.resize((CARD_FRAME_WIDTH, CARD_FRAME_HEIGHT))
        image = ImageTk.PhotoImage(image)
        return image

    def __str__(self):
        if self.value != '10':
            str_rep = f' --- \n|{SUIT_SYMBOL[self.suit]}  |\n| {self.value} |\n|  {SUIT_SYMBOL[self.suit]}|\n --- '
        else:
            str_rep = f' --- \n|{SUIT_SYMBOL[self.suit]}  |\n|{self.value} |\n|  {SUIT_SYMBOL[self.suit]}|\n --- '
        return str_rep

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False
  
    def __lt__(self, other):
        return self.get_numerical_value() < other.get_numerical_value()

    def __gt__(self, other):
        return self.get_numerical_value() > other.get_numerical_value()

    def __le__(self, other):
        return self.get_numerical_value() <= other.get_numerical_value()

    def __ge__(self, other):
        return self.get_numerical_value() >= other.get_numerical_value()


if __name__ == '__main__':
    c = Card("5", "hearts")
    print(c)


