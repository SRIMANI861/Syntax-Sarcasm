"""
Encapsulation: Bundling the data ( attributes and methods ) together with in a class and restricting the direct access
to the people to protect the data.
"""

"""
If a variable has __(variable_name)__ then they are called as 'Special Methods'

If a variable has _ or __ at starting then they are called as 'Private variables', these cannot be accessed outside the classes.

"""

class BankAccount:
    def __init__(self,balance):
        """
        self.balance means that self means it is pointing to current object and balance is a variable, and balance is user input which is on the right side.
        Whenever a user enters the balance, that balance gets stored in the object variable which is self.balance
        """
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
    def getBalance(self):
        print(self.__balance)

class Customer:
    def __init__(self,name,account):
        self.name = name
        self.account = account
    def check_balance(self):
        print(self.account.getBalance())
    def depositMoney(self,amount):
        self.account.deposit(amount)
        print(f"{self.name} deposited {self.amount}")

account = BankAccount(5000)
customer1 = Customer("Srimani")
customer1.check_balance()
customer1.depositMoney(1000)