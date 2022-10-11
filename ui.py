from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer = None
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="Question goes here", font=("Ariel", 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.my_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.my_score.grid(column=1, row=0)

        rightImg = PhotoImage(file="true.png")
        self.button_tick = Button(image=rightImg, highlightthickness=0, command=self.true_button)
        self.button_tick.grid(column=0, row=2)

        wrongImg = PhotoImage(file="false.png")
        self.button_cross = Button(image=wrongImg, highlightthickness=0, command= self.false_button)
        self.button_cross.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.my_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've finished the quiz")
            self.button_tick.config(state="disabled")
            self.button_cross.config(state="disabled")

    def true_button(self):
        self.user_answer = 'True'
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def false_button(self):
        self.user_answer = 'False'
        is_right = self.quiz.check_answer(self.user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
