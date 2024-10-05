from question_model import Question     # Creating instances of questions
from data import question_data          # DB or data we use in our quiz
from quiz_brain import QuizBrain        # The main logic of quiz and pandas.py just connects it all
"""
OOP with its modularity in its best. Only pandas.py knows how each of the classes works or behaves. Our quiz_brain.py 
doesn't need to be changed at all when we change our data.py over.
"""
question_bank = []

for question in question_data:
    question_text = question["question"]  # previously: text
    question_answer = question["correct_answer"]  # previously: answer
    new_que = Question(question_text, question_answer)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your current score is: {quiz.score}/{quiz.question_number}.")





