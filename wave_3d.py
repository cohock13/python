"""
量子力学での二次元量子箱で正方形領域の場合の波動関数のプロットです.
numpy,matplotlibが必要です.
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

###量子数の入力
print("enter n and l")
n = list(map(int,input().split()))

###平面にプロットする数
PLOT_N = 100

fig = plt.figure()
ax = fig.add_subplot(111)

x = y = np.linspace(0,1,PLOT_N)
X,Y = np.meshgrid(x,y)
PSI = np.sqrt(4)*np.sin(n[0]*np.pi*X)*np.sin(n[1]*np.pi*Y)

plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.pcolormesh(X, Y, PSI, cmap='coolwarm')
plt.colorbar (orientation="vertical") 
plt.show()