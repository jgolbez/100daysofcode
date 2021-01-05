#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def pw_random(randomlist, nr_number):
  while nr_number >= 1:
    char = random.choice(randomlist)
    easy_random_pw.append(char)
    nr_number -= 1

easy_random_pw = []
pw_random(letters, nr_letters)
pw_random(symbols, nr_symbols)
pw_random(numbers, nr_numbers)

easy_pw_string = ""
for char in easy_random_pw:
  easy_pw_string += char

print(f"The easy password string is {easy_pw_string}.")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(easy_random_pw)
hard_pw_string = ""
for char in easy_random_pw:
  hard_pw_string += char
print(f"The hard random password is: {hard_pw_string}")
