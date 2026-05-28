class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "milk" :300,
            "water" : 200,
            "coffee" : 100
        }

    def report(self):
        for item in self.resources:
            print(f"{item.title()} : {self.resources[item]}")

    def is_resource_available(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is no {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print("Here is your coffee. Enjoy!")

