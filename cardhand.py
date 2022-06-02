from card import *

class CardHand:
    '''A class to represent a hand of Cards.'''
    
    def __init__(self, list_of_cards):

        self.hand = list_of_cards
        self.index = 0

    def __str__(self):
        str_rep = ""
        for card in self:
            str_rep += card.__str__() + "\n"
        return str_rep
            
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.hand):
            self.next_card = self.hand[self.index]
            self.index += 1
            return self.next_card
        raise StopIteration
    
    def __getitem__(self, i):
        return self.hand[i]

    def __len__(self):
        return len(self.hand)
    
    def __eq__(self, other):
        return self.total() == other.total() 

    def __lt__(self, other):
        return self.total() < other.total() 
    
    def __gt__(self, other):
        return self.total() > other.total() 
        
    def total(self):
        s = 0
        aces = 0
        for card in self:
            s += card.get_numerical_value()
            if card.get_value() == 'ace':
                aces += 1

        while s + 10 <= 21 and aces > 0:
            s += 10
            aces -= 1
        return s
    
    def add_card(self, card):
        self.hand.append(card)


if __name__ == '__main__':
    l = [Card("2","spades"), Card("king", "hearts"), Card("ace", "spades"), Card("ace", "clubs")]
    c = CardHand(l)
    d = CardHand([Card("jack", "hearts"), Card("ace", "spades"), Card("king", "hearsts"), Card("jack", "diamonds")])
    e = CardHand([])
    for i in range(len(c)):
        print(c[i])
        e.add_card(c[i])
    print(c.total())
    print(d.total())
    print(e.total())
    print(d < e)
   