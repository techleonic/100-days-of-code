from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
word_lan = "French"
current_word = {}

df = pandas.read_csv("data/french_words.csv")
word_dict = df.to_dict(orient="records")
# print(word_dict[0]["French"])
# print(word_dict[0]["English"])

def random_word():
    global word_lan
    global current_word
    global flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(word_dict)
    canvas.itemconfig(title,text=word_lan, fill="black")
    canvas.itemconfig(word, text=f"{current_word[word_lan]}", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    window.after(3000, flip_card)


def flip_card():
    global word_lan
    global  current_word
    word_lan = "English" if word_lan == "French" else "French"
    canvas.itemconfig(title,text=word_lan,fill="white")
    canvas.itemconfig(word, text=f"{current_word[word_lan]}",fill="white")
    canvas.itemconfig(card_background, image=card_back)


window =  Tk()
window.title("Flashy")
window.config(pady=50, padx=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front =  PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text='Title', font=("Ariel",40,"italic"))
word = canvas.create_text(400,263, text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

random_word()

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img,highlightthickness=0,command=random_word)
unknown_button.grid(row=1, column=0)

check_img =  PhotoImage(file="images/right.png")
known_button = Button(image=check_img,highlightthickness=0,command=random_word)
known_button.grid(row=1,column=1)


window.mainloop()

