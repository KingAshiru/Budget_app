class Budget:
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment

    def deposit(self, amount):
        print("What category do you want to deposite into? \n")
        print("1. Food\n")
        print("2. Clothing\n")
        print("3. Entertainment\n")
        category = input("Select one from the options above\n")
        if category == '1':
            self.food += amount
            print("You have just deposited " + str(amount) + " into the food category")
        elif category == '2':
            self.clothing += amount
            print("You have just deposited " + str(amount) + " into the clothing category")
        elif category == '3':
            self.entertainment += amount
            print("You have just deposited " + str(amount) + " into the entertainment category")
        else:
            print("The category you selected does not exist.")
        return

    def withdraw(self, amount):
        print("What category do you want to withdraw from? \n")
        print("1. Food\n")
        print("2. Clothing\n")
        print("3. Entertainment\n")
        category = input("Select one from the options above\n")
        if category == '1':
            self.food -= amount
            print("You have just withdrew " + str(amount) + " from the food category")
        elif category == '2':
            self.clothing -= amount
            print("You have just withdrew " + str(amount) + " from the clothing category")
        elif category == '3':
            self.entertainment -= amount
            print("You have just withdrew " + str(amount) + " from the entertainment category")
        else:
            print("The category you selected does not exist.")
        return
    
    def balance(self):
        print("Your balance for food category is " + str(self.food))
        print("Your balance for clothing category is " + str(self.clothing))
        print("Your balance for entertainment category is " + str(self.entertainment))
        return 

    def transferBalance(self):
        amount = int(input("How much do you want to transfer? \n"))
        self.withdraw(amount)
        self.deposit(amount)
        return
    


