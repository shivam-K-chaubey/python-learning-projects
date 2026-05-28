class MenuItem:
    def __init__(self, name, milk, water, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "milk" : milk,
            "water" : water,
            "coffee" : coffee
        }
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", milk=150, water=200, coffee=24, cost=2.5),
            MenuItem(name="espresso", milk=0, water=50, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", milk=50, water=250, coffee=24, cost=3)
        ]
    def get_item(self):
        option = ""
        for item in self.menu:
            option += f"{item.name}/"
        return option

    def find_item(self, choice):
        for item in self.menu:
            if item.name == choice:
                return item
        print(f"Sorry we do not have {choice} in our menu.")
