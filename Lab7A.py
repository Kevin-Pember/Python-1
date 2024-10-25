#Part 1
fibonacci = [0,1,1]
def fibSequence(n):
    for i in range(3,n+1):
        num = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(num)
n = int(input("Enter an N:\n"))
fibSequence(n)
print("Printing Even Numbers")
for i in range(0, len(fibonacci), 3):
    print(fibonacci[i], end=" ")
print()
print("Printing Odd")
for i in range(1, len(fibonacci), 3):
    print(fibonacci[i], end=" ")
    if(i+1 < len(fibonacci)):
        print(fibonacci[i+1], end=" ")
#Part 2
entries = []
userIn = int(input("Enter a number (Enter 0 to stop): "));
mini = userIn;
maxi = userIn;
sumi = 0
while userIn != 0:
    
    if userIn > maxi:
        maxi = userIn;
    elif userIn < mini:
        mini = userIn;
    entries.append(userIn)
    sumi += userIn
    userIn = int(input("Enter a number (Enter 0 to stop): "))
print()
print("[", end=' ')
for i in entries:
    print(i , end=", ")
print("]")
print("Your sum is:",sumi)
print("Your minimum is:",mini)
print("Your maximum is:",maxi)
entries.pop();
print("Modified List is: ",end="")
print("[", end=' ')
for i in entries:
    print(i , end=", ")
print("]")