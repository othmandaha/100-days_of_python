"""The Quiz Brain Definition."""


class QuizBrain:
    """QuizBrain class."""

    def __init__(self, q_list):
        """Initiates the object.
        
        Args:
            q_list (list): list of questions and there answers"""
        self.q_list = q_list
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        """Returns True if it there are still remaining questions
        False otherwise."""
        return self.q_number < len(self.q_list)


    def next_question(self):
        """Gives questions and prompts for answers."""
        current_question = self.q_list[self.q_number]
        self.q_number += 1
        user_answer =input("Q.{}: {} (True/False)?: ".format(self.q_number, current_question.text))
        self.check_answer(user_answer, current_question.answer)

    
    def check_answer(self, user_answer, correct_answer):
        """Check if the answer is correct.
        
        Args:
            user_answer (str): the answer from the user input.
            correct_answer (str): the correct answer.
        """
        if user_answer.lower() == correct_answer.lower():
            print("You've got it right")
            self.score += 1 
        else:
            print("That's not right, the correct answer is {}".format(correct_answer))
        print("Your score is {}/{}.".format(self.score, self.q_number))
        print("\n")

