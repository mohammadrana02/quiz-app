from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Rana's Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Hello", font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.tick_image = PhotoImage(file="images/true.png")
        self.cross_image = PhotoImage(file="images/false.png")
        self.tick = Button(image=self.tick_image, highlightthickness=0)
        self.cross = Button(image=self.cross_image, highlightthickness=0)
        self.tick.grid(column=0, row=2)
        self.cross.grid(column=1, row=2)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

