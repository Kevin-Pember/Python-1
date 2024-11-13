#Part 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def get_width(self):
#         return self.width
#     def set_width(self, newWidth):
#         self.width = newWidth
#     def get_height(self):
#         return self.height
#     def set_height(self, newHeight):
#         self.height = newHeight
#     def calculate_area(self):
#         return self.width * self.height

# def main():
#     rec1 = Rectangle(4,5)
#     rec2 = Rectangle(3,4)
#     print("Rectangle 1's area is",rec1.calculate_area(), ". And Rectangle 2's area is",rec2.calculate_area())
#     rec1.set_height(6)
#     rec2.set_width(4)
#     print("Rectangle 1's new height is",rec1.get_height(), "and Rectangle 2's new width is", rec2.get_width())
#     print("Changing their area's to",rec1.calculate_area(),"and",rec2.calculate_area(),"respectively.")
# main()
#Part 2
import random
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def get_account_num(self):
        return self.__account_number
    def set_account_num(self, newNum):
        self.__account_number = newNum
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        return amount
    def withdraw(self, amount):
        self.__balance -= amount
        return amount
def main():
    
    account1 = BankAccount(random.randint(1000,9999), 6000)
    account2 = BankAccount(random.randint(1000,9999), 3230)
    print("Account 1 has the number", account1.get_account_num(),", it has the balance",account1.get_balance())
    print("Account 2 has the number", account2.get_account_num(),", it has the balance",account2.get_balance())
    account2.deposit(account1.withdraw(1000))
    print("Account 1 pays Account 2 Leaving them with the balances of",account1.get_balance(), "and", account2.get_balance(), "respectively.")
main()