
import numpy as np
import pandas as pd

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

X = np.transpose(np.vstack((np.array([1.]*len(E)),np.log10(P),Z)))
#print(type(X))

y = M_V

# theta = (XH*X)**-1*XH*y

sol = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(np.ndarray.conjugate(X)),X)),np.transpose(np.ndarray.conjugate(X))),y)
print('best fit parameters =', sol)

sigma2 = np.linalg.inv(np.matmul(np.transpose(np.ndarray.conjugate(X)),X)) 
#print(sigma2)

sigma = [np.sqrt(sigma2[i][i]) for i in range(len(sol))]
print('uncertainities =', sigma)
