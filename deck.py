from cardhand import *
from random import *

class Deck(CardHand):
    def __init__(self):
        self.hand = []
        self.index = 0
        for suit in SUITS:
            for value in VALUES:
                self.hand.append(Card(value, suit))
    
    def shuffle(self):
        shuffle(self.hand)
    
    def pop(self):
        top = self.hand.pop()
        return top

    def deal(self, n, player_hand):
        for i in range(n):
            top = self.pop()
            player_hand.add_card(top)
        

if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    print("------")
    for i in range(3):
        print(d.pop())
    p = CardHand([])
    print(id(p.hand))
    d.deal(2, p)
    print("---")
    print(p)
    e = CardHand([])
    print(id(e.hand))
    print(len(e))
    d.deal(2, e)
    print("---")
    print(e)
    print(len(e))