import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
##import ffmpeg

##分割区間
N = 1000

#オイラー法での刻み幅
h = 0.01

##初期値の上限値
INIT_MAX = 10

RANGE = int(INIT_MAX/h)
fig = plt.figure()
x = np.linspace(0,10,N)
ims = []
u = np.zeros(N)

for a in range(RANGE):

	u[0] = a*h
	for b in range(N-1):
		u[b+1]=u[b]+np.sin(u[b])*h

	plt.xlabel("Solution of dx/dt=sin(x)")
	plt.ylabel("x")
	im1, = plt.plot(x, u, "r",label="dx/dt=sin(x),x(0)=")
	im2, = plt.plot(0, u[0], marker='.', color='red' )
	j = round(u[0],1)
	s = 'x(0)='+str(j)
	ttl = plt.text(6, 1, s, horizontalalignment='center', verticalalignment='bottom',fontsize=13)
	ims.append([im1, im2,ttl])
 
ani = animation.ArtistAnimation(fig, ims, interval=20)
##plt.show()
ani.save('diff_sin.gif', writer='imagemagick')