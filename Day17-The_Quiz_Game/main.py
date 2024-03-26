from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


"""Convert dictionary of question and asnwers to list of objects."""
question_bank = []
for dict in question_data:
    question = Question(dict["text"], dict["answer"])
    question_bank.append(question)


"""Initiate the Game and ends it."""
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!!")
print("You final score is {}/{}".format(quiz.score, quiz.q_number))