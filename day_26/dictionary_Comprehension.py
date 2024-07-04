# new_dict ={new_key:new_value for (key,value) in dict.items() if test}
# import random
# name = ["Alex", "Beth", "Dave", "Eleanor", "Freddie"]
#
# students_score = {student:random.randint(1,100)  for student in name}
# print(students_score)
#
# passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
# print(passed_students)

# sentence =  input().split(" ")
# print(sentence)
# dict_letters ={word:len(word) for word in sentence}
# print(dict_letters)

weather_c =  eval(input())
print(type(weather_c))
weather_f = {day:(temp*9/5)+32 for (day, temp) in weather_c.items()}
print(weather_f)