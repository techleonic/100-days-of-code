import pandas as pd

df =  pd.read_csv('sets.csv')


#oldest leago set

print(df.sort_values("year").head())

#newest
print(df.sort_values("year", ascending=False).head())

#high part number
print(df.sort_values('num_parts', ascending=False).head())


