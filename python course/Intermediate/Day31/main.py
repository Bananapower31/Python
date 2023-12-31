from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("python course/Intermediate/Day31/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, fliptimer
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",)
    canvas.itemconfig(card_word, text=current_card["French"])
    canvas.itemconfig(card_background, image=card_front_img)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=card_back_img)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

fliptimer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="python course/Intermediate/Day31/images/card_front.png")
card_back_img = PhotoImage(file="python course/Intermediate/Day31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel 40 italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel 60 bold"))
canvas.config(bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="python course/Intermediate/Day31/images/wrong.png")
unknown_button = Button(image=cross_image, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="python course/Intermediate/Day31/images/right.png")
known_button = Button(image=check_image, borderwidth=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()