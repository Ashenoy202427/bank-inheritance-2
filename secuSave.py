class BankSave:
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
my_account= BankSave("Alan", 1000, 500)
my_account.deposit()
my_account.withdraw()
