import random
from tkinter import *
import pandas

BG_COLOR = "#B1DDC6"
to_lear={}
try:
    data = pandas.read_csv("word_to_learn.csv")
except:
    original_data = pandas.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
currend_card={}

def next_card():
    global  currend_card, flip_timer
    window.after_cancel(flip_timer)
    currend_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French", fill="black")
    canvas.itemconfig(card_word, text = currend_card["French"], fill="black")
    canvas.itemconfig(image_bg, image=photo)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=currend_card["English"], fill="white")
    canvas.itemconfig(image_bg, image=photo1)

def is_Know():
    to_learn.remove(currend_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_to_learn.csv")
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady= 50, bg=BG_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
photo = PhotoImage(file="card_front.png")
photo1 = PhotoImage(file="card_back.png")
image_bg = canvas.create_image(400, 263, image = photo)
card_title = canvas.create_text(400, 150, text="",font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="",font=("Arial", 60, "bold"))
canvas.config(background=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

unknow_Image = PhotoImage(file="wrong.png")
unknow_button = Button(image=unknow_Image, highlightthickness=0, command=next_card)
unknow_button.grid(row=1, column=0)

check_Image = PhotoImage(file="right.png")
check_button = Button(image=check_Image, highlightthickness=0, command=is_Know)
check_button.grid(row=1, column=1)

next_card()

window.mainloop()