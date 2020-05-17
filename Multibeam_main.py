import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from parts.beam_param import BeamParameter
import csv
import collections
import math

fig = plt.figure(figsize=(10.24, 7.68))   #figureの縦横の大きさ
ax = fig.add_subplot(111, projection='3d')  #figure内の枠の大きさとどこに配置するか。subplot(行の数,列の数,何番目に配置しているか,何次元表示にするか)
bp = BeamParameter(nxs=-750, nxe=750, nxd=125, nys=-750, nye=750, nyd=125)  #ビームを何行、何列に区切り、何間隔でユーザを配置するか。Beamparameter(行初め,行終わり,ユーザ配置間隔,列初め,列終わり,ユーザ配置間隔)
#bp = BeamParameter(nxs=-1573, nxe=1573, nxd=100, nys=-1393, nye=1393, nyd=100)
bp.fname = "Multibeam_parts/Multibeam_list.csv" #データ保存ファイル名

b1 = [] #BeapParameterで決定した、各ユーザ位置におけるビーム中心からの相対利得を格納
b2 = [] #上と同じ
b3 = [] #
BR_7beam = [] #各ユーザ位置におけるビットレートを格納

placeList = bp.genPlace()

#print('place pattern = {}'.format(len(placeList)))
#for nb, nf, x, y in placeList:
#    if x == 0 or y == 0:
#        continue
#    if x//10*10 % 400 == 0 and nb == 1 and nf == 1 and y//10*10 % 400 == 0:
#        print('x = {}, y={}, xd={}, yd={} :: nf={}'.format(x, y, x//10*10, y//10*10, nf))
#        _ = bp.genBeam(x, y)

b1 = bp.genBeam(0.0001,0.0001) #指定した二次元座標をビーム中心とし、ビームを配置 BeamParameterで設定したユーザ位置におけるビーム中心からの相対利得を格納
#b2 = bp.genBeam(-226,0)+bp.genBeam(226,0)+bp.genBeam(113,196)+bp.genBeam(-113,196)+bp.genBeam(-113,-196)+bp.genBeam(113,-196)
for i in range(0,6,1): #ループ
    b2.append(bp.genBeam(225*np.cos(np.radians(60*i)),225*np.sin(np.radians(60*i)))) #b1と同様に、ビーム中心から、同心円状に配置

Ibp = b2[3]+b2[5] #干渉電力となる各ビームのビーム中心からの相対利得の総和

b = b2[1]/Ibp #干渉電力の総和と

#ave = np.average(b)
#print(ave)

Xc ,Yc = np.meshgrid(bp.Nx, bp.Ny)
bdb = 10 * np.log10(b)

       
ax.plot_surface(Xc, Yc, bdb.clip(-20, None), cmap=cm.hsv)
ax.contourf(Xc, Yc, bdb, zdir='z', offset=-3, cmap=cm.hsv)
ax.set_xlabel('X[km]')
ax.set_ylabel('Y[km]')
ax.set_zlabel('$G(\theta)[dB]$')
ax.set_zlim(-20, None)
ax.set_zlim(-20, 20)
plt.savefig('RPF3_beam3.png')

for i in range(0, 360, 1):
#	plt.cla()
	j = 45 * np.abs(math.sin(i * 2 * math.pi / 360))
	ax.view_init(j, i)
	print('{:03} : {}'.format(i, round(i/360.0*100, 2)))
	plt.savefig('anim_beamcenter/fig_{:03}.png'.format(i))

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
with open('Multibeam_result_repeat3_beam6.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(BR_7beam)
#    for br in BR_7beam:
#        writer.writerow(br)
