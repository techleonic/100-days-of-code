student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
number_students= len(student_heights)

for student in student_heights:
  total_height += student

print(f"total height = {total_height}")
print(f"number of students = {number_students}")
print(f"average height = {round(total_height/number_students)}")