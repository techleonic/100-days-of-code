import pandas as pd

df = pd.read_csv("QueryResults.csv")

print(df.head())
print(df.columns)

# rows and columns
print(df.shape)
print()

#highest total number of posts
print( df.groupby("TagName").sum())

