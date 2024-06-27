#
# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
# print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")

print(type(data))
print(type(data["temp"]))
print("\n")

data_dict =  data.to_dict()
print(data_dict)
print("\n")

temp_list = data["temp"].to_list()
print(temp_list)
print("\n")

average = data["temp"].mean()
print(average)
print("\n")

print(data["temp"].max())
print("\n")

print(data["condition"])
print(data.condition)

#get row
print(data[data.day == "Monday"])

#get max temperature row
print(data[data.temp == data.temp.max()])


#celcius convert
monday = data[data.day == "Monday"]
print(monday.condition)
temp = (int(monday.temp[0]))
temp =temp *33.8
print(temp)


#create data frame
data_dict = pandas.DataFrame(data_dict)
print(data_dict)
data_dict.to_csv("new_data.csv")