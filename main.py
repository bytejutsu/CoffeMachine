MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "penny": 0.01
}


def get_report(resources_passed):
    return f"Water: {resources_passed['water']}\nMilk: {resources_passed['milk']}\nCoffee: {resources_passed['coffee']}\nMoney: {resources_passed['money']}"


def turn_off():
    print("turning off the machine...")


def check_if_resources_sufficient(needed_ingredients, available_ingredients):
    for ingredient in needed_ingredients:
        if needed_ingredients[ingredient] > available_ingredients[ingredient]:
            return ingredient
    return None


def process_coins():
    inserted_amount = 0
    for coin in COINS:
        inserted_amount += int(input(f"insert {coin}s: ")) * COINS[coin]
    return inserted_amount


def check_transaction_successful(inserted_amount, cost):
    change = round(inserted_amount - cost, 2)
    if change > 0.00:
        print(f"you get back ${change}")
        return True
    elif change < 0.00:
        print(f"Sorry that\'s not enough money. Money refunded. ${inserted_amount}")
        return False
    else:
        print("you inserted the right amount no change back for you")
        return True


def update_resources(command, resources_passed):
    needed_ingredients = MENU[command]["ingredients"].copy()

    money_cost = MENU[command]["cost"]

    for ingredient in needed_ingredients:
        needed_ingredients[ingredient] = needed_ingredients[ingredient] * -1

    needed_ingredients["money"] = money_cost

    for resource in resources_passed:
        resources_passed[resource] += needed_ingredients[resource]

    return resources_passed


def make_coffee(command, resources_passed):
    updated_resources = update_resources(command, resources_passed)
    print(f"Here is your {command}. Enjoy! ☕")
    return updated_resources


def process_coffee_order(command, resources_passed):
    print(f"processing {command}...")
    needed_ingredients = MENU[command]["ingredients"]
    available_ingredients = {
        "water": resources_passed["water"],
        "milk": resources_passed["milk"],
        "coffee": resources_passed["coffee"]
    }

    missing_ingredient = check_if_resources_sufficient(needed_ingredients, available_ingredients)

    if missing_ingredient:
        print(f"Sorry there is not enough {missing_ingredient}")
    else:
        cost = MENU[command]["cost"]
        inserted_amount = process_coins()
        if check_transaction_successful(inserted_amount, cost):
            resources_passed = make_coffee(command, resources_passed)
    return resources_passed


def display_menu():
    for coffee in MENU:
        print(f"{coffee} : ${MENU[coffee]['cost']} ")


def apply_command(command):
    global resources

    if command == "report":
        print(get_report(resources))
        return True
    elif command == "menu":
        display_menu()
        return True
    elif command in ["espresso", "latte", "cappuccino"]:
        resources = process_coffee_order(command, resources)
        return True
    elif command == "off":
        turn_off()
        return False
    else:
        return True


def main():
    while True:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        action = apply_command(command)

        if not action:
            return


main()
