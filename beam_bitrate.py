# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import math
import scipy.special
import json
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

R = 20
c = 3.0*10**8
f = 2.5*10**9
W = 36*10**6
N = 0.0419
λ = c/f
xc = yc = np.linspace(-1.25, 1.25, 1250)
Xc, Yc = np.meshgrid(xc, yc)
BR = []
mod_rate = []

s = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(Xc ** 2 + Yc **2)))
gc = (2*scipy.special.jv(1, s)/ s) ** 2
log_gc = 10*np.log10(gc)

gn = []
g = []
for i in range(0, 360, 60):
    xa = np.cos(np.radians(i))*0.36
    x = np.linspace(-1.25 + xa, 1.25 + xa, 1250)
    ya = np.sin(np.radians(i))*0.36
    y = np.linspace(-1.25 + ya, 1.25 + ya, 1250)
    X, Y = np.meshgrid(x, y)
    s = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(X ** 2 + Y **2)))
    gn.append((2*scipy.special.jv(1, s)/ s) ** 2)

for i in range(0, 360, 30):
    xa2 = np.cos(np.radians(i))*0.72
    x2 = np.linspace(-1.25 + xa2, 1.25 + xa2, 1250)
    ya2 = np.sin(np.radians(i))*0.72
    y2 = np.linspace(-1.25 + ya2, 1.25 + ya2, 1250)
    X2, Y2 = np.meshgrid(x2, y2)
    s2 = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(X2 ** 2 + Y2 **2)))
    gn.append((2*scipy.special.jv(1, s2)/ s2) ** 2)

    
#g = 10*np.log10(gn[0] + gn[1] + gn[2] + gn[3] + gn[4] + gn[5])
g = (N+gn[0]+gn[1]+gn[2]+gn[3]+gn[4]+gn[5]+gn[6]+gn[7]+gn[8]+gn[9]+gn[10]+gn[11]+gn[12]+gn[13]+gn[14]+gn[15]+gn[16]+gn[17])

F_ue = gc/g
L_ue = 10*np.log10(F_ue)

#ax.plot_surface(Xc, Yc, log_gc, cmap=cm.hsv)
#plt.savefig("receivepower_gc.png")

ax.plot_surface(Xc, Yc, L_ue, cmap=cm.hsv)
plt.savefig("interferencepowerhsv_19.png")

for i in range(len(L_ue)):
    for j in range(len(L_ue)):
        if L_ue[i,j] >= 19.5:
            mod_rate.append(4.5)
        elif 15.8 < L_ue[i,j] < 19.5:
            mod_rate.append(4)
        elif 13.8 < L_ue[i,j] < 15.8:
            mod_rate.append(3.5)
        elif 11.2 < L_ue[i,j] < 13.8:
            mod_rate.append(3)
        elif 10.0 < L_ue[i,j] < 11.2:
            mod_rate.append(2.5)
        elif 7.4 < L_ue[i,j] < 10.0:
            mod_rate.append(2.0)
        elif 5.6 < L_ue[i,j] < 7.4:
            mod_rate.append(1.67)
        elif 4.6 < L_ue[i,j] < 5.6:
            mod_rate.append(1.5)
        elif 2.7 < L_ue[i,j] < 4.6:
            mod_rate.append(1.2)
        elif 1.4 < L_ue[i,j] < 2.7:
            mod_rate.append(1.0)
        else:
            mod_rate.append(0)
            
print(mod_rate[781860])
        
#L_ue_QPSK = L_ue[L_ue[]]

#for i in L_ue:
#    if L_ue[i] >= 4.6:
#      BR[i].append(1.5)
#    elif 1.4 < L_ue[i] < 4.6:
#        BR[i].append(1)
#    elif L_ue[i] 
            
#with open('C:\\Users\ic141\OneDrive\Desktop\専攻科\特別研究\Multibeam_tutolial/frequency_utilization_efficiency.json', 'w') as f:


#ax.plot_surface(Xc, Yc, g, cmap=cm.gist_ncar)
#ax.plot_surface(Xc, Yc, g, cmap=cm.tab20)
#plt.savefig("interferencepower2tab20.png")

