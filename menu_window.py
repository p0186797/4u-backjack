from tkinter import *
from tkinter import font
from PIL import Image, ImageTk

MENU_WIDTH = 1024
MENU_HEIGHT = 576

class Menu_Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Blackjack")
        self.root.geometry(f'{MENU_WIDTH}x{MENU_HEIGHT}')
        self.font = font.Font(family = 'Verdana', weight = 'bold', size = 30)
        self.bet = 0
        self.budget = 0
        self.make_start_menu()
        self.root.mainloop()
    
    def destroy_start_menu(self):
        self.play_button.destroy()
        self.make_second_menu()
    
    def destroy_second_menu(self):
        try:
            self.budget = int(self.budget_amount_entry.get())
            self.bet = int(self.bet_amount_entry.get())
            if self.budget > self.bet > 0:
                self.root.destroy()
            else:
                raise ValueError
        except ValueError:
            pass
            

    def make_start_menu(self):
        wallpaper = Image.open("wallpaper.png")
        wallpaper = ImageTk.PhotoImage(wallpaper)
        self.start_menu_label = Label(self.root, image = wallpaper, bg = None)
        self.start_menu_label.image = wallpaper
        
        self.start_menu_label.place(x = 0, y = 0, width = MENU_WIDTH, height = MENU_HEIGHT)
        self.play_button = Button(self.root, text = "PLAY", font = self.font)
        self.play_button.place(x = 50 , y = MENU_HEIGHT // 2, width = 200, height = 100)
        self.play_button['command'] = lambda self = self : self.destroy_start_menu()
    
    def make_second_menu(self):
        self.budget_text = Label(self.root, font = self.font, text = "Budget")
        self.budget_text.place(x = 50, y = 100, width = 150, height = 50)
    
        self.budget_amount_entry = Entry(self.root, font = self.font)
        self.budget_amount_entry.place(x = 50, y = 150, width = 150, height = 50)
      
        self.bet_text = Label(self.root, font = self.font, text = "Bet")
        self.bet_text.place(x = 50, y = 250, width = 150, height = 50)
        
        self.bet_amount_entry = Entry(self.root, font = self.font)
        self.bet_amount_entry.place(x = 50, y = 300, width = 150, height = 50)
        
        self.start_button = Button(self.root, text = 'START', font = self.font)
        self.start_button.place(x = 50, y = 400, width = 150, height = 100)
        self.start_button['command'] = lambda self = self : self.destroy_second_menu()

if __name__ == '__main__':
    m = Menu_Window()
    m.root.mainloop()
