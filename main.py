from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    new_question = Question(i["question"],i["correct_answer"])
    question_bank.append(new_question)


test = QuizBrain(question_bank)

while test.still_has_questrion():
    test.next_question()

print("You've completed the quiz")
print(f"Your final score was: {test.score}/{test.question_number}")