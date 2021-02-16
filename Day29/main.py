from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generate():
    print("Generated a pw")
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)
    password_str = "".join(password_list)
    print(f"Your password is: {password_str}")
    password.insert(0, password_str)
    pyperclip.copy(password_str)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    valid = True
    accept = messagebox.askokcancel(title=f"{website.get()}", message=f"Entered Details:\n User ID: {userid.get()}\n Password: {password.get()}\n Is this correct?")
    if len(website.get()) == 0 or len(userid.get()) == 0 or len(password.get()) == 0:
        valid = False
        messagebox.showinfo(title="Info Missing", message="Some information is missing, please complete all fields before submitting!")
    if accept and valid:
        with open("password_list.txt", "a") as pw_list:
            pw_list.write(f"{website.get()} | {userid.get()} | {password.get()}\n")
            print("Saved the password")
        website.delete(0, 'end')
        password.delete(0, 'end')
        userid.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
#Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Create logo
canvas = Canvas(width=200, height=200)
pw_mgr_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_mgr_image)
canvas.grid(column=1, row=0)

#Website Label
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

#Website Input
website = Entry(width=35)
website.grid(column=1, row=1, columnspan=2)
website.focus()

#UserID Label
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

#User ID Input
userid = Entry(width=35)
userid.grid(column=1, row=2, columnspan=2)
userid.insert(0, "my@email.com")

#Password Label
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

#Password Input
password = Entry(width=21)
password.grid(column=1, row=3)

#Generate PW Button
pw_button = Button(text="Generate Password", command=pw_generate)
pw_button.grid(column=2, row=3)

#Add PW Button
add_button = Button(text="Add", width=36, command=save_pw)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()