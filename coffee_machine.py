class CoffeeMachine:

    def __init__(self, cash, water, milk, beans, cups):
        self.cash = cash
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.choice = None

    def action(self, choice):
        self.choice = choice
        if self.choice == "buy":
            self.buy()
        elif self.choice == "fill":
            self.fill()
        elif self.choice == "take":
            self.take()
        elif self.choice == "remaining":
            self.print_supply()
        elif self.choice == "exit":
            return 1
        else:
            ...

    def print_supply(self):
        print("The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.beans} of coffee beans\n"
              f"{self.cups} of disposable cups\n"
              f"${self.cash} of money")

    def check_supply(self, water_cost, milk_cost, beans_cost, cups_cost):
        if self.water < water_cost:
            print("Sorry, not enough water!")
        elif self.milk < milk_cost:
            print("Sorry, not enough milk!")
        elif self.beans < beans_cost:
            print("Sorry, not enough coffee beans!")
        elif self.cups < cups_cost:
            print("Sorry, not enough cups!")
        else:
            return 1

    def espresso(self):
        water_cost, milk_cost, beans_cost, cups_cost, price = 250, 0, 16, 1, 4
        if self.check_supply(water_cost, milk_cost, beans_cost, cups_cost):
            print("I have enough resources, making you a coffee!")
            self.water -= water_cost
            self.beans -= beans_cost
            self.cups -= cups_cost
            self.cash += price

    def latte(self):
        water_cost, milk_cost, beans_cost, cups_cost, price = 350, 75, 20, 1, 7
        if self.check_supply(water_cost, milk_cost, beans_cost, cups_cost):
            print("I have enough resources, making you a coffee!")
            self.water -= water_cost
            self.milk -= milk_cost
            self.beans -= beans_cost
            self.cups -= cups_cost
            self.cash += price

    def cappuccino(self):
        water_cost, milk_cost, beans_cost, cups_cost, price = 200, 100, 12, 1, 6
        if self.check_supply(water_cost, milk_cost, beans_cost, cups_cost):
            print("I have enough resources, making you a coffee!")
            self.water -= water_cost
            self.milk -= milk_cost
            self.beans -= beans_cost
            self.cups -= cups_cost
            self.cash += price

    def buy(self):
        caffe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if caffe == "back":
            ...
        elif int(caffe) == 1:
            self.espresso()
        elif int(caffe) == 2:
            self.latte()
        elif int(caffe) == 3:
            self.cappuccino()
        else:
            ...

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.cash}")
        self.cash = 0

    def start(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            if self.action(input()):
                break


CoffeeMachine(550, 400, 540, 120, 9).start()
