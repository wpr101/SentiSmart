import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
from ggplot import *
from matplotlib import *


with open('Jan17EarningsData.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content] 

grouped_stocks = []
for line in content:
    symbol, release, EstEPS, ActualEPS = tuple(line.split(' '))
    grouped_stocks.append(( symbol, release, EstEPS, ActualEPS))

df = pd.DataFrame(grouped_stocks, columns=['Symbol', 'Release', 'EstEPS', 'ActualEPS'])
symbol_list = df['Symbol'].tolist()

df1 = df[['EstEPS', 'ActualEPS']]
df1 = df1.astype(float)
#sorted_actualEPS = df1.sort_values('ActualEPS')
#print(sorted_actualEPS.head())

ax = df1[['EstEPS','ActualEPS']].plot(kind='bar', title ="Jan17 Earnings", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Companies", fontsize=12)
ax.set_ylabel("Earnings Per Share", fontsize=12)
ax.set_xticklabels(symbol_list)
plt.show()
