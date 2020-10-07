import tkinter as tk

class ScrabbleBoardSquare(tk.Frame):
    def __init__(self, location, multiplier_type=None, multiplier_value=None, name=None, master=None, **kw):
       tk.Frame.__init__(self, master, **kw)
       self.location = location
       self.multiplier_type = multiplier_type
       self.multiplier_value = multiplier_value
    
    def __repr__(self):
        if name == '':
            self.name = 'Blank'
        else:
            self.name = name

    def multiplier(self, multiplier_type=None, multiplier_value=None):
        pass

class ScrabblePlayer():
    def __init__(self, name, score=0, letters=[]):
        self.player_name = name
        self.score = score
        self.letters = letters
    
    def __repr__(self):
        return self.player_name

    def show_player_info():
        player_window = Tk()
        player_frame = Tk.Frame(master=player_window)


        player_window.mainloop()
