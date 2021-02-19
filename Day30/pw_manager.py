from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
        try:
            with open("pw.json", "r") as pw_list:
                #Load current dict data
                pw_data = json.load(pw_list)
                #Update old data with new data - pull from filled out fields
                pw_data.update({website.get(): {"userid": userid.get(), "password": password.get()}})
        except FileNotFoundError:
            with open("pw.json", "w") as pw_list:
                json.dump({website.get(): {"userid": userid.get(), "password": password.get()}}, pw_list, indent=4)
        else:
            with open("pw.json", "w") as pw_list:
                #Dump updated dict back to file
                json.dump(pw_data, pw_list, indent=4)
        finally:
            website.delete(0, 'end')
            password.delete(0, 'end')

# ---------------------------- SEARCH ------------------------------- #
def search_pw():
    print("Searching")
    search_item = website.get()
    try:
        with open("pw.json", "r") as pw_list:
            # Load current dict data
            pw_data = json.load(pw_list)
            password_data = pw_data[search_item]["password"]
            print(password_data)
            userid_data = pw_data[search_item]["userid"]
    except FileNotFoundError:
        messagebox.showinfo(title="No Entries", message="You have not entered any passwords yet.")
    except KeyError:
        messagebox.showinfo(title="Not Found", message="You have not entered a password for this website yet.")
    else:
        messagebox.showinfo(title=search_item, message=f"User ID: {userid_data}\n Password: {password_data}")


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
website = Entry(width=30)
website.grid(column=1, row=1)
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

#Search Button
search_button = Button(text="Search", command=search_pw)
search_button.grid(column=2, row=1)

window.mainloop()