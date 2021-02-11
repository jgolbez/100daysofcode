from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)

#Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)
km_calc_label = Label(text="0")
km_calc_label.grid(column=1, row=1)
km_calc_label.config(padx=10, pady=10)
#
user_input = Entry(width=10)
#Add some text to begin with
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)


#Buttons
def button_clicked():
    mile_convert = user_input.get()
    km_calc = float(mile_convert) * 1.609
    km_calc_label.config(text=f"{km_calc}")

#calls action() when pressed
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)



window.mainloop()