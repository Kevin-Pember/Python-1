#Part 1
password = input("Enter a Password: \n")
count = 0
if(len(password) >= 8):
    count += 1
if(not any(n.islower() for n in password)):
    count -= 1
elif(not any(n.isupper() for n in password)):
    count -= 1
if(any(n.isnumeric() for n in password)):
    count += 1
if(password.find("!") or password.find("@") or password.find("#") or password.find("$")):
    count += 1
if(count >= 3 ):
    print("Strong")
elif(count > 0):
    print("Moderate")
else:
    print("Weak")

#Part 2
# email = input("Enter your email: \n")
# atIndex = email.find("@")
# dotIndex = email.find(".")
# isSpace = (not " " in email)
# if(email != -1 and atIndex < dotIndex and isSpace):
#     print("Valid Email")
# else:
#     print("Invalid Email")