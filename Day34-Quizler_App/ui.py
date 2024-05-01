from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizGUI:
    """The GUI for the app"""
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.score_point = 0
        #setting the window 
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        #score label
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Courier', 17, 'bold'))
        self.score.grid(row=0, column=1)

        #Quesiton Canvas
        self.qtCanvas = Canvas(width=300, height=250, bg='white')
        self.question = self.qtCanvas.create_text(
            150,
            125,
            width=280,
            text="Question goes here",
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)

        self.qtCanvas.grid(row=1, column=0, columnspan=2, pady=50)

        #true button
        truebt = PhotoImage(file='Day34-Quizler_App/images/true.png')
        self.trueBt = Button(image=truebt, highlightthickness=0, command=self.true_clicked)
        self.trueBt.grid(row=2, column=0)

        #false
        falsebt = PhotoImage(file='Day34-Quizler_App/images/false.png')
        self.falseBt = Button(image=falsebt, command=self.false_clicked)
        self.falseBt.grid(row=2, column=1)

        self.get_question()
        #! keeps the windows open
        self.window.mainloop()
    
    def get_question(self):
        if self.quiz.still_has_questions():
            self.qtCanvas.config(bg='white')
            self.score.config(text=f"Score: {self.quiz.score}")
            self.question_text = self.quiz.next_question()
            self.qtCanvas.itemconfig(self.question, text=self.question_text)
        else: 
            self.qtCanvas.config(bg='white')
            self.qtCanvas.itemconfig(self.question, text="You've reached the end")
            self.trueBt.config(state="disabled")
            self.falseBt.config(state="disabled")
            
    
    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, answer):
        if answer:
            self.qtCanvas.config(bg='green')
        else:
            self.qtCanvas.config(bg='red')
        self.window.after(1000, self.get_question)
    

        
