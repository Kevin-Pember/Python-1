#Part 1
userInt = int(input("Enter a positive Integer:\n"))
if(userInt % 2 != 0):
    userInt -= 1
sum = 0
for i in range(userInt,1, -2):
    sum += i
print("You even sum is:",sum)
#Part 2
userInt = int(input("Enter a positive Integer:\n"))
maxTable = len(str(userInt * userInt)) + 1
if(userInt < 0):
    print("Error: The number is not positive.")
else:
    print("Multiplication Table for " + str(userInt) +":")
    for i in range(userInt+1):
        if(i == 0):
            print(end=" ")
            i = 1;
        else:
            print(i,end="")
        for j in range(1,userInt+1):
                print(("%"+str(maxTable)+"d") % (j * i),end=" ")
        print("\n")
#Part 3
userInt = int(input("Enter a positive Integer:\n"))
print("")
for i in range(1,userInt + 1):
    for j in range(i):
        print("*",end="")
    print("")
    
