
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

alpha_full_sig = 0.143052598123
beta_full_sig = 0.1676473246898537
gamma_full_sig = 0.25234995714561903

alpha_nest_sig = 0.13863519522330173
beta_nest_sig = 0.1590257836552863

samples=500

chisqr_full = (np.random.normal(0.,alpha_full_sig,samples))**2. + (np.random.normal(0.,beta_full_sig,samples))**2. + (np.random.normal(0.,gamma_full_sig,samples))**2.
chisqr_nest = (np.random.normal(0.,alpha_nest_sig,samples))**2. + (np.random.normal(0.,beta_nest_sig,samples))**2.

nu_full=3.
nu_nest=2.

F = ((chisqr_nest - chisqr_full)/(nu_full - nu_nest))/((chisqr_full)/(samples-nu_full))
print(len(F))

numerator_dof=2.
demoninator_dof=1.

F_stat = stats.f.cdf(F, numerator_dof , demoninator_dof)
print(len(F_stat))
print(np.mean(F_stat))

d0 = plt.hist(F_stat,bins=110,density=True,cumulative=True,histtype='step',linewidth=2.0)

y0=d0[0]
x0=d0[1]
xm0=(x0[:-1]+x0[1:])/2.

plt.clf()
plt.plot(xm0,y0)
plt.show()
