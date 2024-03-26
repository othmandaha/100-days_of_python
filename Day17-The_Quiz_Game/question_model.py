"""The defintion of the Question class."""

class Question:
    """The Question class."""

    def __init__(self, text, answer):
        """Initiate the question object.
        
        Args:
            text (str): the question.
            answer (str): the answer to the question
        """
        self.text = text
        self.answer = answer