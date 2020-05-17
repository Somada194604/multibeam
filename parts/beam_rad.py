import math
import scipy.special
import numpy as np
import matplotlib.pyplot as plt

R = 20
c = 3.0*10**8
f = 2.5*10**9
λ = c/f

def beam_rad(rad):
    y = []
    for i in [k/100 for k in range(0,2600)]:
        if rad+i == 0.0:
            continue
        x = (math.pi*R)/λ*math.sin(math.radians(rad+i))
        y.append(10*math.log10((2*scipy.special.jv(1,x)/x)**2))
        if round((2*scipy.special.jv(1,x)/x)**2*2, 1) == 1:
            rad_3db = round(rad+i, 2)
            return rad_3db