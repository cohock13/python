"""
量子力学での三次元量子箱で正方形領域の場合の波動関数のプロットです.
matplotlib,numpyが必要です.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

###量子数の入力
print("enter n,l and m")
n = list(map(int,input().split()))

###空間にプロットする数,30以上にすると多分カクつきます
PLOT_N = 20

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = z = np.linspace(0,1,PLOT_N)
X,Y,Z = np.meshgrid(x,y,z)
PSI = np.sqrt(8)*np.sin(n[0]*np.pi*X)*np.sin(n[1]*np.pi*Y)*np.sin(n[2]*np.pi*Z)
PSI = np.reshape(PSI,PLOT_N**3)

if sum(n)>3:
    threshold = 0.5
    mask = (-threshold<PSI)&(PSI<threshold)
    PSI[mask] = np.nan

img = ax.scatter(X, Y, Z, c=PSI, cmap="coolwarm",alpha=0.8)
fig.colorbar(img)
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y',fontsize=15)
ax.set_zlabel('z', fontsize=15)
plt.show()