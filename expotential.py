import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from numpy import sin,cos

a = 1
x = np.arange(0, 20, 0.01)
 
y= np.zeros(2000)
y[0]=1

for k in range(2000-1):
   y[k+1]=y[k]+np.sin(y[k])*0.01


plt.plot(x, y,"r", Label="dx/dt=sin(x),x(0)=1")
plt.legend()
plt.show()
