# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import math
import scipy.special
import numpy as np
import matplotlib.pyplot as plt

R = 20
c = 3.0*10**8
f = 2.5*10**9
λ = c/f

def beam_param(rad):
    y = []
    for i in [k/100 for k in range(0,2600)]:
        if rad+i == 0.0:
            continue
        x = (math.pi*R)/λ*math.sin(math.radians(rad+i))
        y.append((2*scipy.special.jv(1,x)/x)**2)
    return y
    

plt.plot([i/18 - 5.55555 for i in range(200)], beam_param(-13)[1200:1400])
plt.plot([-5, 5], [math.log10(0.001), math.log10(0.001)], "red", linestyle="dashed")
plt.show()