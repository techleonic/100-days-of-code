import pandas as pd

colors = pd.read_csv('colors.csv')

#first 5 rows
print( colors.head() )

# Unique color count
print(colors['name'].nunique())

#counts each row for is_trans "t"
print(colors.where(colors['is_trans']=='t').count())


#counts the values os the column is_trans
print(colors.is_trans.value_counts())
