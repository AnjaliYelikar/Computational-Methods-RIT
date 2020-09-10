
# part 1

import numpy as np
import matplotlib.pyplot as plt

kpc = 3.086*10.**21. # in meters
G = 6.673*10.**-11    # SI units
M_sun = 1.989*10.**30   # in kg

c = 15.
r_200 = 230.*kpc
v_200 = 160.         # in km/s

a = 0.1
b = 300.*kpc
n = 500

r = np.linspace(a,b,n)
x = r/r_200

v_c_r2 = (v_200**2)*(1./x)*(np.log(1.+c*x) - ((c*x)/(1.+c*x)))/(np.log(1.+c) - ((c)/(1.+c)))      # square of circular velocity at a radius r

M_enc_r = (r*v_c_r2)/G

plt.plot(r/kpc,M_enc_r/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$M_{enc}(r)(M_{\odot})$')
plt.yscale('log')
plt.savefig('M_enc_r_part1.pdf',dpi=300)
plt.show()


# M_total = 10.**8 M_sun?

dM_dr = np.gradient(M_enc_r,r)
#print(dM_dr)

plt.plot(r/kpc,dM_dr*kpc/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$\frac{dM(r)}{dr}(\frac{M_{\odot}}{kpc})$')
plt.yscale('log')
plt.savefig('dM_dr_part1.pdf',dpi=300)
plt.show()


# part 2

import numpy as np
import matplotlib.pyplot as plt

kpc = 3.086*10.**21. # in meters
G = 6.673*10.**-11    # SI units
M_sun = 1.989*10.**30   # in kg

c = 15.
r_200 = 230.*kpc
v_200 = 320.         # in km/s

a = 0.1
b = 300.*kpc
n = 500

r = np.linspace(a,b,n)
x = r/r_200

v_c_r2 = (v_200**2)*(1./x)*(np.log(1.+c*x) - ((c*x)/(1.+c*x)))/(np.log(1.+c) - ((c)/(1.+c)))      # square of circular velocity at a radius r

M_enc_r = (r*v_c_r2)/G

plt.plot(r/kpc,M_enc_r/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$M_{enc}(r)(M_{\odot})$')
plt.yscale('log')
plt.savefig('M_enc_r_part2.pdf',dpi=300)
plt.show()

# M_total = 10.**8 M_sun?

dM_dr = np.gradient(M_enc_r,r)
#print(dM_dr)

plt.plot(r/kpc,dM_dr*kpc/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$\frac{dM(r)}{dr}(\frac{M_{\odot}}{kpc})$')
plt.yscale('log')
plt.savefig('dM_dr_part2.pdf',dpi=300)
plt.show()

# part 3

import numpy as np
import matplotlib.pyplot as plt

kpc = 3.086*10.**21. # in meters
G = 6.673*10.**-11    # SI units
M_sun = 1.989*10.**30   # in kg

c = 30.
r_200 = 230.*kpc
v_200 = 160.         # in km/s

a = 0.1
b = 300.*kpc
n = 500

r = np.linspace(a,b,n)
x = r/r_200

v_c_r2 = (v_200**2)*(1./x)*(np.log(1.+c*x) - ((c*x)/(1.+c*x)))/(np.log(1.+c) - ((c)/(1.+c)))      # square of circular velocity at a radius r

M_enc_r = (r*v_c_r2)/G

plt.plot(r/kpc,M_enc_r/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$M_{enc}(r)(M_{\odot})$')
plt.yscale('log')
plt.savefig('M_enc_r_part3.pdf',dpi=300)
plt.show()

# M_total = 10.**8 M_sun?

dM_dr = np.gradient(M_enc_r,r)
#print(dM_dr)

plt.plot(r/kpc,dM_dr*kpc/M_sun)
plt.xlabel('r(kpc)')
plt.ylabel(r'$\frac{dM(r)}{dr}(\frac{M_{\odot}}{kpc})$')
plt.yscale('log')
plt.savefig('dM_dr_part3.pdf',dpi=300)
plt.show()
