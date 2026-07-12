import customtkinter as ctk
import random

class QuizScreen(ctk.CTkFrame):
    def __init__(self, parent, question_bank):
        super().__init__(parent)

        self.question_bank = question_bank
        self.pack(fill="both", expand=True)

        self.current_question_index = 0
        self.score = 0

        self.question_number_label = ctk.CTkLabel(
            self,
            text="Question 1/10",
            font=("Arial", 20)
        )

        self.question_number_label.pack(pady=10)

        self.question_label = ctk.CTkLabel(
            self,
            text="Question appears here",
            font=("Arial", 24, "bold"),
            wraplength=700
        )
        self.question_label.pack(pady=20)

        self.answers_frame = ctk.CTkFrame(self)

        self.answer_button = []

        for _ in range(4):
            button = ctk.CTkButton(
                self.answers_frame,
                text="Answer",
                width=300,
            )
            button.configure(
                command=lambda b=button: self.check_answer(b)
            )
            button.pack(pady=10)

            self.answer_button.append(button)

        self.answers_frame.pack(pady=20)

        self.score_label= ctk.CTkLabel(
            self,
            text="Score: 0",
            font=("Arial", 18)
        )

        self.score_label.pack(pady=20)

        self.load_question()

    def load_question(self):
        question = self.question_bank[
            self.current_question_index
        ]
        self.question_number_label.configure(
            text= f"Question {self.current_question_index + 1}/10"
        )
        self.question_label.configure(
            text=question.text
        )

        answers = (
                question.incorrect_answers
                + [question.correct_answer]
        )

        random.shuffle(answers)

        for button, answer in zip(
                self.answer_button,
                answers
        ):
            button.configure(text=answer)

    def check_answer(self, button):
        selected_answer = button.cget("text")
        question = self.question_bank[
            self.current_question_index
        ]

        if selected_answer == question.correct_answer:
            self.score += 1
            self.score_label.configure(
                text=f"Score: {self.score}"
            )
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index >= len(self.question_bank):
            self.question_label.configure(
                text="Quiz Completed!"
            )
            for button in self.answer_button:
                button.configure(state = "Disable")
        else:
            self.load_question()
