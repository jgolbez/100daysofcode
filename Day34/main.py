# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Data Sources/Global Variables
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Main Loop
#while quiz.still_has_questions():
#    quiz.next_question()
quiz_window = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
