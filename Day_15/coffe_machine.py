"""Coffee machine program"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    },
}

PROFIT = 0
resourses = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients: list) -> bool:
    """Checks ingredients.

    Args:
        order_ingredients (list): List of ingredients.

    Returns:
        bool: True when order can be made, False if ingredients are insufficient.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resourses[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins() -> float:
    """Returns calculated from coins inserted.

    Returns:
        float: Total coins amount
    """
    print("pleace insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received: float, drink_cost: float) -> bool:
    """_summary_

    Args:
        money_received (float): _description_
        drink_cost (float): _description_

    Returns:
        bool: _description_
    """

    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global PROFIT  # pylint: disable=W0603
        PROFIT += drink_cost
        return True

    print("Sorry that's not enough money. Money refounded.")
    return False


def make_coffee(drink_name: str, order_ingredients: list) -> None:
    """Makes coffee ?)

    Args:
        drink_name (str): _description_
        order_ingredients (list): _description_
    """

    for item in order_ingredients:
        resourses[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


IS_ON = True
while IS_ON:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        IS_ON = False

    elif choice == "report":
        print(
            f"""
              PROFIT: {PROFIT} $
              Water: {resourses['water']} ml
              Milk: {resourses['milk']} ml
              Coffee: {resourses['coffee']} g
              """
        )

    else:
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
