from math import pi

u0 = 4.*pi*1E-7 # T m /A
hbar = 1.0545718E-34 # J s

# 1 T = kg s^-2 A-1 = J A^-1 m^-2

g = { 
    '1H' : 267.513E6, # rad T^-1 s^-1
    '13C': 67.262E6,
    '15N': -27.116E6,
    'e': 176086E6
    }

# nuc_i, nuc_j: nucleus string. ex: '1H'
# r_ij: distance in Angstroms
DCC = lambda nuc_i, nuc_j, r_ij: -1.*(u0*g[nuc_i]*g[nuc_j]*hbar)/(4.*pi*(r_ij*1E-10)**3) 

print('-'*30)
print('1H-15N (1.02A): {:> 8.1f} Hz'.format(DCC('1H','15N', 1.02)/(2.*pi), 'Hz'))
print('1H-15N (1.04A): {:> 8.1f} Hz'.format(DCC('1H','15N', 1.04)/(2.*pi), 'Hz'))

print('-'*30)
print('1H-13C (1.1A): {:> 8.1f} Hz'.format(DCC('1H','13C', 1.1)/(2.*pi), 'Hz'))

print('-'*30)
print('1H-1H (1.00A): {:> 8.1f} Hz'.format(DCC('1H','1H', 1.0)/(2.*pi), 'Hz'))
print('1H-1H (2.4A): {:> 8.1f} Hz'.format(DCC('1H','1H', 2.4)/(2.*pi), 'Hz'))
print('1H-1H (2.8A): {:> 8.1f} Hz'.format(DCC('1H','1H', 2.8)/(2.*pi), 'Hz'))

print('-'*30)
print('13C-13C (1.53A): {:> 8.1f} Hz'.format(DCC('13C','13C', 1.53)/(2.*pi), 'Hz'))

print('-'*30)
print('1H-e (1A): {:> 8.1f} MHz'.format(DCC('1H','e', 1.0)/(1E6*2.*pi), 'Hz'))
print('1H-e (5A): {:> 8.1f} kHz'.format(DCC('1H','e', 5.0)/(1E3*2.*pi), 'Hz'))
print('1H-e (10A): {:> 8.1f} kHz'.format(DCC('1H','e', 10.0)/(1E3*2.*pi), 'Hz'))
print('1H-e (50A): {:> 8.1f} kHz'.format(DCC('1H','e', 50.0)/(1E3*2.*pi), 'Hz'))
print('1H-e (100A): {:> 8.1f} Hz'.format(DCC('1H','e', 100.0)/(2.*pi), 'Hz'))

print('-'*30)
