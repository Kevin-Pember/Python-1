#Part 1
# super_bowl_wins = {
#     "1":["Pittsburgh",6],
#     "2":["Dallas", 5],
#     "3":["San Francisco", 5],
#     "4":["Green Bay", 4],
#     "5":["New York", 4],
#     "6":["New England", 3],
#     "7":["Oakland", 3],
#     "8":["Denver", 2],
#     "9":["Miami", 2],
#     }
# def main():
#     running = True
#     while running:
#         print("Super Bowl Wins \n1.Get team by rank\n2.Print all ranks\n3. Exit")
#         print()
#         userIn = input("Enter your choice: ")
#         if(userIn == "1"):
#             userIn = input("What rank do you want (enter int)")
#             if(super_bowl_wins.get(userIn,None) != None):
#                 print("The rank",userIn,"team is",super_bowl_wins[userIn][0], "with", super_bowl_wins[userIn][1],"wins.")
#             else:
#                 print("That rank isn't recorded")
#         elif(userIn == "2"):
#             for key in super_bowl_wins:
#                 print(key,super_bowl_wins[key][0],"with",super_bowl_wins[key][1],"wins")
#         else:
#             running = False
#         print()
# main()
#Part 2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_grade(self):
        return self.grade
    def set_grade(self, grade):
        self.grade = grade
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def birthday(self):
        self.age += 1
    def promote(self):
        self.grade = self.grade + (self.grade * 0.1)
    def display_info(self):
        print(self.name,"is",self.age, "and has a grade of",self.grade)
def main():
    student1 = Student("Alice",15,90.5)
    student1.display_info()
    student1.birthday()
    student1.promote()
    student1.display_info()
main()