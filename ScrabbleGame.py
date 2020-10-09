class ScrabblePlay():
    active_player = str
    for player in number_of_players:
        active_player = player
    
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
