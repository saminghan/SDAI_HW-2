import pandas as pd
import numpy as np
df_us = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/USDIDR=X.csv")
df_eu = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/EURIDR=X.csv")
df_jp = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/JPYIDR=X.csv")
df_my = pd.read_csv("E:/AFALL2020/SmartDataAnalityc_I/project/MYRIDR=X.csv")
# slice [start:stop:step], starting from index 5 take every 6th record.
us = df_us.iloc[:,2]
eu = df_eu.iloc[:,2]
jp = df_jp.iloc[93:,2]
my = df_my.iloc[93:,2]
data = np.vstack((us,eu,jp,my)).T
df = pd.DataFrame(data)
df.columns =['USD to IDR', 'EURO to IDR', 'JPY to IDR', 'MYR to IDR']
print(df.tail())

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
fig, axes = plt.subplots(nrows=2, ncols=2, dpi=120, figsize=(10,6))
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