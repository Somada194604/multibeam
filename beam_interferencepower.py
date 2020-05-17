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
λ = c/f
xc = yc = np.linspace(-1, 1, 1000)
Xc, Yc = np.meshgrid(xc, yc)
BR = []

s = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(Xc ** 2 + Yc **2)))
gc = (2*scipy.special.jv(1, s)/ s) ** 2
log_gc = 10*np.log10(gc)

gn = []
for i in range(0, 360, 60):
    xa = np.cos(np.radians(i))*0.36
    x = np.linspace(-1 + xa, 1 + xa, 1000)
    ya = np.sin(np.radians(i))*0.36
    y = np.linspace(-1 + ya, 1 + ya, 1000)
    X, Y = np.meshgrid(x, y)
    s = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(X ** 2 + Y **2)))
    gn.append((2*scipy.special.jv(1, s)/ s) ** 2)


    
#g = 10*np.log10(gn[0] + gn[1] + gn[2] + gn[3] + gn[4] + gn[5])
g = (gn[0] + gn[1] + gn[2] + gn[3] + gn[4] + gn[5])
F_ue = gc/g
L_ue = 10*np.log10(F_ue)


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

ax.plot_surface(Xc, Yc, log_gc, cmap=cm.hsv)
plt.savefig("receivepower_gc.png")

ax.plot_surface(Xc, Yc, L_ue, cmap=cm.hsv)
plt.savefig("interferencepowerhsv.png")
