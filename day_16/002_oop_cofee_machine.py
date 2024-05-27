from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on  =  True
menu =  Menu()
items = menu.get_items()
coffe_maker = CoffeeMaker()
money_machine =  MoneyMachine()
print(items)
while is_on:
    selection = input(f"Select your coffe {items}")
    if  selection == "off":
        is_on = False
    elif selection == "report":
        coffe_maker.report()
        money_machine.report()
    elif selection in items:
        order = menu.find_drink(selection)
        if coffe_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffe_maker.make_coffee(order);
    else:
        print("Invalid selection Enter drink")

