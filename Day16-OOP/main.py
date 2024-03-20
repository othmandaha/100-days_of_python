from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system


menu = Menu()
coffee_maker = CoffeeMaker()
moneyMachine = MoneyMachine()

off = False

while off != True:
    # system('cls')
    prompt = input("What would you like? {}:".format(menu.get_items()))
    if prompt == 'off':
        off = True
        break
    elif prompt == 'report':
        coffee_maker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(prompt)
        if drink == False:
            break
        else:
            if coffee_maker.is_resource_sufficient(drink) == False:
                break

            if moneyMachine.make_payment(drink.cost) == False:
                break

            coffee_maker.make_coffee(drink)

