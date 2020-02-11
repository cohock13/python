import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
##import ffmpeg

 
fig = plt.figure()
x = np.arange(0, 10, 0.01)
 
ims = []
u = np.zeros(1000)
for a in range(100):
	u[0] = a*0.1
	for b in range(1000-1):
		u[b+1]=u[b]+0.01*np.sin(u[b])
		
	plt.subplot(1,2,1)
	im1, = plt.plot(x, u, "r",label="dx/dt=sin(x),x(0)=")
	plt.subplot(1,2,2)
	im2, = plt.plot(x, u, color='red' )
	j = round(a*0.1,1)
	s = 'x(0)='+str(j)
	ttl = plt.text(6, 1, s, horizontalalignment='center', verticalalignment='bottom',fontsize=13)
	ttl2 = plt.text(8, 2, s, horizontalalignment='center', verticalalignment='bottom',fontsize=13)
	ims.append([im1, im2,ttl,ttl2])
 
ani = animation.ArtistAnimation(fig, ims, interval=20, repeat=False)
plt.show()
#ani.save("sin_1.mp4",writer="ffmpeg")
##ani.save('sample.mp4', writer='ffmpeg')