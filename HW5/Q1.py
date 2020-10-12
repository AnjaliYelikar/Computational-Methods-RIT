import numpy as np
import matplotlib.pyplot as plt

data0 = np.load('galaxies0.npy')
print(len(data0))
data1 = np.load('galaxies1.npy')
print(len(data1))

x0 = data0[:,0]
y0 = data0[:,1]

x1 = data1[:,0]
y1 = data1[:,1]


plt.subplot(1,2,1)
plt.scatter(x0,y0)
plt.xlabel('x(Mpc)')
plt.ylabel('y(Mpc)')
plt.title('t=0')

plt.subplot(1,2,2)
plt.scatter(x1,y1)
plt.xlabel('x(Mpc)')
plt.ylabel('y(Mpc)')
plt.title('t=1000 yrs')

plt.show()
