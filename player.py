from cardhand import *

class Player:
    def __init__(self, hand = CardHand([]), bet = 0):
        self.hand = hand
        self.bet = bet

if __name__ == '__main__':
    l = [Card("2","spades"), Card("ace", "hearts")]
    c = CardHand(l)
    p = Player()
    list_of_cards = p.hand.hand
    for card in list_of_cards:
        print(card.value, card.suit)