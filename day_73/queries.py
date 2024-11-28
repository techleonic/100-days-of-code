import  pandas as pd
from pandas import DataFrame


df = pd.read_csv('QueryResults.csv')
df['m'] = pd.to_datetime(df['m'])
mask = (df['m'] > '2020-01-01') & (df['m'] <= '2020-12-31')
# print(mask)

new_df = DataFrame(df.loc[mask])
new_df.fillna(0)
new_df.rename({'m': 'date','TagName':'lang', 'Unnamed: 2':'posts'}, axis='columns',inplace=True)
# conver to numeric
new_df['posts'] = pd.to_numeric(new_df['posts'])

print(new_df[['lang','posts']].groupby('lang').sum().sort_values('posts', ascending=False))


# print(type(new_df.columns[2][0]))

# df.groupby('TagName').sum()
# print(df['m'][0])