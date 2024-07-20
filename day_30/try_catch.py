
try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["1"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("something")
except
    pass
finally:
    pass