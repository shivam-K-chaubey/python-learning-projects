from ui.app import QuizApp
from database.db_manager import DatabaseManager

db = DatabaseManager()

app = QuizApp(db)
app.mainloop()
