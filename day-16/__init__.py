# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon",["Pikachu", "Dragon", "Fish"])
# table.add_column("Color",["Yellow", "Orrange", "Blue"])
# table.align = "l"
# print(table)

# CoffeMachine
# from menu import Menu, MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
# menu = Menu()
# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
# isDone = True
#
# while isDone == True:
#     choice = input(f"What would you like? {menu.get_items()}")
#     if choice == "off":
#         isDone = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)
#


