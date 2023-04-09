import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.current_score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score = tkinter.Label(self.window, text=f'Score: {self.current_score}', bg=THEME_COLOR, fg='white',
                                   font=('Arial', 16))
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(self.window, height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Question goes here",
                                                     font=('Arial', 17, 'italic'),
                                                     fill=THEME_COLOR, width=250)

        tick_image = tkinter.PhotoImage(file='images/true.png')
        self.tick_button = Button(self.window, image=tick_image, highlightthickness=0,
                                  command=lambda: self.button_click_handler(1))
        self.tick_button.grid(row=2, column=0, pady=20)

        cross_image = tkinter.PhotoImage(file='images/false.png')
        self.cross_button = Button(self.window, image=cross_image, highlightthickness=0,
                                   command=lambda: self.button_click_handler(2))
        self.cross_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def button_click_handler(self, button_id):
        self.check_answer(button_id)
        if self.quiz.still_has_questions():

            self.get_next_question()

        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f'Quiz Completed! You scored: {self.current_score}/{self.quiz.question_number}')
            self.canvas.config(bg='white')
            self.tick_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def check_answer(self, button_id):
        answer = self.quiz.check_answer().lower()

        if button_id == 1:
            user_answer = 'true'
        if button_id == 2:
            user_answer = 'false'

        if user_answer == answer:
            self.current_score += 1
            self.score.config(text=f'Score: {self.current_score}')
            self.canvas.config(bg='green')
            self.canvas.update()
            self.window.after(1000, self.canvas.config(bg='white'))

        else:
            self.canvas.config(bg='red')
            self.canvas.update()
            self.window.after(1000, self.canvas.config(bg='white'))











