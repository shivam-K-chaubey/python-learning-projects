import customtkinter as ctk
from api.quiz_api import QuizAPI
from models.questions import Question
from ui.quiz_screen import QuizScreen

class QuizSettings(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        self.heading = ctk.CTkLabel(
            self,
            text="Quiz Settings",
            font=("Arial", 32, "bold")
        )

        self.heading.pack(pady=20)

        self.settings_frame = ctk.CTkFrame(self)

        self.settings_frame.pack(pady=20)

        self.category_label = ctk.CTkLabel(
            self.settings_frame,
            text="Category"
        )

        self.category_label.pack(pady=(10, 5))

        self.category_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["Science", "History", "Sports", "Technology"],
            width=250
        )

        self.category_menu.pack(pady=(0, 15))

        self.difficulty_label = ctk.CTkLabel(
            self.settings_frame,
            text="Difficulty"
        )

        self.difficulty_label.pack(pady=(10, 5))

        self.difficulty_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["Easy", "Medium", "Hard"],
            width=250
        )

        self.difficulty_menu.pack(pady=10)

        self.type_label = ctk.CTkLabel(
            self.settings_frame,
            text="Type"
        )

        self.type_label.pack(pady=(10, 5))

        self.type_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["Multiple Choice", "True/False"],
            width=250
        )

        self.type_menu.pack(pady=10)

        self.amount_label = ctk.CTkLabel(
            self.settings_frame,
            text="Number of Questions"
        )

        self.amount_label.pack(pady=(10, 5))

        self.amount_menu = ctk.CTkOptionMenu(
            self.settings_frame,
            values=["5", "10", "15", "20"],
            width=250
        )

        self.amount_menu.pack(pady=10)

        self.start_quiz_button = ctk.CTkButton(
            self.settings_frame,
            text="Start Quiz",
            command=self.start_quiz
        )

        self.start_quiz_button.pack(pady=20)

    def start_quiz(self):
        category = self.category_menu.get()
        difficulty = self.difficulty_menu.get()
        question_type = self.type_menu.get()
        amount = int(self.amount_menu.get())

        api = QuizAPI()

        questions = api.get_questions(amount)
        question_bank = []
        for question in questions:
            q = Question(
                text=question["question"],
                correct_answer=question["correct_answer"],
                incorrect_answers=question["incorrect_answers"]
            )
            question_bank.append(q)

        self.destroy()
        QuizScreen(
            self.master,
            question_bank,
        )
