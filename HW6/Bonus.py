
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data = pd.read_table('cepheid_data.txt',sep='\t',skiprows=1)
#print(data[1])

#I choose the V-band

data = np.loadtxt('cepheid_data.txt', delimiter=',', usecols=(1,2,3,4,5,6,7,8),skiprows=1)

d = data[:,1]
E = data[:,6]
R_V=np.array([3.1]*len(E))
A_V = R_V*E
m_V = data[:,2]
M_V = m_V - 5.*np.log10(d) + 5. - A_V
#print(len(M_V))
#print(len(m_V)) 

P = data[:,0]
Z = data[:,7]

X = np.transpose(np.vstack((np.array([1.]*len(E)),np.log10(P))))

y = M_V
eps = np.array([0.1]*len(E))

# theta = (XH*X)**-1*XH*y

sol1 = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(np.ndarray.conjugate(X)),X)),np.transpose(np.ndarray.conjugate(X))),y)
sol2 = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(np.ndarray.conjugate(X)),X)),np.transpose(np.ndarray.conjugate(X))),eps)
sol = sol1 + sol2
print('best fit parameters=', sol) 

sigma2 = np.linalg.inv(np.matmul(np.transpose(np.ndarray.conjugate(X)),X)) 

sigma = [np.sqrt(sigma2[i][i]) for i in range(len(sol))]
print('uncertainities =', sigma)

M_V_fit = sol[0] + sol[1]*np.log10(P)

plt.scatter(P,M_V,c='C0',label='data')
plt.scatter(P,M_V_fit,c='r',label='fit')
plt.xscale('log')
plt.legend(fontsize=10)
plt.xlabel('Period(days)')
plt.ylabel(r'$M_{V}$')
plt.savefig('Bonus_fit.pdf', dpi=300)
#plt.show()

 
