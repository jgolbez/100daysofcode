import sys

'''
We track 3 data stores in this program:
MENU which includes ingredients and cost to dispense
RESOURCES which keeps track of how many resources the machine can use to dispense
CASH which keeeps track of how much money has been accepted by the machine (not counting overpayment returned)
'''
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

cash = 0.0
paid = False
'''
Function Definitions



Count each coin and calculate value, return total paid to check against order cost
'''
def input_payment():
    print("Please insert coins.")
    q_num = int(input("How many quarters? "))
    d_num = int(input("How many dimes? "))
    n_num = int(input("How many nickels? "))
    p_num = int(input("How many pennies? "))
    q_sum = q_num * 0.25
    d_sum = d_num * 0.10
    n_sum = n_num * 0.05
    p_sum = p_num * 0.01
    total_paid = round(q_sum + d_sum + n_sum + p_sum, 2)
    return total_paid

'''
For each ingredient, check the entered order ingredients needed against machine resources, keep track if any ingredients are out (show False)
When check of all ingredients is completed return value whether drink can be dispensed (T/F value)
'''
def check_resources(order):
    if order in MENU:
        can_make = []
        for k, v in MENU[order]['ingredients'].items():
            can_make.append(v < resources[k])
        return (False not in can_make)


'''
Take in total payment and compare to cost. If the cost exceeds the payment we cancel the payment and do not take any money
If the payment is sufficient we deduct the cost of the order and return any extra, then update the cash in the machine
'''
def resolve_payment(order, money_paid):
    global cash
    if MENU[order]['cost'] <= money_paid:
        change = round(money_paid - MENU[order]['cost'], 2)
        if change > 0:
            changestr = "{:.2f}".format(change)
            print(f"Here is ${changestr} in change")
        cash += MENU[order]['cost']
        return True
    else:
        money_paidstr = "{:.2f}".format(money_paid)
        print(f"There are insufficient funds to order, refunding ${money_paidstr}")


'''
Deduct resources from the machine after verifying we have enough to dispense and also enough money was provided
'''
def dispense_coffee(order):
    for k in MENU[order]['ingredients'].keys():
        resources[k] -= MENU[order]['ingredients'][k]
    print(f"Here is your {order}. Enjoy!")


'''
MAIN PROGRAM
'''
while True:
    user_choice = input("What would you like? ").lower()
    if user_choice == "off":
        sys.exit()
    elif user_choice == "report":
        for k, v in resources.items():
            if k == 'water' or k == 'milk':
                print(f"{k.title()}: {str(v) + 'ml'}")
            elif k == 'coffee':
                print(f"{k.title()}: {str(v) + 'g'}")
        cashstr = "{:.2f}".format(cash)
        print(f"Money: ${cashstr}")
    elif user_choice in MENU:
        can_make_coffee = check_resources(user_choice)
        if can_make_coffee:
            total_paid = input_payment()
            paid = resolve_payment(user_choice, total_paid)
            if paid:
                dispense_coffee(user_choice)
        else:
            print(f"There are insufficient resources to make {user_choice}, please turn 'off' machine and call for service")
