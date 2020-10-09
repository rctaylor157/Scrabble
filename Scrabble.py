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

class ScrabbleGame():
    def __init__(self)
    active_player = str
    
    def player_letters_display():
        letters_display = tk.Tk()
        letters_display.title("Letters")
        for i in range(7):
            letters_display.columnconfigure(i, weight=1)
            letters_display.rowconfigure(1, weight=1)
            frame = Frame.Tk(master=letters_display)
            letter_tile = Label.Tk(master=frame, text=active_player.letter[i])
        
        letters_display.mainloop()
        
    def score_word(word):
        word_score = 0
        word = word.upper()
        is_valid = False
        for item in valid_words_list:
            if word == item:
                is_valid = True
                for letter in word:
                    word_score += letters_to_points.get(letter, 0)
                return word_score
        if is_valid == False:
            return 'Not a valid word!'
