# file = open("my_file.txt",)
#
# content = file.read()
#
# print(content)
#
# file.close()
# modes w= write r= read  a= append

#write
with open("my_file.txt",mode="a") as file:
    file.write("\nmy second favorite language is Dart")

#read
with open("C:/Users/LeonidaProgramimg/Desktop/my_file.txt",mode="r") as file:
    content = file.read()
    print(content)

#write create
with open("new_file.txt", mode="w") as file:
    file.write("this is a new file")

