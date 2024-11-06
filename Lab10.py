# #Part 1
def string_list(lis):
    retString = "["
    for i in range(len(lis)):
        if i + 1 == len(lis):
            retString += str(lis[i])+ "]"
        else:
            retString += str(lis[i])+ ", "
    return retString

num_list = [1,3,2,4,53,1,2,4,3,3]
num_list2 = list(set(num_list))
print("Old list",string_list(num_list))
print("New list",string_list(num_list2))
#Part 2
list1 = set(input("Enter elements for list 1 (separated by spaces): ").split())
list2 = set(input("Enter elements for list 2 (separated by spaces): ").split())
print("Common Elements:",list1.intersection(list2))
print("Unique Elements in List 1:",list1.difference(list2))
print("Unique Elements in List 2:", list2.difference(list1))

