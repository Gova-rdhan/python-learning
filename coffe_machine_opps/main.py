from menu import Menu, MenuItem
from cofee_maker import CoffeeMaker
from money_machine import MoneyMachine

cofee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
is_on = True
while is_on:
    choice = input("what do you whant latte/espresso/cappuccino: ").lower()
    if choice == 'report':
        cofee.report()
        money.report()
    elif choice == 'off':
        is_on = False
    else:
        if choice in ("latte", "espresso", "cappuccino"):
            item = menu.find_drink(choice)
            if cofee.is_resource_sufficient(item):
                if money.make_payment(item.cost):
                    cofee.make_coffee(item)
        else:
            print("please type the latte or espresso or cappuccino ")




