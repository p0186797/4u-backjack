from card import *

class CardHand:
    def __init__(self, list_of_cards = []):
        self.hand = list_of_cards
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self): 
        if self.index < len(self.hand):
            self.next_card = self.hand[self.index]
            self.index += 1
            return self.next_card
        raise StopIteration
    
    def __len__(self):
        return len(self.hand)
    
    def __getitem__(self, i):
        return self.hand[i]
        
    def __str__(self):
        str_rep = ""
        for card in self:
            str_rep += card.__str__() + " "
        return str_rep

    def get_hand(self):
        return self.hand
    
    def add_to_hand(self, card):
        self.hand.append(card)

    def total(self):
        sum = 0
        aces = []
        for card in self.hand:
            if card.get_value() == "ace":
                aces.append(card)
            sum += card.get_numerical_value()
        for ace in aces:
            while sum + 10 <= 21:
                sum += 10
        return sum

if __name__ == '__main__':
    hand = [Card("2", "hearts"), Card("5", "clubs"), Card("ace", "spades"), Card("ace", "clubs")]
    c = CardHand(hand)
    print(c)
    for card in c:
        print(c.index)
        print(card)
    print(c[0])
