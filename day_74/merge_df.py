import pandas as pd
import matplotlib.pyplot as plt


themes =  pd.read_csv('themes.csv')
sets = pd.read_csv('sets.csv')
set_theme_count = sets['theme_id'].value_counts()
sets_count = pd.DataFrame({'id':set_theme_count.index, 'set_count':set_theme_count.values})
merge = pd.merge(sets_count, themes , on='id')

print(themes.head())
print(merge.head())

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merge.name[:10], merge.set_count[:10])
plt.show()