from budget import Budget

def main():
    food, clothing, entertainment = 0, 0, 0
    budget = Budget(food, clothing, entertainment)
    performOperation = 'Y'
    while (performOperation == 'Y') or (performOperation == 'y'):
        print("What would you like to do?\n")
        print("1. Make deposit\n")
        print("2. Make withdrawals\n")
        print("3. Check balance\n")
        print("4. Transfer inter-budgets\n")
        option = input("Select from the above\n")
        if option == '1':
            amount = int(input("How much would you like to deposit? \n"))
            budget.deposit(amount)
        elif option == '2':
            amount = int(input("How much would you like to withdraw? \n"))
            budget.withdraw(amount)
        elif option == '3':
            budget.balance()
        elif option == '4':
            budget.transferBalance()
        else:
            print("You have entered an invalid input.")
        performOperation = input("Wanna perform another operation? Enter Y for YES or any other character for NO\n")

main()