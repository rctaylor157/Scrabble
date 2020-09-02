import tkinter as tk

class ScrabbleBoardSquare(tk.Frame):
    def __init__(self, location, multiplier_type=None, multiplier_value=None, master=None, **kw):
       tk.Frame.__init__(self, master, **kw)
       self.location = location
       self.multiplier_type = multiplier_type
       self.multiplier_value = multiplier_value

    def multiplier(self, multiplier_type=None, multiplier_value=None):
        pass