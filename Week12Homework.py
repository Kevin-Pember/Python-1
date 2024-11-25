# # Part 1
# class Library:
#     def __init__(self, name = "", location = "", max_capacity = 0, books = []):
#         self.name = name
#         self.location = location
#         self.max_capacity = max_capacity
#         self.books = books
#     def set_name(self, name):
#         self.name = name
#     def set_location(self,location):
#         self.location = location
#     def set_capacity(self, cap):
#         self.max_capacity = cap
#     def add_book(self, book):
#         if self.max_capacity > len(self.books):
#             self.books.append(book)
#             print("Book",book,"added to the library.")
#         else:
#             print("Error: books at Capacity")
#     def remove_book(self, book):
#         try:
#             self.books.remove(book)
#             print("Book",book,"removed from the library.")
#         except ValueError:
#             print("Book not in Library")
#     def display_books(self):
#         print("Books in library:")
#         for book in self.books:
#             print("-",book)

# def main():
#     occLibrary = Library("OCC Library", "Orange Coast College", 2)
#     running = True
#     while running:
#         print("Library Management System: \n1. Add a book\n2. Remove a book\n3. Display all books\n4.Exit\n")
#         userIn = input("Enter your choice (1-4): ")

#         if userIn == "1":
#             occLibrary.add_book(input("Enter the name of the book you want to add: "))
#         elif userIn == "2":
#             occLibrary.remove_book(input("Enter the name of the book you want to remove: "))
#         elif userIn == "3":
#             occLibrary.display_books()
#         elif userIn == "4":
#             running = False
# main()
            
#Part 2
class FinanceTracker:
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.account_balance = float(balance)
        self.transactions = []
    def add_transaction(self,description, amount):
        self.account_balance += amount
        self.transactions.append([description,amount])
    def display_balance(self):
        print("Current Account Balance: %.2f \n" % self.account_balance)
    def display_transactions(self):
        print("Transaction History")
        for i in range(len(self.transactions)):
            print(str(i + 1)+".", self.transactions[i][0]+":",("+" if self.transactions[i][1] > 0 else "") + "%.2f" % self.transactions[i][1])
        print()

def main():
        finTrack = FinanceTracker("Jerry", 3000.00)
        running = True
        while running:
            print("Personal Finance Tracker"+
              "\n1. Add a new transaction"+
              "\n2. Display account balance"+
              "\n3. Display all transactions"+
              "\n4. Exit\n")
            userIn = input("Enter your choice (1-4): ")
            if userIn == "1":
                finTrack.add_transaction(input("Enter transaction description: "), float(input("Enter transaction amount: ")))
            elif userIn == "2":
                 finTrack.display_balance()
            elif userIn == "3":
                 finTrack.display_transactions()
            elif userIn == "4":
                 print("Exiting the Personal Finance Tracker. Goodbye!")
                 running = False
        
        
main()