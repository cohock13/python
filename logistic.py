import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import numpy as np 
import random
from tqdm import tqdm

"""
変数
"""
MAX_TIME = 1000##シミュレーションの最大時
P_INFECTION = 0.005##感染確率
P_HEAL = 0.005##治癒確率


print("Enter N:",end=" ")
N = int(input())

fig = plt.figure()
ims = []

        
model = [[0 for i in range(N)] for j in range(N)]
infected = [0 for i in range(MAX_TIME)]
healed = [0 for i in range(MAX_TIME)]
model[N//2][N//2] = 1
N_infected = 1
N_healed = 0

dxdy = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]##周囲の8方向へ感染
for t in tqdm(range(MAX_TIME)):
    ##隣接した個体に感染する
    for i in range(N):
        for j in range(N):
            if model[i][j] == 1:
                for dx,dy in dxdy:
                    x = i + dx
                    y = j + dy
                    tmp_rand_infection = random.random()
                    if 0<=x<N and 0<=y<N and tmp_rand_infection<P_INFECTION and model[x][y] == 0:
                        model[x][y] = 1
                        N_infected += 1
                ##感染した個体について、一定確率で治癒し、二度と感染しない
                tmp_rand_heal = random.random()
                if tmp_rand_heal < P_HEAL and N_infected != 1:
                    model[i][j] = 2
                    N_healed += 1
                    ##N_infected -= 1
                            
    infected[t] = N_infected
    healed[t] = N_healed
    
    healthy_graph_x = []
    healthy_graph_y = []
    infected_graph_x = []
    infected_graph_y = []
    healed_graph_x = []
    healed_graph_y = []
    for i in range(N):
        for j in range(N):
            if model[i][j] == 0:
                healthy_graph_x.append(i)
                healthy_graph_y.append(j)
            elif model[i][j] == 1:
                infected_graph_x.append(i)
                infected_graph_y.append(j)
            else:##model[i][j] == 2
                healed_graph_x.append(i)
                healed_graph_y.append(j)
            
    healthy_graph_x = np.array(healthy_graph_x)
    healthy_graph_y = np.array(healthy_graph_y)
    infected_graph_x = np.array(infected_graph_x)
    infected_graph_y = np.array(infected_graph_y)
    healed_graph_x = np.array(healed_graph_x)
    healed_graph_y = np.array(healed_graph_y)
    
    plt.subplot(1,2,1)
    plt.tick_params(labelbottom=False,
        labelleft=False,
        labelright=False,
        labeltop=False)
    plt.title("Green:healthy,Red:infected,Gray:healed")
    plt_1 = plt.scatter(healthy_graph_x,healthy_graph_y,color="limegreen", s = 50)
    plt_2 = plt.scatter(infected_graph_x,infected_graph_y, color="tomato", s = 50)
    plt_3 = plt.scatter(healed_graph_x,healed_graph_y,color="dimgray",s = 50)
    
    plt.subplot(1,2,2)
    plt.title("Green:healthy,Red:infected,Gray:healed")
    plt.xlabel("times")
    times = np.array([i for i in range(t)])
    N_fill = np.array([N**2 for i in range(t)])
    fill = plt.fill_between(times,N_fill,color="limegreen")
    infected_nums = np.array(infected[:t])
    healed_nums = np.array(healed[:t])
    plt_4 = plt.fill_between(times,infected_nums,color="tomato")
    plt_5 = plt.fill_between(times,healed_nums,color="dimgray")
    
    ims.append([plt_1,plt_2,plt_3,fill,plt_4,plt_5])

ani = animation.ArtistAnimation(fig,ims,interval=10,repeat=True,blit=True)
##ani.save("test.mp4",writer="pillow")
plt.show()




