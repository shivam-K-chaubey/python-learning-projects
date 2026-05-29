import customtkinter as ctk
from ui.dashboard import DashboardFrame

class QuizApp(ctk.CTk):

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.resizable(False, False)
        self.title("Quiz Game")
        self.geometry("900x900")

        #Setting the theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        #Heading
        self.heading = ctk.CTkLabel(
            self,
            text="Quiz Game",
            font=("Poppins", 42, "bold")
        )

        self.heading.pack(pady=40)
        #Login Frame
        self.login_frame = ctk.CTkFrame(
            self,
            width=400,
            height=350
        )

        self.login_frame.pack(pady=20)

        # Username Label
        self.username_label = ctk.CTkLabel(
            self.login_frame,
            text="Username"
        )

        self.username_label.pack(pady=(30, 5))

        self.username_entry = ctk.CTkEntry(
            self.login_frame,
            width=250,
            placeholder_text="Enter username"
        )

        self.username_entry.pack(pady=5)

        # Password label
        self.password_label = ctk.CTkLabel(
            self.login_frame,
            text="Password"
        )
        self.password_label.pack(pady=(20, 5))

        # Password Entry
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            width=250,
            placeholder_text="Enter password",
            show="*"
        )

        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = ctk.CTkButton(
            self.login_frame,
            width=200,
            text="Login",
            command=self.login
        )

        self.login_button.pack(pady=(30, 10))

        # Signup Button
        self.signup_button = ctk.CTkButton(
            self.login_frame,
            text="Sign Up",
            width=200,
            command=self.signup
        )
        self.signup_button.pack()

        # Message label
        self.message_label = ctk.CTkLabel(
            self.login_frame,
            text = "",
            text_color="red"
        )

        self.message_label.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        valid = self.db.validate_user(username, password)

        if valid:
            self.open_dashboard()

        else:
            self.message_label.configure(
                text="Invalid username or password.",
                text_color="red"
            )


    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if len(username) < 3:
            self.message_label.configure(
                text="Username must contain at least 3 characters."
            )
            return

        if len(password) < 6:
            self.message_label.configure(
                text="Password must contain at least 6 characters."
            )
            return

        success = self.db.create_user(username, password)

        if success:
            self.message_label.configure(
                text="Account created successfully!",
                text_color="green"
            )
        else:
            self.message_label.configure(
                text="Username already exists.",
                text_color="red"
            )

    def open_dashboard(self):
        self.login_frame.destroy()
        dashboard = DashboardFrame(self)