student_dict = {
    "student":["Angela", "James", "Lily"],
    "score":[56, 76 , 98]
}

import pandas
student_df = pandas.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(f"{row.student} {row.score}")