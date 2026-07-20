import requests

class QuizAPI:
    BASE_URL = "https://opentdb.com/api.php"

    def get_questions(self, amount=10):
        params = {
            "amount": amount
        }

        response = requests.get(
            url=self.BASE_URL,
            params=params
        )

        data = response.json()
        return data["results"]

