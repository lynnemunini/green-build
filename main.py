import sys
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


report = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
while True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "off":
        break
    elif coffee == "report":
        print(report)
    else:
        def make_coffee(your_coffee):

            if resources["water"] >= MENU[your_coffee]["ingredients"]["water"]:
                if your_coffee == "latte" or your_coffee == "cappuccino":
                    if resources["coffee"] >= MENU[your_coffee]["ingredients"]["coffee"]:
                        if resources["milk"] >= MENU[your_coffee]["ingredients"]["milk"]:
                            print("Please enter coins")
                            quarters = int(input("Quarters: "))
                            dimes = int(input("Dimes: "))
                            nickles = int(input("Nickles: "))
                            pennies = int(input("Pennies: "))

                            # Monetary value
                            quarter = 0.25
                            dime = 0.1
                            nickle = 0.05
                            penny = 0.01
                            total = ((quarter * quarters) + (dime * dimes) + (nickle * nickles) + (penny * pennies))
                        else:
                            print(f"sorry there is not enough {your_coffee} ☕.")
                            sys.exit()
                    else:
                        print(f"sorry there is not enough {your_coffee} ☕.")
                        sys.exit()
                elif your_coffee == "espresso":
                    if resources["coffee"] >= MENU[your_coffee]["ingredients"]["coffee"]:
                        print("Please enter coins")
                        quarters = int(input("Quarters: "))
                        dimes = int(input("Dimes: "))
                        nickles = int(input("Nickles: "))
                        pennies = int(input("Pennies: "))
                        # Monetary value
                        quarter = 0.25
                        dime = 0.1
                        nickle = 0.05
                        penny = 0.01
                        total = ((quarter * quarters) + (dime * dimes) + (nickle * nickles) + (penny * pennies))
                    else:
                        print(f"sorry there is not enough {your_coffee} ☕.")
                        sys.exit()
            else:
                print(f"sorry there is not enough {your_coffee} ☕.")
                sys.exit()

            if total < MENU[your_coffee]["cost"]:
                print("Sorry that's not enough money. Money refunded")
            elif total > MENU[your_coffee]["cost"]:
                change = round((total -(MENU[your_coffee]["cost"])), 2)
                print(f"Here is $ {change} dollars in change.")
                print(f"Enjoy your {your_coffee} ☕")
                for item in MENU[your_coffee]["ingredients"]:
                    resources[item] -= MENU[your_coffee]["ingredients"][item]
                    report[item] = resources[item]
                report["money"] += MENU[your_coffee]["cost"]
            elif total == MENU[your_coffee]["cost"]:
                print(f"Enjoy your {your_coffee} ☕")
                for item in MENU[your_coffee]["ingredients"][item]:
                    resources[item] -= MENU[your_coffee]["ingredients"]
                    report[item] = resources[item]
                report["money"] += MENU[your_coffee]["cost"]
        make_coffee(coffee)


