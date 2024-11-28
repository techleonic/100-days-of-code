import matplotlib.pyplot
import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv')
new_df =  df.pivot(index='m', columns='TagName',values=df.columns[2])[:20]
new_df.fillna(0, inplace=True)
# new_df = new_df.rolling(window=6).mean()

"""
TagName              assembly      c      c#    c++  ...  python    r   ruby  swift
m                                                    ...                           
2008-07-01 00:00:00       0.0    0.0     3.0    0.0  ...     0.0  0.0    0.0    0.0
2008-08-01 00:00:00       8.0   85.0   511.0  164.0  ...   124.0  0.0   73.0    0.0
2008-09-01 00:00:00      28.0  321.0  1649.0  755.0  ...   542.0  6.0  290.0    0.0
2008-10-01 00:00:00      15.0  303.0  1989.0  811.0  ...   510.0  0.0  249.0    0.0
2008-11-01 00:00:00      17.0  259.0  1730.0  735.0  ...   452.0  1.0  160.0    0.0

"""

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)

# plt.plot(new_df.index, new_df.java)
# plt.plot(new_df.index, new_df.python)

for column in new_df.columns:
    plt.plot(new_df.index, new_df[column], linewidth=3, label=new_df[column].name)

plt.legend(fontsize=16)
plt.show()