class MoneyMachine:
    CURRENCY = "$"

    COINS_VALUE = {
        "quarters" : 0.25,
        "dimes" : 0.10,
        "nickles" : 0.05,
        "pennies" : 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money : {self.CURRENCY}{self.profit}")

    def process_money(self):
        print("Please insert coins.")
        for coin in self.COINS_VALUE:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COINS_VALUE[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process_money()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"here is your change {change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            self.money_received = 0
            print("Sorry, that's not enough money. Money refunded.")
            return False
