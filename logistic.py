import matplotlib.pyplot as plt
import numpy as np 
import random
from tqdm import tqdm

def graph(N):
    MAX_TIME = 3000##シミュレーションの最大時間
    THRESHOLD = 0.005##感染確率　この場合0.01%
    if N < 10:
        print("Please Enter Some Number Over 10.")
        return
    else:
        model = [[0 for i in range(N)] for j in range(N)]
        time_list = []
        infected = [0 for i in range(MAX_TIME)]
        model[N//2][N//2] = 1
        count = 1
        time = 0
        x_0 = 0
        dxdy = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]##周囲の8方向へ感染
        for t in tqdm(range(MAX_TIME)):##計算量O(MAX_TIME*N^2)ただappendのせいもあり重い?
            for i in range(N):
                for j in range(N):
                    if model[i][j] == 1:
                        for dx,dy in dxdy:
                            x = i + dx
                            y = j + dy
                            tmp_rand = random.random()
                            if 0<=x<N and 0<=y<N and tmp_rand<THRESHOLD and model[x][y] == 0:
                                model[x][y] = 1
                                count += 1
                                if count == (N**2)//2:
                                    x_0 = t
            infected[t] = count
        print("x_0",x_0)
        time = np.linspace(0,MAX_TIME,MAX_TIME)
        infected = np.array(infected)
        plt.plot(time,infected,label="stochastic")
        logistic = (N**2)/(1+(N**2-1)*np.exp(-THRESHOLD*(time)))
        plt.plot(time,logistic,label="logistic")
        plt.legend(loc="best",shadow=True)
        plt.xlabel("time")
        plt.xlim(0,MAX_TIME)
        plt.ylabel("Infected[percent]")
        ##plt.ylim(0,105)
        plt.show()

        return

if __name__ == "__main__":
    print("enter N :",end="")
    N = int(input())
    graph(N)


