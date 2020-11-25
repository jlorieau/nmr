#15N/1H relaxation based on

# Mandel a M, Akke M, Palmer a G. Backbone dynamics of Escherichia
# coli ribonuclease HI: correlations with structure and function in an
# active enzyme. J Mol Biol. 1995 Feb 10;246(1):144–63. PMID: 7531772

from math import cos, sin, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


taum = 8.40E-9 # seconds

gamma_H = 267.5221900E6  # rad s^-1 T^-1
gamma_N = -27.116E6

rNH = 1.02E-10  # m
u0 = 1.2566370614E-6
dNH = u0 * gamma_H * gamma_N * (6.62607004E-34) /(8. * pi**2 * rNH**3)

rHH = 2.2E-10  # m
sHH2 = (u0 / (4. * pi))**2 * gamma_H**4 * 6.62607004E-34**2 / (40. * pi**2 * rHH**6)

cN = lambda omegaN: omegaN * -160.E-6 / sqrt(3.)
cH = lambda omegaH: omegaH * 15.E-6 / sqrt(3.)

J = lambda omega, S2=1.0, tauc=100.E-1, taum=taum: ((2./5.) * (S2 * taum) / (1. + omega**2 * taum**2) +
                                                     (2./5.)*(1.-S2)*tauc/(1.+ (omega*tauc)**2))
R1N = dict()
R2N = dict()
hetNOE = dict()

taum = np.arange(0.1, 20, 0.1) * 1E-9  # s

for vH in (500., 600., 750.):
    wH = vH * 1.E6 * 2. * pi  # rad s^-1  
    wN = vH * 1.E6 * 2. * pi * (gamma_N/gamma_H)  # rad s^-1
    
    R1Ndip = (dNH**2 / 4.) * (J(wH-wN, taum=taum) + 3.0 *J(wN, taum=taum) +
                              6.*J(wH+wN, taum=taum)) 
    R1Ncsa = cN(wN)**2 *J(wN, taum=taum) 

    R1N[vH] = R1Ndip + R1Ncsa

    R2Ndip = (dNH**2 / 8.) * (4. * J(0, taum=taum) +
                              J(wH-wN, taum=taum) + 3.*J(wN, taum=taum) + 6.*J(wH, taum=taum) +
                              6.*J(wN+wH, taum=taum)) 
    R2Ncsa = (cN(wN)**2  / 6.) * (4. * J(0, taum=taum) + 3.*J(wN, taum=taum)) 

    R2N[vH] = R2Ndip + R2Ncsa

    hetNOE[vH] = (1. + (dNH**2/(4.*R1N[vH])) * (gamma_H / gamma_N) *
                  (6.*J(wH+wN, taum=taum) - J(wH-wN)))


fig, axes = plt.subplots(3, 1, sharex=True, figsize=(6,6)) # 3 rows, 1 cos

# Plot the R1N
for vH, data in sorted(R1N.items()):
    axes[0].plot(taum / 1E-9, data, label="{:.0f}MHz".format(vH))
axes[0].set_ylim(0,4.5)
axes[0].yaxis.set_major_locator(MultipleLocator(1.))
axes[0].set_ylabel('$R_{1N}$ ($s^{-1}$)')
axes[0].legend(loc='upper right', ncol=len(R1N))

# Plot the R2N
for vH, data in sorted(R2N.items()):
    axes[1].plot(taum / 1E-9, data, label="{:.0f}MHz".format(vH))
axes[1].set_ylabel('$R_{2N}$ ($s^{-1}$)')


# Plot the HetNOE
for vH, data in sorted(hetNOE.items()):
    axes[2].plot(taum / 1E-9, data, label="{:.0f}MHz".format(vH))
axes[2].set_ylim(0., 0.9)
axes[2].yaxis.set_major_locator(MultipleLocator(0.1))
axes[2].set_ylabel('$^{15}N$-{$^{1}H$}')
axes[2].set_xlabel('$\\tau_m$ ($ns$)')

fig.tight_layout()
fig.savefig('15N_relaxation.pdf')    
