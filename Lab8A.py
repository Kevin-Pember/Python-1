#Part 1
# def get_student_details():
#     fName = input("Enter your first name: ")
#     lName = input("Enter your last name: ")
#     studentID = input("Enter your student ID: ")
#     return(fName,lName,studentID)
# prime_numbers = (2,3,5,7,11)
# print("Second prime number is:",prime_numbers[2])
# print("Error: states that tuple object doesn't support Item assignment")
# studentInfo = get_student_details();
# print("Student Details: (", end="")
# for i in studentInfo:
#     print(i,end=", ")
# print(")")
#Part 2
medal_table = [
    ["USA", 3,2,1],
    ["China", 2, 1, 0],
    ["Japan", 1,0,1]
]
def total_medals(index):
    count = 0;
    for i in range(1,len(medal_table[index])):
        count += medal_table[index][i]
    return count

print("Total medals for the USA:",total_medals(0))
print("Total medals for the China:",total_medals(1))