import tkinter as tk

class ScrabbleBoardSquare(tk.Frame):
    def __init__(self, location, master=None, **kw):
       tk.Frame.__init__(self, master, **kw)
       self.location = location
       
#label = tk.Label(master=ScrabbleBoardSquare, text='test'
