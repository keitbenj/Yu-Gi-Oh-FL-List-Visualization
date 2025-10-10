# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 18:17:03 2025

@author: benja
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("csv/YGO OCG Banlist Percentages.csv")

plt.figure(figsize=(25, 25), dpi=80)

types = data["Card Type"]
total = data['Total']
ban = data['Forbidden']
limit = data['Limited']
semi = data['Semi-Limited']

bd = []
status_total= np.array([ban, limit, semi])

ban=np.array(ban)
limit=np.array(limit)
semi=np.array(semi)
for i in range(len(ban)):
   bd.append([ban[i], limit[i], semi[i]])
   
bd = [item for sublist in bd for item in sublist]

outer_colors = ['#FDE68A', '#A5694A', '#2D6BAD', '#674291',
          '#E3E5E0', '#242831', '#017977', '#0067D9',
          '#1D9E74', '#A13977']

inner_colors = ['#fd7345', '#fdb245', '#fdd445',
    '#a53525','#a55225','#a56125','#2d3657','#2d5357','#2d6357',
    '#672149','#673349','#673d49','#e37370','#e3b270','#e3d470',
    '#241419','#241f19','#242519','#013d3c', '#015e3c', '#01703c',
    '#00346d','#00506d','#005f6d','#1d4f3a','#1d7a3a','#1d923a',
    '#a11d3c','#a12c3c','#a1353c']

outer_labels = types
inner_labels = ['Forbidden', 'Limited', 'Semi-Limited']

plt.pie(total, labels = types, labeldistance=1.01, colors=outer_colors, 
        startangle=30, radius = 1.2, autopct='%1.1f%%', 
        pctdistance=0.91, wedgeprops={"width": 0.2, "edgecolor":'w'}, 
        textprops={'fontsize': 25, "color": 'w', 'fontweight':'bold'})
plt.legend(prop={'size': 17})

plt.pie(bd, radius = 1, colors = inner_colors, startangle= 30,
        autopct=lambda pct: '{:1.2f}%'.format(pct) if pct > 0 else '', 
        pctdistance=0.9, textprops={'fontsize': 15, "color": 'w', 'fontweight':'bold'}, 
        wedgeprops={"width": 0.2, "edgecolor":'w'},)
plt.title("Yu-Gi-Oh! OCG F/L List History Breakdown", fontsize=50, fontweight='bold')
plt.show()
