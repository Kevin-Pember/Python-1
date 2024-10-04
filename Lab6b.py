#Part 1
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1;
#     else:
#         seq = fibonacci(n - 1) + fibonacci(n - 2)
#         return seq;

# num = int(input("Enter an integer: \n"))
# fib = fibonacci(num);
# if num == 1:
#     print("The %dst Fibonacci number is %d." % (num, fib))
# elif num == 2:
#     print("The %dnd Fibonacci number is %d." % (num, fib))
# elif num == 3:
#     print("The %drd Fibonacci number is %d." % (num, fib))
# else:
#     print("The %dth Fibonacci number is %d." % (num, fib))
#Part 2
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
def main():
    num = int(input("Enter a number: "))
    print("The factorial of %d is %d" % (num, fact(num)))
main()