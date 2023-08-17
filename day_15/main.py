#!/usr/bin/python3

import coffee_machine

money = 0.00
ingredients_available = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MENU = coffee_machine.MENU


def pay_for_order(cash=0.0, order=''):
    global money
    money += MENU[order]["cost"]
    cash -= MENU[order]["cost"]
    change = cash
    if change > 0.0:
        print(f"Here is ${change:0.2f} in change.")
        print(f"Here is your {order} 🍵, Enjoy")
    elif change < 0.0:
        print(f"Money not enough for {order}")


def make_latte(pay=0.0):
    resources['water'] -= MENU['latte']['ingredients']['water']
    resources['milk'] -= MENU['latte']['ingredients']['milk']
    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    pay_for_order(pay, 'latte')


def make_cappuccino(pay=0.0):
    resources['water'] -= MENU['cappuccino']['ingredients']['water']
    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
    pay_for_order(pay, 'cappuccino')


def make_espresso(pay=0.0):
    resources['water'] -= MENU['espresso']['ingredients']['water']
    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    pay_for_order(pay, 'espresso')


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['water']}g")
    print(f"Money: ${money:0.2f}")


def resources_available(choice=''):
    if (resources['water'] > MENU[choice]['ingredients']['water']
            and resources['milk'] > MENU[choice]['ingredients']['water']
            and resources['coffee'] > MENU[choice]['ingredients']['water']):
        return True
    else:
        return False


while ingredients_available:
    select = input("What would you like? (espresso/latte/cappuccino): ")
    if select == 'report':
        print_report()
    else:
        ingredients_available = resources_available(select)
        print("Please insert some coins.")
        quaters = int(input("How many quarter?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        money_paid = (quaters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

        if select == 'espresso':
            make_espresso(money_paid)
        elif select == 'latte':
            make_latte(money_paid)
        elif select == 'cappuccino':
            make_cappuccino(money_paid)
        else:
            print("ERROR: invalid menu item")
