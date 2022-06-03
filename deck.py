from card import *
from cardhand import CardHand

class Deck(CardHand):
    def __init__(self):
        self.hand = []
        for suit in SUITS:
            for value in VALUES:
                c = Card(value, suit)
                self.hand.append(c)
    
    def get_deck(self):
        return self.hand

    def shuffle(self):
        random.shuffle(self.hand)

    def draw_card(self):
        top_card = self.hand.pop()
        return top_card

    def draw_cards(self, hand, n):
        for i in range(n):
            hand.add_to_hand(self.hand.pop())
    
    def __str__(self):
        d = ""
        for card in self:
            d += Card.__str__(card) + ","
        return d
            
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(deck)

    for card in deck:
        print(card)

    print("----")
    hand = []
    second_hand = []
    for i in range(5):
        hand.append(deck.draw_card())
    for card in hand:
        print(card)
    print("--------------")
    for j in range(6):
        second_hand.append(deck.draw_card())
    for card in second_hand:
        print(card)
    print("--------------------")
    for card in deck.get_deck():
        print(card)
