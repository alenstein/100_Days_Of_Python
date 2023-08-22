#!/usr/bin/python3
# Day 16 for 100 Days of code challenge - Coffee machine version 2.0

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_status = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_status:
    drinks = menu.get_items()

    drink = input(f"What would you like? ({drinks}): ").lower()

    if drink == 'on':
        machine_status = True
    elif drink == 'off':
        machine_status = False
    elif drink == 'report':
        coffee_maker.report()
        money_machine.report()
    elif drink in drinks:
        order = menu.find_drink(drink)
        sufficient = coffee_maker.is_resource_sufficient(order)
        if sufficient:
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
        else:
            print(f"Sorry can't make {order.name} at the moment!")
    else:
        machine_status = False
        print("ERROR occurred, machine shutting down ....")
