
try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    # print(a_dict["1"])
    print(a_dict["key"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("something")
except KeyError as msg_error:
    print(f"that key {msg_error} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    # raise TypeError("This  is an error that i made up")


height = float(input("Height: "))
weight = int(input("weight: "))
if height > 3:
    raise ValueError("Humans are not over 3 meters high")

bmi = weight / (height * height)
print(bmi)