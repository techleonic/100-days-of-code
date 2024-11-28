import pandas as pd

df = pd.read_csv('QueryResults.csv')
print(df.head())

"""
                     m     TagName  Unnamed: 2
0  2008-07-01 00:00:00          c#           3
1  2008-08-01 00:00:00    assembly           8
2  2008-08-01 00:00:00  javascript         162
3  2008-08-01 00:00:00           c          85
4  2008-08-01 00:00:00      python         124
"""

new_df =  df.pivot(index='m', columns='TagName',values=df.columns[2])
print(new_df.head())

"""
TagName              assembly      c      c#    c++  ...  python    r   ruby  swift
m                                                    ...                           
2008-07-01 00:00:00       NaN    NaN     3.0    NaN  ...     NaN  NaN    NaN    NaN
2008-08-01 00:00:00       8.0   85.0   511.0  164.0  ...   124.0  NaN   73.0    NaN
2008-09-01 00:00:00      28.0  321.0  1649.0  755.0  ...   542.0  6.0  290.0    NaN
2008-10-01 00:00:00      15.0  303.0  1989.0  811.0  ...   510.0  NaN  249.0    NaN
2008-11-01 00:00:00      17.0  259.0  1730.0  735.0  ...   452.0  1.0  160.0    NaN
"""

print(new_df.count().head())

"""
TagName
assembly    144
c           144
c#          145
c++         144
delphi      144
dtype: int64
"""

# replace NaN fro 0
print(new_df.fillna(0).head())

"""
TagName              assembly      c      c#    c++  ...  python    r   ruby  swift
m                                                    ...                           
2008-07-01 00:00:00       0.0    0.0     3.0    0.0  ...     0.0  0.0    0.0    0.0
2008-08-01 00:00:00       8.0   85.0   511.0  164.0  ...   124.0  0.0   73.0    0.0
2008-09-01 00:00:00      28.0  321.0  1649.0  755.0  ...   542.0  6.0  290.0    0.0
2008-10-01 00:00:00      15.0  303.0  1989.0  811.0  ...   510.0  0.0  249.0    0.0
2008-11-01 00:00:00      17.0  259.0  1730.0  735.0  ...   452.0  1.0  160.0    0.0
"""

print(new_df.isna().values.any())
"""
[5 rows x 14 columns]
True
"""