from math import pi
#Part 1 
def calculate_area(radius):
    return pi * radius * radius
def calculate_circumference(radius):
    return 2 * pi * radius
r = float(input("Enter the radius of your circle: "))
print()
print("The area of the circle is:  %.2f" % calculate_area(r))
print("The circumference of the circle is: %.2f" % calculate_circumference(r))
#Part 2
def square_number(num):
    return num ** 2
num = int(input("Enter a number to square: "))
print("The square of",num,"is",square_number(num))
#Part 3
def calculate_area(length, width):
    return length * width
def calculate_perimeter(length, width):
    return 2 * length + 2 * width;
l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))
print()
print("The area of the rectangle is:",calculate_area(l,w))
print("The perimeter of the rectangle is:",calculate_perimeter(l,w))