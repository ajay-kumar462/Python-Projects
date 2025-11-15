from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: ", bg=THEME_COLOR, font=("Arial", 15, "bold"), fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_next = self.canvas.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)

        correct_img = PhotoImage(file="./images/true.png")
        wrong_img = PhotoImage(file="./images/false.png")

        self.correct = Button(image=correct_img, command=self.clicked_correct, highlightthickness=0)
        self.correct.grid(row=2, column=0)

        self.wrong = Button(image=wrong_img, command=self.clicked_wrong, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_next, text=q_text)
        else:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_next, text="You've reached the end")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def clicked_correct(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def clicked_wrong(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, right_or_wrong):
        if right_or_wrong:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



