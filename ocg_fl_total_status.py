# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 17:55:23 2025

@author: benja
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/YGO OCG Banlist Totals by Status.csv")

plt.figure(figsize=(25, 10), dpi=80)

x=data['List Date']
ban = data['Forbidden']
limit = data['Limited']
semi = data['Semi-Limited']

plt.plot(x, ban, color='#FE0000', linewidth=2)
plt.plot(x, limit, color='#FF8C00', linewidth=2)
plt.plot(x, semi, color='#FFD800', linewidth=2)

plt.title("OCG Banlist Totals by Status", fontsize="25", fontweight='bold')
plt.xlabel('List Date')
plt.ylabel('Number of cards')
plt.legend(['Forbidden', 'Limited', 'Semi-Limited'])
ax=plt.gca()
ax.grid(True, color='black', linestyle='-', alpha=0.5)
ax.set_facecolor('#BEBFC5')
ax.set_axisbelow(True)
plt.minorticks_on()
plt.xticks(rotation=45)
plt.tight_layout()
plt.ylim(0, None)
plt.show()