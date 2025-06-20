class bankSave:
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self):
        amount = float(input("Please enter your deposit amount: "))
        self.current_balance += amount
        print(f"Current Balance: {self.current_balance}")


    def withdraw(self):
        amount = float(input("Please enter your withdraw amount: "))
        if self.current_balance - amount < self.minimum_balance:
            print("Sorry, you don't have enough money!")
        else:
            self.current_balance -= amount
            print(f"Current Balance: {self.current_balance}")



    def print_customer_information(self):
        print(f"Name: {self.name}")
        print(f"Current Balance: {self.current_balance}")

print("Welcome to SecuSave credit union!!")
my_account= bankSave("Alan", 1000, 500)

class savAcc(bankSave):

    def interestFee(self):
        self.current_balance *= 1.02 # 2% interest example

class chekAcc(bankSave):
    # class that imposes limits on just how much $ can be transferred
    def transfer(self, targetAcc):
        limit = 650
        amount = float(input("How much would you like to transfer? "))

        if amount > limit:
            print("Transfer exceeds allotted limit!")
        elif self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds!")
        else:
            self.current_balance -= amount
            targetAcc.current_balance += amount
            print(f"Transferred ${amount} to ${targetAcc.name}")
