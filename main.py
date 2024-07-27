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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit=0
def resources_sufficient(order):
    for item in order:
        if order[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def count_money():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def payment_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def prepare_order(drink,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink}. Enjoy!!")

off=False
while not off:
    choice = input("What would you like?, Type 'espresso'.'latte' or  'cappuccino'.").lower()
    report=input("Type 'yes' to generate report, else 'no'.")
    if choice=="off":
        off=True
    elif report=='yes':
        for i in resources:
            print(i,resources[i])
    else:
        drink=MENU[choice]
        x=drink["cost"]
        print(f"Total is ${x}")
        if resources_sufficient(drink["ingredients"]):
            pay=count_money()
            if payment_successful(pay,x):
                prepare_order(choice,drink["ingredients"])

