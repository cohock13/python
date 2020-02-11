import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
##import ffmpeg
import types


fig, ax = plt.subplots()
delta = 0.025
xrange = np.arange(-1.5, 1.5, delta)
yrange = np.arange(-1.5, 1.5, delta)
X, Y = np.meshgrid(xrange,yrange)
 
ims = []
c = ["red", "blue", "green", "darkorange","salmon","navy","firebrick","tan","blueviolet","chartreuse"]
for i in range(1,6):
    plt.axis([-1.5, 1.5, -1.5, 1.5])
    plt.gca().set_aspect('equal', adjustable='box')
    Z = X**(2*i) + Y**(2*i) -1
    im = plt.contour(X, Y, Z,[0],colors=c[i])
    add_art = im.collections
    s = 'x^'+str(2*i)+' + y^'+str(2*i)+' = 1'
    ttl_1 = plt.text(0, 1.2, s, horizontalalignment='center', verticalalignment='bottom',fontsize=12)

    ims.append(add_art+[ttl_1])

ani = animation.ArtistAnimation(fig, ims, interval=500,repeat=False)
plt.show()
###ani.save('circle.gif', writer='imagemagick')

