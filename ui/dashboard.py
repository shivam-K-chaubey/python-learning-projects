import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        self.heading = ctk.CTkLabel(
            self,
            text="Welcome to Quiz Dashboard",
            font=("Arial", 32, "bold")
        )

        self.heading.pack(pady=50)

        self.start_button = ctk.CTkButton(
            self,
            text="Start Quiz",
            width=200,
            height=50
        )

        self.start_button.pack(pady=20)