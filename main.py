# CLASS

class CoffeeMachine:

    def __init__(self, water, milk, beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = None

    # CURRENT STATE

    def current_state(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            self.state = input()
            if self.state == "buy":
                    self.buy_operation()
            elif self.state == "fill":
                    self.fill_operation()
            elif self.state == "take":
                    self.take_operation()
            elif self.state == "remaining":
                    self.display_ingredients()
            elif self.state == "exit":
                exit()
            else:
                print("Wrong action, try again.")

    # DISPLAY RESOURCES

    def display_ingredients(self):
        print("The coffee machine has:\n",
              self.water, "of water\n",
              self.milk, "of milk\n",
              self.beans, "of coffee beans\n",
              self.disposable_cups, "of disposable cups\n",
              self.money, "of money\n"
              )

    # BUYING OPERATION

    def buy_operation(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu")
        coffee = input()
        coffee = self.enough_resources(coffee)
        if coffee == '1':
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.disposable_cups -= 1
        elif coffee == '2':
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.disposable_cups -= 1
        elif coffee == '3':
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.disposable_cups -= 1

    # ENOUGH RESOURCES

    def enough_resources(self, coffee_type):
        if coffee_type == '1':
            if self.water - 250 < 0:
                print("Sorry, not enough water!")
                return 'back'
            elif self.beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
                return 'back'
            else:
                print("I have enough resources, making you a coffee!")
                return coffee_type
        elif coffee_type == '2':
            if self.water - 350 < 0:
                print("Sorry, not enough water!")
                return 'back'
            elif self.beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
                return 'back'
            elif self.milk - 75 < 0:
                print("Sorry, not enough milk!")
                return 'back'
            else:
                print("I have enough resources, making you a coffee!")
                return coffee_type
        elif coffee_type == '3':
            if self.water - 200 < 0:
                print("Sorry, not enough water!")
                return 'back'
            elif self.beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
                return 'back'
            elif self.milk - 100 < 0:
                print("Sorry, not enough milk!")
                return 'back'
            else:
                print("I have enough resources, making you a coffee!")
                return coffee_type

    # FILL MACHINE OPERATION

    def fill_operation(self):

        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    # WITHDRAWING INFORMATION

    def take_operation(self):
        print("I gave you $", self.money)
        self.money = 0


# STARTING RESOURCES

init_water, init_milk, init_beans, init_disposable_cups, init_money = 400, 540, 120, 9, 550

# MAIN BODY

coffee_example = CoffeeMachine(init_water, init_milk, init_beans, init_disposable_cups, init_money)
coffee_example.current_state()