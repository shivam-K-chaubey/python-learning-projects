from data import orders_requirement, coffee_machine
ingredients = ['milk', 'water', 'coffee']

print(coffee_machine['ingredients'])
print(orders_requirement)

def check(machine, coffee):
    for ingredient in ingredients:
        if machine[ingredient] < coffee[ingredient]:
            return False
    return True

def report(machine):
    for ingredient in ingredients:
        print(f"{ingredient} : {machine['ingredients'][ingredient]}")
    print(f"Money: {machine['money']}")

def insert_coins():
    while True:
        try:
            quarters = int(input("Please insert quarters here: "))
            dimes = int(input("Please insert dimes here: "))
            nickles = int(input("Please insert nickles here: "))
            pennies = int(input("Please insert pennies here: "))
            total_amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            return round(total_amount, 2)
        except ValueError:
            print("Please enter a whole number.")

def update(machine, coffee):
    for  ingredient in ingredients:
        machine['ingredients'][ingredient] -= coffee['ingredients'][ingredient]
    machine['money'] += coffee['price']


def calculate_change(pay, coffee):
    change = round(pay - coffee, 2)
    print(f"Here is your change ${change} and coffee")

coffee_machine_on = True
while coffee_machine_on:
    order = input("What would you like? Espresso, Cappuccino, Latte. ").lower()
    if order not in orders_requirement and order not in ['report', 'off']:
        print("Invalid coffee choice.")
        continue
    if order == 'off':
        coffee_machine_on = False
    elif order == 'report':
        report(coffee_machine)
    else:
        is_material_available = check(coffee_machine['ingredients'], orders_requirement[order]['ingredients'])
        if is_material_available:
            print("All resources are available, please insert the money\n")
            total = insert_coins()
            while True:
                if total >= orders_requirement[order]['price']:
                    calculate_change(total, orders_requirement[order]['price'])
                    update(coffee_machine, orders_requirement[order])
                    break
                else:
                    print("Sorry, not enough money. Money Refunded")
                    break
        else:
            print("For today the material is not available now.Please come tomorrow")
            break