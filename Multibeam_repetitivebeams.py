import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from parts.beam_param import BeamParameter
import csv
import collections

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
bp = BeamParameter(nxs=-750 - 225, nxe=750 - 225, nxd=125, nys=-750, nye=750, nyd=125)
#bp = BeamParameter(nxs=-1573, nxe=1573, nxd=100, nys=-1393, nye=1393, nyd=100)
bp.fname = "Multibeam_parts/Multibeam_list.csv"

b1 = []
b2 = []
b3 = []
BR_7beam = []

#placeList = bp.genPlace()

#print('place pattern = {}'.format(len(placeList)))
#for nb, nf, x, y in placeList:
#    if x == 0 or y == 0:
#        continue
#    if x//10*10 % 400 == 0 and nb == 1 and nf == 1 and y//10*10 % 400 == 0:
#        print('x = {}, y={}, xd={}, yd={} :: nf={}'.format(x, y, x//10*10, y//10*10, nf))
#        _ = bp.genBeam(x, y)

b1 = bp.genBeam(0,0)
#b2 = bp.genBeam(-226,0)+bp.genBeam(226,0)+bp.genBeam(113,196)+bp.genBeam(-113,196)+bp.genBeam(-113,-196)+bp.genBeam(113,-196)
for i in range(0,6,1):
    b2.append(bp.genBeam(225*np.cos(np.radians(60*i)),225*np.sin(np.radians(60*i))))

Ibp = b2[3]+b2[5]

b = b2[1]/Ibp

Xc ,Yc = np.meshgrid(bp.Nx, bp.Ny)
bdb = 10 * np.log10(b)

ax.plot_surface(Xc, Yc, bdb, cmap=cm.hsv)
ax.contourf(Xc, Yc, bdb, zdir='z', offset=-3, cmap=cm.hsv)
ax.set_xlabel('X[km]')
ax.set_ylabel('Y[km]')
ax.set_zlabel('$G(\theta)[dB]$')
ax.set_zlim(-60, 0)
plt.savefig('RPF3.png')
plt.show()

for j in range(len(bdb)):
    for w in range(len(bdb)):
        BitRate = bp.BitRate(bdb[j,w])
        #if BitRate != 0:
            #print(BitRate)
        BR_7beam.append(int(BitRate))

#print(bp.BitRate(11.0))
#c = collections.Counter(BR_7beam)
#print(c)
with open('Multibeam_repeat_1beam_2.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(BR_7beam)
#    for br in BR_7beam:
#        writer.writerow(br)
