import tkinter as tk
import random
import ScrabbleClass

# create Scrabble set
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[""] = 0
letter_bag = []
valid_words_list = []
with open('valid_words.txt', 'r') as valid_words:
    for line in valid_words.readlines():
        line = line.strip('\n\t')
        valid_words_list.append(line.upper())
print(len(valid_words_list))
players_scores = {'player1': 0, 'player2': 0, 'player3': 0, 'player4': 0}
players_letters = {'player1': [], 'player2': [], 'player3': [], 'player4': []}
triple_word_score_loc = [0, 7, 14, 105, 119, 210, 217, 224]
double_word_score_loc = [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]
triple_letter_score_loc = [20, 24, 76, 80, 84, 88,136, 140, 144, 148, 200, 204]
double_letter_score_loc = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]

def create_letter_bag():
    letter_bag = []
    # 1-point letters
    for i in range(12):
        letter_bag.append("E")
    for i in range(9):
        letter_bag.append("A")
    for i in range(9):
        letter_bag.append("I")
    for i in range(8):
        letter_bag.append("O")
    for i in range(6):
        letter_bag.append("N")
    for i in range(6):
        letter_bag.append("R")
    for i in range(6):
        letter_bag.append("T")
    for i in range(4):
        letter_bag.append("L")
    for i in range(4):
        letter_bag.append("S")
    for i in range(4):
        letter_bag.append("U")
    # 2-point letters
    for i in range(4):
        letter_bag.append("D")
    for i in range(3):
        letter_bag.append("G")
    # 3-point letters
    for i in range(2):
        letter_bag.append("B")
    for i in range(2):
        letter_bag.append("C")
    for i in range(2):
        letter_bag.append("M")
    for i in range(2):
        letter_bag.append("P")
    # 4-point letters
    for i in range(2):
        letter_bag.append("F")
    for i in range(2):
        letter_bag.append("H")
    for i in range(2):
        letter_bag.append("V")
    for i in range(2):
        letter_bag.append("W")
    for i in range(2):
        letter_bag.append("Y")
    # other letters
    letter_bag.append("K")
    letter_bag.append("J")
    letter_bag.append("X")
    letter_bag.append("Q")
    letter_bag.append("Z")
    for i in range(2):
        letter_bag.append("")
    random.shuffle(letter_bag)
    return letter_bag

def setup_game(players_letters=players_letters, letter_bag=create_letter_bag()):
    for player, letters in players_letters.items():
        for i in range(7):
            letters.append(letter_bag.pop(0))
    print(players_letters)
    print(len(letter_bag))
    print(letter_bag)

def draw_board():
    board = tk.Tk()
    board.title("Scrabble")
    location = 0
    for i in range(15):
        board.columnconfigure(i, weight=1)
        board.rowconfigure(i, weight=1)
        for j in range(15):
            if location in triple_word_score_loc:
                name = 'Triple \n Word \n Score'
                multiplier_type = 'word'
                multiplier_value = 3
            elif location in double_word_score_loc:
                name = 'Double \n Word \n Score'
                multiplier_type = 'word'
                multiplier_value = 2
            elif location in triple_letter_score_loc:
                name = 'Triple \n Letter \n Score'
                multiplier_type = 'letter'
                multiplier_value = 3
            elif location in double_letter_score_loc:
                name = 'Double \n Letter \n Score'
                multiplier_type = 'letter'
                multiplier_value = 2
            elif location == 112:
                name = 'Center'
                multiplier_type = 'word'
                multiplier_value = 2
            square = ScrabbleClass.ScrabbleBoardSquare(
                master=board,
                relief=tk.RAISED,
                borderwidth=1,
                location=location
            )
            square.grid(row=i, column=j, padx=1, pady=1)
            label = tk.Label(master=square, text=name, height=5, width=5)
            label.pack(padx=1, pady=1)
            location += 1
            name = ''
    board.mainloop()

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

draw_board()