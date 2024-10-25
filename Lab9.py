# #Part 1
# try:
#     balance = 200
#     withdraw = int(input("Enter the amount of money you would like to withdraw: "))
#     if(withdraw > balance):
#         raise ValueError("You don't have enough Money")
#     else :
#         balance -= withdraw
#         print("Remaining Balance:", balance)
# except ValueError as exception:
#     print("Error:",str(exception))
# #Part 2
# try:
#     data = open("data.txt", "r")

#     for i in data:
#         print(i,end="")

#     data.close()
# except FileNotFoundError:
#     print("The file was not found.")
#Part 3
try:
    nums = []
    nums.append(float(input("Enter a number: ")))
    nums.append(float(input("Enter a second number: ") ))
    print("The two added:", (nums[0] + nums[1]))
    print("The two subtracted:", (nums[0] - nums[1]))
    print("The two multiplied:", (nums[0] * nums[1]))
    print("The two divided:", (nums[0] / nums[1]))
except ZeroDivisionError:
    print("Cannot Divide by zero")
except TypeError:
    print("Enter Numbers only")
finally:
    print("All operations complete.")