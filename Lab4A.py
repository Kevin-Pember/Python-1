#Part 1
userIn = float(input("Enter a number:\n"))
sum = 0
count = 0
while userIn >= 0:
    sum += userIn
    count += 1
    userIn = float(input("Enter a number, enter a negative to end:\n"))
print("Your Average is:", (sum / count))
#Part 2
# userIn = float(input("Enter a number:\n"))
# min = userIn
# while userIn >= 0:
#     if(userIn < min):
#         min = userIn
#     userIn = float(input("Enter a number, enter a negative to end:\n"))
# print("You minimum is:",min)