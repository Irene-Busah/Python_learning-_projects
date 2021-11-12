from Budget_App_project_OOP import *

print("Create an account")
username = input("Enter username: ")
password = input("Enter a password(8 character): ")
print("\n-------------------- Account created successfully ----------------------")
print("\nLogin now!\n")
username2 = input("Enter your username: ")
password2 = input("Enter your password: ")
if len(password2) >= 8:
    if username == username2 and password == password2:
        print("\n------------- Logged in successfully ------------------\n")
    else:
        print("Invalid Credential")
        quit()
else:
    print("Wrong password")
    quit()


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")
print("\nWhat would you like to do?")
answer = int(input("1. Deposit\n2. Withdraw\n3. Transfer: "))

if answer == 1:
    # Testing the deposit method in the Budget class
    print("Which category would you like to deposit the funds?")
    ans = int(input("1. Food\n2. Clothing\n3. Entertainment: "))
    if ans == 1:
        amount_deposit = int(input("Enter the amount of funds you want to deposit for food($): "))
        print(food.deposit(amount=amount_deposit))
        print("\n========================== Thank you ============================\n")

    elif ans == 2:
        amount_deposit = int(input("Enter the amount of funds you want to deposit for clothing($): "))
        print(clothing.deposit(amount=amount_deposit))
        print("\n========================== Thank you ============================\n")

    elif ans == 3:
        amount_deposit = int(input("Enter the amount of funds you want to deposit for entertainment($): "))
        print(entertainment.deposit(amount=amount_deposit))
        print("\n========================== Thank you ============================\n")


elif answer == 2:
    # Testing the withdraw method in the budget class
    print("Which category would you like to withdraw the funds?")
    ans = int(input("1. Food\n2. Clothing\n3. Entertainment: "))
    if ans == 1:
        amount_withdraw = int(input("Enter the amount of funds you want to withdraw from food budget($): "))
        print(food.withdraw(amount=amount_withdraw))
        print("\n========================== Thank you ============================\n")
        # print(food.check_balance())
    elif ans == 2:
        amount_withdraw = int(input("Enter the amount of funds you want to withdraw from clothing budget($): "))
        print(clothing.withdraw(amount=amount_withdraw))
        print("\n========================== Thank you ============================\n")
        # print(food.check_balance())
    elif ans == 3:
        amount_withdraw = int(input("Enter the amount of funds you want to withdraw from entertainment budget($): "))
        print(entertainment.withdraw(amount=amount_withdraw))
        print("\n========================== Thank you ============================\n")
        # print(food.check_balance())


elif answer == 3:
    # Testing the transfer method in the budget class
    amount_transfer = int(input("Enter the amount of funds you want to transfer($): "))
    print("Which category would like to transfer from?")
    option = int(input("1. Food to clothing\n2. Food to Entertainment\n3. Clothing to Food\n4. Clothing to "
                       "Entertainment\n5. Entertainment to Food\n6. Entertainment to Clothing: "))

    if option == 1:
        print(food.transfer(amount_transfer, clothing))
        print("\n========================== Thank you ============================\n")
    elif option == 2:
        print(food.transfer(amount_transfer, entertainment))
        print("\n========================== Thank you ============================\n")
    elif option == 3:
        print(clothing.transfer(amount_transfer, food))
        print("\n========================== Thank you ============================\n")
    elif option == 4:
        print(clothing.transfer(amount_transfer, entertainment))
        print("\n========================== Thank you ============================\n")
    elif option == 5:
        print(entertainment.transfer(amount_transfer, food))
        print("\n========================== Thank you ============================\n")
    elif option == 6:
        print(entertainment.transfer(amount_transfer, clothing))
        print("\n========================== Thank you ============================\n")

