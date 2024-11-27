import pandas as pd

df = pd.read_csv("QueryResults.csv")
# print(df['m'][1])

print(type(df['m'][1]))

df['date'] = pd.to_datetime(df['m'])
print(df)

print(type(df['date'][0]))