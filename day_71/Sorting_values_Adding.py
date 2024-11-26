import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
clean_df =  df.dropna()

print(df.columns)

print(clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"])
# clean_df["Mid-Career 90th Percentile Salary"].substract(clean_df["Mid-Career 10th Percentile Salary"])

spread_col =  clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]

clean_df.insert(1, "spread",spread_col)

print(clean_df.head())

low_risk =  clean_df.sort_values('spread')
print(low_risk[['Undergraduate Major','spread']].head())

highest_potencial = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potencial[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head())