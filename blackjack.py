from tkinter import *
from deck import *
from player import *
from dealer import *
from card import *
from cardhand import *
from menu_window import *
from window import *
from PIL import Image, ImageTk
from tkinter import font

class BlackJack:

    def __init__(self, bet, budget):
        self.budget = budget
        self.bet = bet
        self.deck = Deck()
        self.deck.shuffle()
        self.window = Window()
        self.winner = ""
        self.deal()
        self.setting_up_buttons()
        self.setting_up_labels()
    
    def set_winner(self):
        player_total = self.player.get_hand().total()
        dealer_total = self.dealer.get_hand().total()

        if player_total > 21 and dealer_total <= 21:
            self.winner = self.dealer
        elif dealer_total > 21 and player_total <= 21:
            self.winner = self.player
        elif player_total < dealer_total <= 21:
            self.winner = self.dealer
        elif dealer_total < player_total <= 21:
            self.winner = self.player
        else:
            self.winner = "Tie"
        
        
    def deal(self):
        deck = self.deck
        player_hand = []
        dealer_hand = []
        for hand in [player_hand, dealer_hand]:
            for i in range(2):
                hand.append(deck.draw_card())
        self.player = Player(CardHand(player_hand), self.budget)
        self.dealer = Dealer(CardHand(dealer_hand))

    def add(self):
        card = self.deck.draw_card()
        i = len(self.player.get_hand())
        self.player.get_hand().add_to_hand(card)
        image = card.get_image()

        label = self.window.get_player_card_labels()[i]
        label['image'] = image
        label.image = image

        self.window.get_player_total_label()['text'] = self.player.get_hand().total() 
        if self.player.get_hand().total() >= 21:
            self.deactivate_buttons()
            self.revealing_first_card()
            self.set_winner()
            self.declare_winner()
            

    def revealing_first_card(self):
        first_card_label = self.window.get_dealer_card_labels()[0]
        first_card = self.dealer.get_hand()[0]
        image = first_card.get_image()
        first_card_label['image'] = image 
        first_card_label.image = image
        self.window.get_dealer_total_label()['text'] = self.dealer.get_hand().total() 

    def dealer_play(self):
        self.revealing_first_card()
        while self.dealer.get_hand().total() < 21:
            action = self.dealer.play()
            if action == "hit":
                self.add_card_for_dealer()
                self.window.get_dealer_total_label()['text'] = self.dealer.get_hand().total() 
            else:
                break
        self.set_winner()
        self.declare_winner()

    def declare_winner(self):
        if self.winner == self.dealer:
            self.window.get_dealer_winner_label()['text'] = "WINNER"
            self.budget = self.budget - self.bet
            self.window.balence_amount_label['text'] = str(self.budget)
        elif self.winner == self.player:
            self.budget = self.budget + self.bet
            self.window.get_player_winner_label()['text'] = "WINNER"
            self.window.balence_amount_label['text'] = str(self.budget)
        else:
            self.window.get_dealer_winner_label()['text'] = "TIE"
            self.window.get_player_winner_label()['text'] = "TIE"

    def stand(self):
        self.deactivate_buttons()
        self.dealer_play()
                           
    def surrender(self):
        self.end = True
        self.window.root.destroy()

    def double(self):
        self.bet = self.bet * 2
        self.window.get_bet_amount_label()['text'] = str(self.bet)

    def play_again(self):
        self.window.root.destroy()
        if self.budget > 0:
            game = BlackJack(self.bet, self.budget)
            game.window.root.mainloop()
        else:
            menu = Menu_Window()
            game = BlackJack(menu.bet, menu.budget)
            game.window.root.mainloop()

    def setting_up_buttons(self):
        hit_button = self.window.get_hit_button()
        hit_button['command'] = lambda self = self : self.add()
        stand_button = self.window.get_stand_button()
        stand_button['command'] = lambda self = self : self.stand()
        surrender_button = self.window.get_surrender_button()
        surrender_button['command'] = lambda self = self : self.surrender()
        double_button = self.window.get_double_button()
        double_button['command'] = lambda self = self : self.double()
        play_again_button = self.window.get_play_again_button()
        play_again_button['command'] = lambda self = self: self.play_again()

    def setting_up_labels(self):
        i = 0
        player_card_labels = self.window.get_player_card_labels()
        dealer_card_labels = self.window.get_dealer_card_labels()
        
        for player in [self.player, self.dealer]:
            for card in player.get_hand():
                image = card.get_image()
                if player == self.player:
                    label = player_card_labels[i]
                    label['image'] = image 
                    label.image = image
                else:
                    back_card = Card(card.get_value(), card.get_suit())
                    back_card.set_image_location("card_back_red.png")
                    back_card_image = back_card.get_image()
                    label = dealer_card_labels[i]
                    if i == 0:
                        label['image'] = back_card_image
                        label.image = back_card_image
                    else:
                        label['image'] = image
                        label.image = image
                i += 1
            i = 0
        
        total_font = font.Font(family = 'Verdana', size = 30, weight = 'bold')
        self.window.get_balance_amount_label()['text'] = self.budget
        self.window.get_bet_amount_label()['text'] = self.bet
        self.window.get_player_total_label()['text'] = self.player.get_hand().total() 
        
        
    
    def deactivate_buttons(self):
        hit_button = self.window.get_hit_button()
        hit_button['state'] = DISABLED
        stand_button = self.window.get_stand_button()
        stand_button['state'] = DISABLED
        double_button = self.window.get_double_button()
        double_button['state'] = DISABLED

    def activate_buttons(self):
        hit_button = self.window.get_hit_button()
        hit_button['state'] = NORMAL
        stand_button = self.window.get_stand_button()
        stand_button['state'] = NORMAL
        double_button = self.window.get_double_button()
        double_button['state'] = NORMAL

    def add_card_for_dealer(self):
        card = self.deck.draw_card()
        len_of_hand = len(self.dealer.get_hand())
        self.dealer.get_hand().add_to_hand(card)
        image = card.get_image()
        label = self.window.get_dealer_card_labels()[len_of_hand]
        label['image'] = image
        label.image = image

    
    
if __name__ == '__main__':
    menu = Menu_Window()
    game = BlackJack(menu.bet, menu.budget)
    game.window.root.mainloop()
    

    

        