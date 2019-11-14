"""
Monte Carlo Method
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import ffmpeg


N = 100

fig = plt.figure()
ims = []
x_1 = np.linspace(0,1,10000)
y_1 = np.sqrt(1.0 - x_1*x_1)
x_2  = y_2 = np.array([])
inside_x = inside_y = outside_x = outside_y = np.array([])

count_i = 0
count_o = 0



for a in range (N):
    if a == 0:
        tmp_x = tmp_y = 0.5;
    else:
        tmp_x , tmp_y = np.random.rand(2)

    if  tmp_x*tmp_x + tmp_y*tmp_y <= 1:
        inside_x = np.append(inside_x ,tmp_x)
        inside_y = np.append(inside_y, tmp_y)
        count_i+=1
    else:
        outside_x = np.append(outside_x,tmp_x)
        outside_y = np.append(outside_y,tmp_y)
        count_o+=1

    value = 4 * count_i/(count_i + count_o)
    x_2 = np.append(x_2,a)
    y_2 = np.append(y_2,value)
    
    ##左側
    plt.subplot(1,2,1)
    plt.title("Monte Carlo Method(MC)")
    plt_1 = plt.scatter(inside_x, inside_y, color="green", s = 10)
    plt_2 = plt.scatter(outside_x,outside_y, color="tomato", s = 10)
    s = 'N='+str(a)
    text_1 = plt.text(0.5, -0.185, s, horizontalalignment='center', verticalalignment='bottom',fontsize=12)
    plt_3 = plt.plot(x_1, y_1, color = "black")
    #ims.append([plt_1,plt_2,text_1,plt_3])
    
    ##右側
    r = plt.subplot(1,2,2)
    plt.title("4*(Green)/(Green+Orange)")
    plt.xlabel("number of plots")
    plt_4 = plt.scatter(x_2, y_2, color = "red", s = 10)
    r.axhline(np.pi, ls = "-.", color = "gray")
    o = "Value="+(str(round(value,6))).ljust(8,'0')
    text_2 = plt.text(N/2, 3.75, o, horizontalalignment='center', verticalalignment='bottom',fontsize=12)
    ims.append([plt_1,plt_2,text_1,plt_4,text_2])

ani = animation.ArtistAnimation(fig, ims, interval=20)
##ani.save('Monte.mp4', writer='ffmpeg')
plt.show()