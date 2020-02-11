
"""
3.0以上のバージョンのPythonが必要です.
numpy,matplotlibの最新バージョン(2019/11現在)を使用しています.
動画を出力する場合は一番下のani.saveのコメントアウトを外して,plt.show()にコメントアウトしてください.
また,動画の出力にはffmpegが必要です.
"""

import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
##import ffmpeg

V_0 = 1
fig = plt.figure()
ims = []
E = np.linspace(0,V_0,200)
x = np.linspace(-8,8,200)
j = 1j

def kappa(E):
    return np.sqrt(V_0-E)

def k(E):
    return np.sqrt(E)

def ratio(E):
    return k(E)/kappa(E)
def Q(E,a):
    return 2*(1-(ratio(E))**2)*np.sinh(kappa(E)*a)-4*j*ratio(E)*np.cosh(kappa(E)*a)

def A(E,a):
    return -(2/Q(E,a))*(1+(ratio(E))**2)*np.exp(-j*k(E)*a)*np.sinh(kappa(E)*a)

def B(E,a):
    return -(2*j/Q(E,a))*ratio(E)*np.exp(-k(E)*a/2)*(1+j*ratio(E))*np.exp(-j*k(E)*a/2)

def C(E,a):
    return -(2*j/Q(E,a))*ratio(E)*np.exp(k(E)*a/2)*(1-j*ratio(E))*np.exp(-j*k(E)*a/2)

def D(E,a):
    return -(4*j/Q(E,a))*ratio(E)*np.exp(-j*k(E)*a)

def func_T(E,a):
    return np.real(D(E,a)*np.conj(D(E,a)))

def incident_wave(E,a,x):
    return np.real(A(E,a)*np.exp(-j*k(E)*x)+np.exp(j*k(E)*x))

def wave_wall(E,a,x):
    return np.real(B(E,a)*np.exp(kappa(E)*x)+C(E,a)*np.exp(-kappa(E)*x))

def transmitted_wave(E,a,x):
    return np.real(D(E,a)*np.exp(j*k(E)*x))

for i in range(600):

    a = 0.01*i
    ##左側(E-Tグラフ)
    plt.subplot(1,2,1)
    plt.title("Transmission Coefficient")
    plt.xlabel("E / V₀")
    plt.ylabel("T")

    T_curve, = plt.plot(E, func_T(E,a), "r")
    T_point, = plt.plot(0.5*V_0,func_T(0.5*V_0,a),marker=".",color="red")
    s = 'l='+str(round(a,1))
    l_label = plt.text(0.5, 0.95, s, horizontalalignment='center', verticalalignment='bottom',fontsize=15)

    ##右側(x-ψグラフ)
    plt.subplot(1,2,2)
    plt.title("Tunneling Effect")
    plt.xlabel("x")
    plt.ylabel("Re(Ψ)")
    plt.xlim(-8,8)
    plt.ylim(-5,5)

    square = plt.axvspan(xmin=-0.5*a, xmax=0.5*a,ymin=0, ymax=0.8, alpha=0.3, color='red')

    u = "T(0.5V₀)="+(str(round(func_T(0.5*V_0,a),2))).ljust(4,'0')
    t_label = plt.text(0, 4.2, u, horizontalalignment='center', verticalalignment='bottom',fontsize=15)

    left = np.linspace(-8,8,200)
    wall = np.linspace(-8,8,200)
    right = np.linspace(-8,8,200)

    left[left>-0.5*a]=np.nan
    wall[-0.5*a>=wall]=np.nan
    wall[wall>=0.5*a]=np.nan
    right[0.5*a>right]=np.nan

    wave_l, = plt.plot(x,incident_wave(0.5*V_0,a,left),color="r")
    wave_c, = plt.plot(x,wave_wall(0.5*V_0,a,wall),color="g")
    wave_r, = plt.plot(x,transmitted_wave(0.5*V_0,a,right),color="b")

    ims.append([T_curve,T_point,l_label,square,t_label,wave_l,wave_c,wave_r])


 
ani = animation.ArtistAnimation(fig, ims, interval=30, repeat=True,blit=True)
plt.show()
##ani.save('Tunneling_1.mp4', writer='ffmpeg')
##ani.save("Tunneling_1.gif",writer="Imagemagick")