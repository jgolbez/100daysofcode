from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cmenu = Menu()
cmaker = CoffeeMaker()
mmachine = MoneyMachine()
isOn = True

#TODO Print Menu/Take Order
while isOn:
    order = input(f"What would you like? {cmenu.get_items()}").lower()
    if order == "off":
        isOn = False
        print("Shutting down.")
    elif order == "report":
        cmaker.report()
        mmachine.report()
    elif order in cmenu.get_items():
        orderitem = cmenu.find_drink(order)
        if cmaker.is_resource_sufficient(orderitem):
            paid = mmachine.make_payment(orderitem.cost)
            if paid:
                cmaker.make_coffee(orderitem)
    else:
        print("That is not a valid choice")