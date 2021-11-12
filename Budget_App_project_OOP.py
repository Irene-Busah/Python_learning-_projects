# ------------ TASK 1 ----------------

# Create a Budget class that can instantiate objects based on different budget
# categories like food, clothing, and entertainment. These objects should allow
# for depositing and withdrawing funds from each category, as well computing category
# balances and transferring balance amounts between categories


print()
print("*" * 50)
print("\n 💵 WELCOME TO THE BUDGET APP 💵 \n")
print("*" * 50)


class Budget:
    """Initializing the methods and attributes of the class Budget"""

    def __init__(self, cat_name):
        self.amount = 0
        # os.system('cls')
        self.name = cat_name
        self.balance = 0

    def deposit(self, amount):
        """This method allows depositing funds to each category"""
        self.balance += amount
        return f"Your new balance is ${self.balance} in {self.name} budget"

    def withdraw(self, amount):
        """This method allows withdrawing funds from each category"""

        if self.balance < amount:
            print("************** Transaction failed **************")
            print("\tInsufficient funds")
        else:
            self.balance = self.balance - amount
            results = "************** Transaction Successful **************"
            results += f"\nYour new balance is ${self.balance} in {self.name} budget"
            return results

    @staticmethod
    def check_balance(self):
        """This method allows for computing the balance of each category"""
        balance = f"Your new balance is ${self.balance} in {self.name} budget"
        return balance

    def __str__(self):
        balance = f"Your new balance is ${self.balance} in {self.name} budget"
        return balance

    def transfer(self, amount, category):
        """This method allows for transferring funds between categories"""

        if self.name == category.name:
            result = "ERROR!\n"
            result += "Your cannot transfer funds within the same category. "
            result += "Your can only transfer to other category"
            return result
        else:
            if self.balance < amount:
                print("************** Transaction failed **************")
                print("\tInsufficient funds")
            else:
                self.balance -= amount
                category.balance += amount

                transfer_results = "************** Transaction Successful *******"
                transfer_results += f"Your new balance is ${self.balance} in {self.name} budget"
                transfer_results += f"\nThe balance for {category.name} is ${category.balance}"
                return transfer_results


