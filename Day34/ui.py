# Imports
from tkinter import *
from quiz_brain import QuizBrain

# Data Sources/Global Variables
THEME_COLOR = "#375362"


# Class



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="", width=280, font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR, tag="question")
        self.canvas.grid(column=0, row=1, columnspan=2)
        x_button_img = PhotoImage(file="images/false.png")
        check_button_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_button_img, highlightthickness=0, command=self.check_button_press)
        self.check_button.grid(column=0, row=2)
        self.x_button = Button(image=x_button_img, highlightthickness=0, command=self.x_button_press)
        self.x_button.grid(column=1, row=2)
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def check_button_press(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def x_button_press(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






