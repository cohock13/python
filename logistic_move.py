import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap
import numpy as np 
import random
import ffmpeg
from tqdm import tqdm

"""
変数
"""
MAX_TIME = 1500##シミュレーションの最大時
P_INFECTION = 0.01##感染確率
P_HEAL = 0.001##治癒確率
P_DEAD = 0.0005##死亡確率
RADIUS_INFECTION = 1.2##感染距離

P_DEAD = 1 - P_DEAD

def graph(N):

    fig = plt.figure()
    ims = []

    model = [[0 for i in range(N)] for j in range(N)]
    infected = [0 for i in range(MAX_TIME)]
    healed = [0 for i in range(MAX_TIME)]
    dead = [0 for i in range(MAX_TIME)]
    model[N//2][N//2] = 1
    N_infected = 1
    N_healed = 0
    N_dead = 0

    ##初期速度
    velocity = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            x,y = random.randint(-1,1),random.randint(-1,1)
            if x != 0 and y != 0:
                velocity[i][j] = [x,y]
            else:
                velocity[i][j] = [x,y]

    ##初期位置
    position = [[[] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            position[i][j] = [i,j]

    for t in tqdm(range(MAX_TIME)):
                                
        infected[t] = N_infected
        healed[t] = N_healed + N_dead
        dead[t] = N_dead
        
        healthy_graph_x = []
        healthy_graph_y = []
        infected_graph_x = []
        infected_graph_y = []
        healed_graph_x = []
        healed_graph_y = []
        dead_graph_x = []
        dead_graph_y = []

        for i in range(N):
            for j in range(N):
                x = position[i][j][0]
                y = position[i][j][1]
                if model[i][j] == 0:
                    healthy_graph_x.append(x)
                    healthy_graph_y.append(y)
                elif model[i][j] == 1:
                    infected_graph_x.append(x)
                    infected_graph_y.append(y)
                elif model[i][j] == 2:
                    healed_graph_x.append(x)
                    healed_graph_y.append(y)
                else:##dead
                    dead_graph_x.append(x)
                    dead_graph_y.append(y)
                
        healthy_graph_x = np.array(healthy_graph_x)
        healthy_graph_y = np.array(healthy_graph_y)
        infected_graph_x = np.array(infected_graph_x)
        infected_graph_y = np.array(infected_graph_y)
        healed_graph_x = np.array(healed_graph_x)
        healed_graph_y = np.array(healed_graph_y)
        dead_graph_x = np.array(dead_graph_x)
        dead_graph_y = np.array(dead_graph_y)



        plt.subplot(1,2,1)
        plt.tick_params(labelbottom=False,
            labelleft=False,
            labelright=False,
            labeltop=False)
        plt_1 = plt.scatter(healthy_graph_x,healthy_graph_y,color="limegreen", s=50)
        plt_2 = plt.scatter(infected_graph_x,infected_graph_y, color="tomato", s=50)
        plt_3 = plt.scatter(healed_graph_x,healed_graph_y,color="deepskyblue",s=50)
        plt_4 = plt.scatter(dead_graph_x,dead_graph_y,color="dimgray",s =50)
        
        plt.subplot(1,2,2)
        plt.xlabel("times")
        times = np.array([i for i in range(t)])
        N_fill = np.array([N**2 for i in range(t)])
        fill = plt.fill_between(times,N_fill,color="limegreen")
        infected_nums = np.array(infected[:t])
        healed_nums = np.array(healed[:t])
        dead_nums = np.array(dead[:t])
        plt_5 = plt.fill_between(times,infected_nums,color="tomato")
        plt_6 = plt.fill_between(times,healed_nums,color="deepskyblue")
        plt_7 = plt.fill_between(times,dead_nums,color="dimgray")
        ims.append([plt_1,plt_2,plt_3,plt_4,fill,plt_5,plt_6,plt_7])
        plt.suptitle("Green:healthy Orange:infected Blue:healed Gray:dead")


        ##感染,治癒,死亡
        for i in range(N):
            for j in range(N):
                if model[i][j] == 1: 
                    for k in range(N):
                        for h in range(N):
                            distance = np.sqrt((position[i][j][0]-position[k][h][0])**2+(position[i][j][1]-position[k][h][1])**2)
                            p = random.random()
                            if distance < RADIUS_INFECTION and p < P_INFECTION and  model[k][h] == 0:
                                model[k][h] = 1
                                N_infected += 1

                    if N_infected != 1:##初期状態での終了を防止
                        p = random.random()
                        if p < P_HEAL:
                            model[i][j] = 2
                            N_healed += 1
                        elif p > P_DEAD:
                            model[i][j] = 3
                            N_dead += 1

        ##位置更新
        for i in range(N):
            for j in range(N):
                if model[i][j] == 3:##死亡していた場合
                    velocity[i][j][0] = 0
                    velocity[i][j][1] = 0
                position[i][j][0] += 0.01*velocity[i][j][0]
                position[i][j][1] += 0.01*velocity[i][j][1]
                if not 0 <= position[i][j][0] <= N:
                    velocity[i][j][0] *= -1
                if not 0 <= position[i][j][1] <= N:
                    velocity[i][j][1] *= -1
                        
    ani = animation.ArtistAnimation(fig,ims,interval=5,repeat=False)
    ani.save("log.mp4",writer="ffmpeg",fps=50)
    ##plt.show()


def enter():
    print("Enter N(10<=N<=30):",end=" ")
    N = int(input())
    return N

if __name__ == "__main__":
    N = enter()
    graph(N)
    