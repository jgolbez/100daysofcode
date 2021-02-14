from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
# Reset Button
def reset_button_press():
    global REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    check_label.config(text="")
    REPS = 0
    print("Reset Button was pressed")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Start Button
def start_button_press():
    global REPS
    REPS += 1
    print("Start Button was pressed")
    print(REPS)
    if REPS % 8 == 0:
        print("STARTING LONG BREAK")
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)

    elif REPS % 2 == 0:
        print("STARTING SHORT BREAK")
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        print("STARTING WORK MINS")
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#Count down
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        checks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            checks += "✔"
            check_label.config(text=checks)
            check_label.grid(column=1, row=4)
        start_button_press()




# ---------------------------- UI SETUP ------------------------------- #
#Basic Window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=105, pady=50, bg=YELLOW)

#Tomato Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

#Create a variable from the canvas create text so we can change it below
timer_text = canvas.create_text(103, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

#Word: Timer
timer_label = Label(text="Timer")
timer_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

#Check Mark Label
check_label = Label()
check_label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 32, "bold"))
check_label.grid(column=1, row=4)

reset_button = Button(text="Reset", command=reset_button_press)
reset_button.grid(column=3, row=3)


start_button = Button(text="Start", command=start_button_press)
start_button.grid(column=0, row=3)



window.mainloop()