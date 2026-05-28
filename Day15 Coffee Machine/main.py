from menu import Menu, MenuItem
from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine

menu = Menu()
money_counter = MoneyMachine()
coffee_machine = CoffeeMachine()

is_cafe_on = True

while is_cafe_on:
    option = menu.get_item()
    choice = input(f"What would you like to order? {option}: ")

    if choice == "off":
        is_cafe_on = False
    elif choice == "report":
        coffee_machine.report()
        money_counter.report()
    else:
        drink = menu.find_item(choice)
        if coffee_machine.is_resource_available(drink):
            money_counter.make_payment(drink.cost)
            coffee_machine.make_coffee(drink)
