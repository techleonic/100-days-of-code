import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
clean_df = df.dropna()
print(clean_df.columns)

print(clean_df.groupby('Group').count())
print(clean_df[['Starting Median Salary',
       'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
       'Mid-Career 90th Percentile Salary', 'Group']].groupby('Group').mean())