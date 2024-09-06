#Part 1
a = -2
b = 0
print("a =", a, ", b =",b)
print("Sum:",a + b)
print("Difference:",a - b)
print("Product:",a * b)
print("Average:",(a + b)/2)
print("Distance:",abs(a - b))
print("Minimum:",min(a, b))
print("Maximum:",max(a, b))

#Part 2
due = 411
received = 693
balance = received - due
print("Due:",due,"Received:", received)
print(balance//100, "dollar (s)")
balance %= 100
print(balance//25, "quarters (s)")
balance %= 25
print(balance//10, "dime (s)")
balance %= 10
print(balance//5, "nickel (s)")
balance %= 5
print(balance, "pennie (s)")