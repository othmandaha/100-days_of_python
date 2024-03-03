from os import system
from art import logo
from menu import MENU


def resource_checker(order, resources):
    """
    Checks if resources are enough.
    
    Args:
        order (str): The user's order
        resources (dict): available resources
    Returns:
        0 - if resources are enough.
        1 - otherwise.
    """
    ingredients = MENU[order]['ingredients']
    
    for ingredient, amount in ingredients.items():
        if ingredient in resources and resources[ingredient] < amount:
            return 1
        
    return 0


def resource_manager(order, resources):
    """
    Resource Managment function.

    Args:
        order (str): user's order
        resources (dict): dictionary of available resources
    Returns:
        resources.
    """
    if resource_checker(order, resources) == 1:
        return resources
    else:
        if 'milk' in MENU[order]['ingredients']:
            resources['milk'] -= MENU[order]['ingredients']['milk'] 
        
        resources['water'] -= MENU[order]['ingredients']['water']  
        resources['coffee'] -= MENU[order]['ingredients']['coffee'] 
        resources['money'] += MENU[order]['cost'] 
        return resources


def process_coins(inserted_coins):
    """processes the inserted coins

    Args:
        inserted_coins (dict): the coins the user insert.
    Returns:
        The total in dollar."""
    total = 0
    total += inserted_coins['quarters'] * 0.01
    total += inserted_coins['nickles'] * 0.05
    total += inserted_coins['dimes'] * 0.10
    total += inserted_coins['quarters'] * 0.25
    return total  


def launch():
    """The coffee machine launcher.""" 
    resources = {
        'water': 500,
        'milk': 250,
        'coffee': 150,
        'money': 0.0,
    }
    on = True
    system('cls')
    print(logo)
    while on == True:
        change = 0
        order = input("\tWhat would you like? (espresso/ latte/ cappuccino): ")
        if order == 'off':
            on = False
        elif order == "report":
            print("{}".format(resources))
        elif order in MENU:
            if resource_checker(order, resources) == 1:
                print("Sorry not enough resources!!")
            else:
                inserted_coins = {
                    'quarters': int(input("\nHow many quarters: ")),
                    'nickles': int(input("\nHow many nickles: ")),
                    'dimes': int(input("\nHow may dimes: ")),
                    'pennies': int(input("\nHow many pennies: "))
                }
                total = process_coins(inserted_coins)
                if total < MENU[order]['cost']:
                    print("Sorry that's not enouch money! Money refunded.")
                elif total > MENU[order]['cost']:
                    resources = resource_manager(order, resources)
                    change += round((total - MENU[order]['cost']), 2)
                    print("Here is you {}☕. Enjoy!!".format(order))
                    print(f"here is ${change} in change")

                else:
                    resources = resource_manager(order, resources)
                    print("Here is you {}☕. Enjoy!!".format(order))


if __name__ == "__main__":
    launch()