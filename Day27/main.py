from tkinter import *

window = Tk()
window.title("TKInter Fun")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10)


# Label
label = Label(text="Fucking Labels and Shit", font=("Courier", 24, "bold"))

# Can directly modify object attribute as if it were a K/V ina dict, or use the config to edit attrib
label["text"] = "New Text"
label.config(text="Newer Text")
label.grid(column=0, row=0)
label.config(padx=40, pady=40)


# Button
def button_clicked():
    print("Button was clicked")
    label_text = user_input.get()
    label.config(text=label_text)


button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=3, row=0)

# Entry

user_input = Entry(width=10)
user_input.grid(column=4, row=4)


window.mainloop()
'''
#*args creates unlimited/unspecified arguments passed into funct, creates a tuple that can be indexed
def add(*args):
    print(args[2])
    sum = 0
    for n in args:
        print(n)
        sum += n
    return sum

print(add(1, 4, 5, 2))
'''

'''
#kwargs allows us to pass in unlimited/unspecified keyword/positional arguments
def calculate(n, **kwargs):
#    print(kwargs)
#    print(type(kwargs))
#    for k, v in kwargs.items():
#        print(k)
#        print(v)
    n += kwargs["add"] # This uses N value, adds to whatever is the value in the kwargs dict for 'add' key (3)
    n *= kwargs["multiply"] # This uses N value, multiplies to whatever is the value in the kwargs dict for 'multiply' key (5)
    print(n)

calculate(2, add=3, multiply=5)


#showing how we can set attributes (or not) with kwargs in a Class
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Nissan", model="GTG-R")
print(my_car.model)


#If we don't pass in a value for one of the attributes it will throw a error when called
#Instead we can use get("make") method which will return None instead of traceback if it doesnt exist

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.seats) # Returns None
'''
