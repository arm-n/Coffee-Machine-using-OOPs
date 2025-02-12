from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_maker = MoneyMachine()
menu=Menu()
is_on=True
while is_on:
    menu_item = str(input("Enter coffee type: 'espresso/latte/cappuccino: ")).lower()
    menu_order=menu.find_drink(menu_item)
    if menu_item == 'report':
        coffee_maker.report()
        money_maker.report()
        continue
    elif menu_item == 'off':
        is_on = False
        continue
    else:
        ingredient = coffee_maker.is_resource_sufficient(menu_order)
        cost = money_maker.make_payment(menu_order.cost)
        if cost == True and ingredient == True:
            coffee = coffee_maker.make_coffee(menu_order)
        else:
            print("Not enough money")






