import tkinter
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(new_img, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, to_english)

def to_english():
    canvas.itemconfig(new_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    data2 = pandas.DataFrame(data_dict)
    data2.to_csv("data/words_to_learn.csv", index=False)
    random_word()

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, to_english)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
new_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cancel_img = PhotoImage(file="./images/wrong.png")
correct_img = PhotoImage(file="./images/right.png")

cancel_btn = Button(image=cancel_img, command=random_word, highlightthickness=0)
cancel_btn.grid(row=1, column=0)

correct_btn = Button(image=correct_img, command=is_known, highlightthickness=0)
correct_btn.grid(row=1, column=1)

random_word()
print(current_card)

window.mainloop()

