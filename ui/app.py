import customtkinter as ctk

class QuizApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Quiz Game")
        self.geometry("900x600")

        #Setting the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.heading = ctk.CTkLabel(
            self,
            text="Quiz Game",
            font=("Arial", 40, "bold")
        )

        self.heading.pack(pady=40)
        self.start_button = ctk.CTkButton(
            self,
            text="Start Quiz",
            width=200,
            height=50
        )
        self.start_button.pack(pady=20)
