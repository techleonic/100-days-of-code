# number = [1, 2, 3, ]
# new_list = [n + 1 for n in number]
# print(new_list)
#
# name = input("Write your name\n")
# name_list = [letter for letter in name]
# print(name_list)
#
# range_list = [n * 2 for n in range(1, 5)]
# print(range_list)
#
# name = ["Alex", "Beth", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in name if len(name) < 5]
# print(short_names)
# upper_list = [name.upper() for name in name]
# print(upper_list)

#list of squares
# numbers =  [1,1,2,3,5,8,13,21,34,55]
# squared_list = [n*n for n in numbers]
# print(squared_list)
#
# list_of_string = input().split(",")
# list_int = [int(n) for n in list_of_string]
# list_of_eve= [n for n in list_int if n % 2 == 0]
# print(list_of_eve)

with open("file1.txt", mode="r") as file1:
    list1 =  file1.readlines()

with open("file2.txt", mode="r") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]
print(result)