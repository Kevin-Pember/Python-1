#Part 1 
num = float(input("Enter your grade percentage: \n"))
if num >= 90:
    print("You have an A")
elif num >= 80:
    print("You have a B")
elif num >= 70:
    print("You have a C")
elif num >= 60:
    print("You have a D")
else:
    print("You have a F")
#Part 2
num = int(input("Enter an Integer: \n"))
if (num % 2 == 0):
    print("Your number is even")
else:
    print("Your number is odd")
#Part 3
num = int(input("Enter your Age: \n"))
if num >= 65:
    print("You are a senior")
elif num >= 20:
    print("You are a adult")
elif num >= 13:
    print("You are a teenager")
elif num >= 2:
    print("You are a child")
else:
    print("You are a infant")
