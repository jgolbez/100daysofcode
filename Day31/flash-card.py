from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


# Data Sources - Try to load previous list, if not found load full list
try:
    french_english_card = pandas.read_csv("data/words_to_learn.csv")
    lang_dict = french_english_card.to_dict(orient="records")

except FileNotFoundError:
    french_english_card = pandas.read_csv("data/french_words.csv")
    lang_dict = french_english_card.to_dict(orient="records")

finally:
    words_to_learn = lang_dict.copy()

new_card = {}



# Functions


def save_progress():
    global words_to_learn
    words_to_learn.remove(new_card)
    lang_df = pandas.DataFrame(words_to_learn)
    lang_df.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(card_canvas, image=card_back)
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_card["English"], fill="white")



# Button Functions
def check_button_press():
    global new_card, flip_timer
    save_progress()
    window.after_cancel(flip_timer)
    print(f"Removed {new_card} from list")
    new_card = random.choice(words_to_learn)
    print(f"Picked new card: {new_card}")
    canvas.itemconfig(card_canvas, image=card_front)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def x_button_press():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(words_to_learn)
    canvas.itemconfig(card_canvas, image=card_front)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

# UI
#Create window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)


# TODO Create screen
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_canvas = canvas.create_image(400, 262, image=card_front)
card_lang = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), tag="lang")
card_word = canvas.create_text(400, 250, text="", font=("Arial", 60, "bold"), tag="word")
canvas.grid(column=0, row=0, columnspan=2)
x_button_img = PhotoImage(file="images/wrong.png")
check_button_img = PhotoImage(file="images/right.png")

# TODO Create Buttons for Check / X
x_button = Button(image=x_button_img, highlightthickness=0, command=x_button_press)
x_button.grid(column=0, row=2)

check_button = Button(image=check_button_img, highlightthickness=0, command=check_button_press)
check_button.grid(column=1, row=2)

x_button_press()
# MainLoop
window.mainloop()
