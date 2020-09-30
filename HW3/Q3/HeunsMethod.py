
import numpy as np
import matplotlib.pyplot as plt

def odeHeun(f,y0,t):
	#ODE solver by Heun's method where f is y'=f(t,y), y0 is the initial value
 	#at t0, t is the list of times we need to solve for

	y = np.zeros(len(t))
	y[0] = y0
	for n in range(0,len(t)-1):
		y_predictor = y[n] + (t[n+1] - t[n])*f(t[n],y[n])
		
		y[n+1] = y[n] + ((t[n+1] - t[n])/2.0)*(f(t[n],y[n]) + f(t[n+1],y_predictor))
	return y

t = np.linspace(0,2,20)
y0 = 1.
f = lambda y,t: y
y = odeHeun(f,y0,t)
y_true = np.exp(t)
plt.plot(t,y,'r.-',t,y_true,'b-')
plt.legend(['Heun','True'])
plt.axis([0,2,0,10])
plt.show()
