# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 18:17:03 2025

@author: benja
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("csv/YGO TCG Banlist Totals by Type.csv")

plt.figure(figsize=(25, 10), dpi=80)

x=data['List Date']
nor=data['Normal']
eff=data['Effect']
rit=data['Ritual']
fsn=data['Fusion']
syn=data['Synchro']
xyz=data['Xyz']
pnd=data['Pendulum']
lnk=data['Link']
spl=data['Spell']
trp=data['Trap']

plt.plot(x, nor, color='#FDE68A', linewidth=2)
plt.plot(x, eff, color='#A5694A', linewidth=2)
plt.plot(x, rit, color='#2D6BAD', linewidth=2)
plt.plot(x, fsn, color='#674291', linewidth=2)
plt.plot(x, syn, color='#E3E5E0', linewidth=2)
plt.plot(x, xyz, color='#242831', linewidth=2)
plt.plot(x, pnd, color='#017977', linewidth=2)
plt.plot(x, lnk, color='#0067D9', linewidth=2)
plt.plot(x, spl, color='#1D9E74', linewidth=2)
plt.plot(x, trp, color='#A13977', linewidth=2)

plt.title("TCG Banlist Totals by Type", fontsize="25", fontweight='bold')
plt.xlabel('List Date')
plt.ylabel('Number of cards')
plt.legend(['Normal', 'Effect', 'Ritual', 'Fusion', 'Synchro', 'Xyz', 'Pendulum', 'Link', 'Spell', 'Trap'])
ax=plt.gca()
ax.grid(True, color='black', linestyle='-', alpha=0.5)
ax.set_facecolor('#BEBFC5')
ax.set_axisbelow(True)
plt.minorticks_on()
plt.xticks(rotation=45)
plt.tight_layout()
plt.ylim(0, None)
plt.show()