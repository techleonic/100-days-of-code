import pandas as pd
import matplotlib.pyplot as plt

sets = pd.read_csv('sets.csv')
# print(sets.head())

sets_by_year = sets.groupby('year').count()

# plt.plot(sets_by_year.index,sets_by_year['set_num'])
# plt.show()

# themes by year where theme_id is nunique
theme_by_year = sets.groupby('year').agg({'theme_id':pd.Series.nunique})

# rename columns
theme_by_year.rename(columns= {'theme_id':'nr_themes'}, inplace=True)

# print(type(theme_by_year.index))

# TODO: year between 1949 and 2019
mask = (theme_by_year.index > 1949) & (theme_by_year.index < 2019)
selected = theme_by_year.loc[mask]
print(selected.head())

# print(theme_by_year.head())

new_df =  sets.groupby('year').agg({'num_parts':pd.Series.mean})
print(new_df.head())

plt.scatter(new_df.index[:-2], new_df.num_parts[:-2])
plt.show()