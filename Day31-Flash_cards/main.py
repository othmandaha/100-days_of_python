from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
index = None

#! Opening the csv file
try:
    words_list = pandas.read_csv('Day31-Flash_cards/data/words_to_learn.csv')
except FileNotFoundError:
    words_list = pandas.read_csv('Day31-Flash_cards/data/french_words.csv')
finally:
    words_list = words_list.to_dict(orient='records')



#!--------------------------   remove_word   ---------------------------!#
def remove_word():
    global index
    words_to_learn = words_list
    words_to_learn.remove(index)
    words_data = pandas.DataFrame(words_to_learn)
    words_data.to_csv("Day31-Flash_cards/data/words_to_learn.csv", index=False)
    next_word()




#!--------------------------   flip   ---------------------------!#
def flip(random_word):
    """flips the card to display the english word"""
    cards_canvas.itemconfig(card, image=card_back)
    cards_canvas.itemconfig(language, text='English', fill='white')
    cards_canvas.itemconfig(word, text=random_word['English'], fill='white')


#!--------------------------   Picker   ---------------------------!#
def next_word():
    """picks a random word to display"""
    global index
    random_word =  random.choice(words_list)
    index = random_word
    french_word =  random_word['French']
    cards_canvas.itemconfig(card, image=card_front)
    cards_canvas.itemconfig(language, text='French', fill='black')
    cards_canvas.itemconfig(word, text=french_word, fill='black')
    window.after(3000, flip, random_word)


#!--------------------------   UI   ---------------------------!#
#* Window setting
window = Tk()
window.title("Flashy")
window.config(height=700, width=1000, bg=BACKGROUND_COLOR, padx=50, pady=50)

#* importing images
card_front = PhotoImage(file='Day31-Flash_cards/images/card_front.png')
card_back = PhotoImage(file='Day31-Flash_cards/images/card_back.png')
right = PhotoImage(file='Day31-Flash_cards/images/right.png')
wrong = PhotoImage(file='Day31-Flash_cards\images\wrong.png')

#* Cards Canvas
cards_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card = cards_canvas.create_image(400, 263, image=card_front)
    # setting text in canvas:
language = cards_canvas.create_text(400, 150, text='', font=("Ariel", 30, "italic"))
word = cards_canvas.create_text(400, 263, text='', font=("Ariel", 60, "bold"))
cards_canvas.grid(row=0, column=0, columnspan=2)
next_word()



#* Buttons
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)


#! Keeps the window open
window.mainloop()
