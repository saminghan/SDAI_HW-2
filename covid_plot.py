import pandas as pd
import numpy as np
df_ind = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/covid_ind.csv")
df_may = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/covid_may.csv")
df_jpn = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/covid_jpn.csv")
df_usa = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/covid_usa.csv")
df_fce = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/covid_fce.csv")
# slice [start:stop:step], starting from index 5 take every 6th record.
may= df_may.iloc[:285,5]
jpn = df_jpn.iloc[:285,5]
usa = df_usa.iloc[:285,5]
fce = df_fce.iloc[:285,5]
ind = df_ind.iloc[:,5]
data = np.vstack((may,jpn,usa,fce,ind)).T
df = pd.DataFrame(data)
df.columns =['Malaysia', 'Japan', 'USA', 'France', 'Indonesia']
print(df.tail())

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
fig, axes = plt.subplots(nrows=5, ncols=1, dpi=120, figsize=(10,6))
for i,ax in enumerate(axes.flatten()):
    data = df[df.columns[i]]
    ax.plot(data, color='red', linewidth=1)
    # Decorations
    ax.set_title(df.columns[i])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.spines["top"].set_alpha(0)
    ax.tick_params(labelsize=6)

plt.tight_layout();