#Part 1
# import math
# class Shape:
#     def __init__(self, name):
#         self.name = name if name != None else "Generic"
#     def area(self):
#         return 0
# class Rectangle(Shape):

#     def __init__(self,length, width):
#         super().__init__("Rectangle")
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
#     def get_width(self):
#         return self.width
#     def set_width(self, newWidth):
#         self.width = newWidth
#     def get_height(self):
#         return self.height
#     def set_height(self, newHeight):
#         self.height = newHeight
# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__("Circle")
#         self.radius = radius
#     def area(self):
#         return math.pi * math.pow(self.radius,2)
#     def get_radius(self):
#         return self.radius
#     def set_radius(self, radius):
#         self.radius = radius

# def main():
#     circle1 = Circle(float(input("Enter a number for your radius (float): ")))
#     rectangle1 = Rectangle(float(input("Enter a number for your length (float): ")),float(input("Enter a number for your width (float): ")))

#     print("Circle Area:", circle1.area())
#     print("Rectangle Area", rectangle1.area())
# main()

#Part 2
class Vehicle:
    def __init__(self, type):
        self.type = type if type != None else "Vehicle"
    def info(self):
        print(self.type+":", end=" ")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__("Car")
        self.make = make
        self.model = model
    def info(self):
        super().info()
        print(self.make, self.model)

class Motorcycle(Vehicle):
    def __init__(self, make):
        super().__init__("Motorcycle")
        self.make = make
    def info(self):
        super().info()
        print(self.make)
def main():
    car1 = Car("Honda", "Pilot")
    cycle1 = Motorcycle("Harley Davidson")
    car1.info()
    cycle1.info()
main()
