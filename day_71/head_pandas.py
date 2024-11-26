import pandas as pd

df = pd.read_csv("salaries_by_college_major.csv")
# THE FRIST 5 ROWS
# print(df.head())
# NUMBER OF COLUMNS  AND CELLS
# print(df.shape)
# THE NAME OF THE COLUMNS
# print(df.columns)
# CHECK IS THE LAST FIVE HAVE NON FILL CELLS
# print(df.tail().isna)

# CLEAN THE UN FILL CELLS
clean_df = df.dropna()

# THE COLUMN STRATTING MEDIAN SALARY
print(clean_df["Starting Median Salary"])

# THE MAX STARTING SALARY
print(clean_df["Starting Median Salary"].max())

#GET THE INDEX OF THE MAX
id = clean_df["Starting Median Salary"].idxmax()
print(clean_df.loc[id])

#  major has the highest mid-career salary
id = clean_df["Mid-Career Median Salary"].idxmax()
print(clean_df.loc[id])


