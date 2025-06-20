class bankSave:
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self.__account_number = 123456 #priv
        self._routing_number = 987654321 #public

    def deposit(self):
        amount = float(input(f"{self.name}, Please enter your deposit amount: "))
        self.current_balance += amount
        print(f"Current Balance: {self.current_balance}")


    def withdraw(self):
        amount = float(input(f"{self.name}, Please enter your withdraw amount: "))
        if self.current_balance - amount < self.minimum_balance:
            print("Sorry, you don't have enough money!")
        else:
            self.current_balance -= amount
            print(f"Current Balance: {self.current_balance}")



    def print_customer_information(self):
        print(f"Name: {self.name}")
        print(f"Current Balance: {self.current_balance}")

#subclasses go below this line
class savAcc(bankSave):

    def interestFee(self):
    #to avoid hardcode, prompt an interest rate
    #then convert to  percent using replace, then back to float for calculations (stack overflow)
        interesting = input(f"{self.name}, what percentage interest rate would you like? ")
        interesting = interesting.replace('%','')
        interesting = float(interesting)
        self.current_balance *= interesting # 2% interest example

class chekAcc(bankSave):

    # class that imposes limits on just how much $ can be transferred
    def transfer(self, targetAcc):
        #limit = 650
        #again instead of hardcode, prompt a transfer limit,do a check, THEN prompt the amount
        limit = float(input(f"{self.name}, Please enter a transfer limit: "))
        if limit>self.current_balance:
            print("Sorry, that limit is too high! brokie!")

        amount = float(input(f"{self.name}, How much would you like to transfer? "))

        if amount > limit:
            print("Transfer exceeds allotted limit!")
        elif self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds!")
        else:
            self.current_balance -= amount
            targetAcc.current_balance += amount
            print(f"Transferred ${amount} to {targetAcc.name}")

class superAcc(savAcc, chekAcc):
    pass