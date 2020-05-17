import numpy as np
import itertools
import scipy.special

class BeamParameter:
    fname = "Multibeam_list.csv"
    R = 20
    c = 299792458
    f1 = 2.5 * 10 ** 9
    λ1 = c/f1
    Ku = 36*10**6.
    reb = 3.0
    numb = 7.0

    Ds = 35786

    def __init__(self, nbs=1, nbe=10, nbd=10, nfs=1, nfe=30, nfd=30, nxs=0, nxe=27, nxd=28, nys=0, nye=31, nyd=32):
        self.Nb = np.linspace(nbs,nbe,nbd)
        self.Nf = np.linspace(nfs,nfe,nfd)
        self.Nx = np.linspace(nxs,nxe,nxd)
        self.Ny = np.linspace(nys,nye,nyd)
        self.nxs = nxs
        self.nxe = nxe
        self.nxd = nxd
        self.nys = nys
        self.nye = nye
        self.nyd = nyd
    
    def genPlace(self):
        self.placeList = list(itertools.product(self.Nb, self.Nf, self.Nx, self.Ny))
        return self.placeList
    
    def genBeam(self, x, y):
        x2 = np.linspace(self.nxs-x, self.nxe-x, self.nxd)
        y2 = np.linspace(self.nys-y, self.nye-y, self.nyd)
        self.X2, self.Y2 = np.meshgrid(x2, y2)
        t = np.arctan2(np.sqrt(self.Y2 ** 2 + self.X2 ** 2), self.Ds)
        #s = (np.pi * self.R) / self.λ1 * np.sin(np.radians(np.sqrt(X2 ** 2 + Y2 **2)))
        s = ((np.pi * self.R) / self.λ1) * np.sin(t)
        return (2*scipy.special.jv(1, s) / s) ** 2
    
    def BitRate(self, CNR):
        if CNR >= 19.5:
            BR = 4.5*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif CNR > 15.8 and 19.5 > CNR:
            BR = 4*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 13.8 < CNR and CNR < 15.8:
            BR = 3.5*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 11.2 < CNR and CNR< 13.8:
            BR =3*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 10.0 < CNR and CNR< 11.2:
            BR = 2.5*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 7.4 < CNR  and CNR< 10.0:
            BR = 2.0*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 5.6 < CNR  and CNR< 7.4:
            BR = 1.67*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 4.6 < CNR  and CNR< 5.6:
            BR = 1.5*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 2.7 < CNR  and CNR< 4.6:
            BR = 1.2*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        elif 1.4 < CNR  and CNR< 2.7:
            BR = 1.0*((self.Ku)/(self.reb*self.numb*self.nxd*self.nyd))
            return BR
        else:
            BR =0
            return BR
    
    def writeCSV(self):
        with open(self.fname, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["num_beam", "same freq.", "x", "y"])

        with open(self.fname, "a") as f:
            writer = csv.writer(f)
            for m in self.placeList:
                writer.writerow(m)
