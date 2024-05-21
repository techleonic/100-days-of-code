#fuction with output

def format_name (first_name,last_name):
    if first_name == "" or last_name == "":
        return "Your did't provide any valid inputs" # retrun
    first_name = first_name.title() #Upper case frist letter of each word
    last_name = last_name.capitalize() #Upper case first letter of a string
    return f"{first_name} {last_name}"

print(format_name(input("Name"),input("Last Name")))