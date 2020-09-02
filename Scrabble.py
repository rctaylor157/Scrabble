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

def draw_board_test():
    window = tk.Tk()
    window.title("Scrabble")
    for i in range(15):
        window.columnconfigure(i, weight=1, minsize=25)
        window.rowconfigure(i, weight=1, minsize=25)

        for j in range(15):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack(padx=5, pady=5)
            print(label)

    window.mainloop()

def setup_game(players_letters=players_letters, letter_bag=create_letter_bag()):
    for player, letters in players_letters.items():
        for i in range(7):
            letters.append(letter_bag.pop(0))
    print(players_letters)
    print(len(letter_bag))
    print(letter_bag)

def draw_board():
    window = tk.Tk()
    window.title("Scrabble")
    location = 0
    for i in range(15):
        window.columnconfigure(i, weight=1, minsize=25)
        window.rowconfigure(i, weight=1, minsize=25)
        for j in range(15):
            square = ScrabbleClass.ScrabbleBoardSquare(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
                location=location
            )
            square.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=square, text=str(location))
            label.pack(padx=5, pady=5)
            location += 1
    window.mainloop()

def score_word(word):
    word_score = 0
    word = word.upper()
    is_valid = False
    for item in valid_words_list:
        print(item)
        if word == item:
            is_valid = True
            for letter in word:
                word_score += letters_to_points.get(letter, 0)
            return word_score
    if is_valid == False:
        return 'Not a valid word!'

draw_board()