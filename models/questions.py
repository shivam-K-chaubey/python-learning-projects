import html

class Question:

    def __init__(self, text, correct_answer, incorrect_answers):
        self.text = html.unescape(text)
        self.correct_answer = html.unescape(correct_answer)
        self.incorrect_answers = [html.unescape(answer) for answer in incorrect_answers]

