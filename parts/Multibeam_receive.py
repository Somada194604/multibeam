import numpy as np
import scipy.special

R = 20
c = 3.0*10**8
W = 36*10**6
f1 = 2.5*10**9
N = 0.0419
xc = yc = np.linspace(-1.25, 1.25, 1250)
Xc, Yc = np.meshgrid(xc, yc)

def beam_receivepower():
    s = (np.pi * R) / λ1 * np.sin(np.radians(np.sqrt(Xc ** 2 + Yc **2)))
    gc = (2*scipy.special.jv(1, s)/ s) ** 2
    log_gc = 10*np.log10(gc)

    gn = []
    g = []
    #for i in range(0, 360, 60):
    #    xa = np.cos(np.radians(i))*0.36
    #    x = np.linspace(-1.25 + xa, 1.25 + xa, 1250)
    #    ya = np.sin(np.radians(i))*0.36
    #    y = np.linspace(-1.25 + ya, 1.25 + ya, 1250)
    #    X, Y = np.meshgrid(x, y)
    #    s = (np.pi * R) / λ * np.sin(np.radians(np.sqrt(X ** 2 + Y **2)))
    #    gn.append((2*scipy.special.jv(1, s)/ s) ** 2)
    place = [(30, 0.72), (90, 0.72), (150, 0.72), (210, 0.72), (270, 0.72), (330, 0.72)]
    for t, r in place:
        xa2 = np.cos(np.radians(t))*r
        x2 = np.linspace(-1.25 + xa2, 1.25 + xa2, 1250)
        ya2 = np.sin(np.radians(t))*r
        y2 = np.linspace(-1.25 + ya2, 1.25 + ya2, 1250)
        X2, Y2 = np.meshgrid(x2, y2)
        s2 = (np.pi * R) / λ1 * np.sin(np.radians(np.sqrt(X2 ** 2 + Y2 **2)))
        gn.append((2*scipy.special.jv(1, s2)/ s2) ** 2)


    print(len(gn))    
    #g = 10*np.log10(gn[0] + gn[1] + gn[2] + gn[3] + gn[4] + gn[5])
    g = (N+gn[0]+gn[1]+gn[2]+gn[3]+gn[4]+gn[5])
    #+gn[6]+gn[7]+gn[8]+gn[9]+gn[10]+gn[11]+gn[12]+gn[13]+gn[14]+gn[15]+gn[16]+gn[17])
    
    
    #F_ue = gc/g
    F_ue = gc/g
    L_ue = 10*np.log10(F_ue)