import matplotlib.pyplot
import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv')
new_df =  df.pivot(index='m', columns='TagName',values=df.columns[2]).head()

python_plot = plt.plot(new_df.index, new_df['python'])
plt.xlabel("Date", fontsize=15)
plt.ylabel('Number of posts', fontsize=15)
plt.ylim(0,1500)
plt.show()