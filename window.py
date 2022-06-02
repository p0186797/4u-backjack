
from tkinter import *
from tkinter import font

OVERALL_WIDTH = 1500
WIDTH = 1000
HEIGHT = 800
CARD_WIDTH = 500
CARD_HEIGHT = 726
DARK_GREEN = '#08521c'
BORDERWIDTH = 20
STEEL = '#2a382e'
CARD_FRAME_WIDTH = CARD_WIDTH // 3
CARD_FRAME_HEIGHT = CARD_HEIGHT // 3

BUTTON_FRAME_HEIGHT = 100
PLAYER_FRAME_HEIGHT = (HEIGHT - BUTTON_FRAME_HEIGHT - 2 * BORDERWIDTH) / 2

BUTTON_WIDTH = (WIDTH - 7 * BORDERWIDTH) / 6
BUTTON_HEIGHT = BUTTON_FRAME_HEIGHT - 2 * BORDERWIDTH

BIG_BUTTON_WIDTH = 300
BIG_BUTTON_HEIGHT = 200

class Window:

    def __init__(self):
        self.root = Tk()
        self.root.title("Blackjack")
        self.root.geometry(f'{OVERALL_WIDTH}x{HEIGHT}')
        self.root['background'] = DARK_GREEN
        self.setup()
        
    def get_root(self):
        return self.root

    def get_player_card_labels(self):
        return self.player_card_labels

    def get_dealer_card_labels(self):
        return self.dealer_card_labels
    
    def get_hit_button(self):
        return self.hit_button
    
    def get_stand_button(self):
        return self.stand_button
    
    def get_double_button(self):
        return self.double_button
    
    def get_surrender_button(self):
        return self.surrender_button
    
    def get_balance_amount_label(self):
        return self.balence_amount_label
    
    def get_bet_amount_label(self):
        return self.bet_amount_label
    
    def get_player_total_label(self):
        return self.player_total_label
    
    def get_dealer_total_label(self):
        return self.dealer_total_label

    def get_player_winner_label(self):
        return self.player_winner_label
    
    def get_dealer_winner_label(self):
        return self.dealer_winner_label
    
    def get_play_again_button(self):
        return self.play_again_button

    def make_overall_frames(self):
        self.player_frame = Frame(self.root,background = DARK_GREEN, borderwidth = BORDERWIDTH)
        self.player_frame.place(x = 0, y = PLAYER_FRAME_HEIGHT + BORDERWIDTH, width = WIDTH, height = PLAYER_FRAME_HEIGHT)

        self.dealer_frame = Frame(self.root, background = DARK_GREEN, borderwidth = BORDERWIDTH)
        self.dealer_frame.place(x = 0, y = 0, width = WIDTH, height = PLAYER_FRAME_HEIGHT)
        
        self.button_frame = Frame(self.root, background = 'black', borderwidth = BORDERWIDTH)
        self.button_frame.place(x = 0, y = PLAYER_FRAME_HEIGHT + BORDERWIDTH + PLAYER_FRAME_HEIGHT, width = OVERALL_WIDTH, height = BUTTON_FRAME_HEIGHT)
    
    def make_buttons(self):
        text_font = font.Font(family = 'Verdana', weight = 'bold', size = 16)
        
        self.balance_frame = Frame(self.button_frame, borderwidth = BORDERWIDTH/2)
        self.balance_frame.place(x = 0, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

        self.balance_label = Label(self.balance_frame, text = "Balance", font = text_font)
        self.balance_label.place(x = 0, y = 0, width = BUTTON_WIDTH - 2 * BORDERWIDTH /2, height = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2)

        self.balence_amount_label = Label(self.balance_frame)
        self.balence_amount_label.place(x = 0, y = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2, width = BUTTON_WIDTH - 2 * BORDERWIDTH /2, height = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2)

        self.bet_frame = Frame(self.button_frame, borderwidth = BORDERWIDTH / 2)
        self.bet_frame.place(x = BUTTON_WIDTH + BORDERWIDTH, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

        self.bet_label = Label(self.bet_frame, text = "Bet", font = text_font)
        self.bet_label.place(x = 0, y = 0, width = BUTTON_WIDTH - 2 * BORDERWIDTH /2, height = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2)

        self.bet_amount_label = Label(self.bet_frame)
        self.bet_amount_label.place(x = 0, y = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2, width = BUTTON_WIDTH - 2 * BORDERWIDTH /2, height = (BUTTON_HEIGHT - 2 * BORDERWIDTH/2)/ 2)

        self.hit_button = Button(self.button_frame, text = "HIT", font = text_font)
        self.hit_button.place(x = (BUTTON_WIDTH + BORDERWIDTH) * 2, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

        self.stand_button = Button(self.button_frame, text = "STAND", font = text_font)
        self.stand_button.place(x = (BUTTON_WIDTH + BORDERWIDTH) * 3, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

        self.surrender_button = Button(self.button_frame, text = "QUIT", font = text_font)
        self.surrender_button.place(x = (BUTTON_WIDTH + BORDERWIDTH) * 4, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT)

        self.double_button = Button(self.button_frame, text = "Double", font = text_font)
        self.double_button.place(x = (BUTTON_WIDTH + BORDERWIDTH) * 5, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT / 2)
    
        self.play_again_button = Button(self.button_frame, text = "Play Again", font = text_font)
        self.play_again_button.place(x = (BUTTON_WIDTH + BORDERWIDTH) * 6, y = 0, width = BUTTON_WIDTH, height = BUTTON_HEIGHT / 2)
    
    def make_card_labels(self): 
        self.player_card_labels = []
        for i in range(5):
            l = Label(self.player_frame, background = DARK_GREEN)
            l.place(x = i * (CARD_FRAME_WIDTH + BORDERWIDTH), y = 0, width = CARD_FRAME_WIDTH, height = CARD_FRAME_HEIGHT)
            self.player_card_labels.append(l)

        self.dealer_card_labels = []
        for i in range(5):
            l = Label(self.dealer_frame, background = DARK_GREEN)
            l.place(x = i * (CARD_FRAME_WIDTH + BORDERWIDTH), y = 0, width = CARD_FRAME_WIDTH, height = CARD_FRAME_HEIGHT)
            self.dealer_card_labels.append(l)
        
    def make_stats_area(self):
        text_font = font.Font(family = 'Verdana', weight = 'bold', size = 16)
        winner_font = font.Font(family = 'Verdana', weight = 'bold', size = 24)

        self.dealer_stats_frame = Frame(self.root, background = DARK_GREEN, borderwidth = BORDERWIDTH)
        self.dealer_stats_frame.place(x = WIDTH + BORDERWIDTH, y = 0, width = OVERALL_WIDTH - WIDTH, height = PLAYER_FRAME_HEIGHT)

        self.dealer_total_label = Label(self.dealer_stats_frame, background = DARK_GREEN, font = text_font)
        self.dealer_total_label.place(x = 0, y = 0, width = OVERALL_WIDTH - WIDTH - 2 * BORDERWIDTH, height = BUTTON_HEIGHT)

        self.dealer_winner_label = Label(self.dealer_stats_frame, background = DARK_GREEN, font = winner_font)
        self.dealer_winner_label.place(x = 0, y = BUTTON_HEIGHT, width = OVERALL_WIDTH - WIDTH - 2 * BORDERWIDTH, height = BUTTON_HEIGHT)
        
        self.player_stats_frame = Frame(self.root, background = DARK_GREEN, borderwidth = BORDERWIDTH)
        self.player_stats_frame.place(x = WIDTH + BORDERWIDTH, y = PLAYER_FRAME_HEIGHT + BORDERWIDTH, width = OVERALL_WIDTH - WIDTH, height = PLAYER_FRAME_HEIGHT)

        self.player_total_label = Label(self.player_stats_frame, background = DARK_GREEN, font = text_font)
        self.player_total_label.place(x = 0, y = 0, width = OVERALL_WIDTH - WIDTH - 2 * BORDERWIDTH, height = BUTTON_HEIGHT)

        self.player_winner_label = Label(self.player_stats_frame, background = DARK_GREEN, font = winner_font)
        self.player_winner_label.place(x = 0, y = BUTTON_HEIGHT, width = OVERALL_WIDTH - WIDTH - 2 * BORDERWIDTH, height = BUTTON_HEIGHT)
 

    def setup(self):
        self.make_overall_frames()
        self.make_buttons()
        self.make_card_labels()
        self.make_stats_area()
        
        
if __name__ == '__main__':       
    w = Window()
    w.root.mainloop()

