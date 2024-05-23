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
Profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

is_on = True
profit = 0

def is_resource_sufficient(other_resource):
    for key in other_resource:
        if other_resource[key] > resources[key]:
            print(f"There is not enught{key} ")
            False
        else:
            return True

def process_coins():
    """Ask for user's coins and returns Total"""
    print("insert Coin")
    total =  int(input("How many Quarters ")) *0.05
    total += int(input("How many deimes ")) * 0.1
    total += int(input("How many nickels ")) * 0.05
    total += int(input("How many pennies ")) * 0.01
    return total

def is_transaction_successful(payment,cost):
    if payment >= cost:
        change = round(payment-cost,2)
        print(f"Here is your change: {change}")
        global profit
        profit += cost
        return True
    else:
        print("is not enugh money ")
        return False

def make_coffe(drink_name, other_ingredients):
    """Deduct de resourcess"""
    for item in other_ingredients:
        print( resources[item],other_ingredients[item])
        resources[item]-=other_ingredients[item]
    print(f"Here is your {drink_name} enjoy")

while is_on == True:
    choice = input("What would you like (espresso/latte/cappuccino) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
    elif choice == "profit":
        print(f"Money in this machine : {profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffe(choice, drink["ingredients"])