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
        self.tick = Button(image=self.tick_image, highlightthickness=0, command=self.true_pressed)
        self.cross = Button(image=self.cross_image, highlightthickness=0, command=self.false_pressed)
        self.tick.grid(column=0, row=2)
        self.cross.grid(column=1, row=2)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
