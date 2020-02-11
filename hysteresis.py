import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from tqdm import tqdm

##VARIABLES
RANGE = 2
PLOT_N = 100
center_x = 2
center_y = -2
radius = 4
t_move = 100
t_stop = 50

##AREAS
X = np.linspace(-RANGE,RANGE,PLOT_N)
prime = np.linspace(-RANGE,RANGE,PLOT_N)
prime[prime<0]=np.nan

##FUNCTIONS
def enter(x):
    return RANGE*np.sin(x*np.pi/4)

def circle(x,N):
    if N==1:##UP
        return center_y+np.sqrt(-(x-center_x)**2+radius**2)
    else:##DOWN
        return -center_y-np.sqrt(-(x+center_x)**2+radius**2)

def f(x,N):
    if N==0:
        return enter(x)
    else:
        return circle(x,N)



def animate(x,N,second,max,min,ims,reverse):

    for i in tqdm(range(second)):
        if reverse==True:
            a = max-(max-min)*(i/second)
        else:
            a = min-(min-max)*(i/second)
        
        x = np.linspace(-RANGE,RANGE,PLOT_N)
        prime = np.linspace(-RANGE,RANGE,PLOT_N)
        prime[prime<0]=np.nan
        plt.xlabel("E[V/m]")
        plt.ylabel("D[C/m^2]")
        P_text = plt.text(-0.25,1.5, "Pr", horizontalalignment='center', verticalalignment='bottom',fontsize=16,color="black")
        P_scat = plt.scatter([0,0],[circle(0,1),circle(0,2)],s=70,color="limegreen")
        plt.hlines([0],-RANGE,RANGE,linestyle="dotted")
        plt.vlines([0],-RANGE,RANGE,linestyle="dotted")
        fin, = plt.plot(prime,enter(x),linestyle='dashed',color="r")
        circle_1, = plt.plot(x,circle(x,1),color="r")
        circle_2, = plt.plot(x,circle(x,2),color="r")
        point = plt.scatter(a,f(a,N),color="r",s=120)
        s = "E="+(str(round(a,1))).ljust(2,'0')
        value_E = plt.text(-1.5,1.5, s, horizontalalignment='center', verticalalignment='bottom',fontsize=20)

        ims.append([P_text,P_scat,fin,circle_1,circle_2,point,value_E])

def animate_2(x,second,max,min,ims,reverse):
    
    for i in tqdm(range(second)):
        if reverse==True:
            a = max-(max-min)*(i/second)
        else:
            a = min-(min-max)*(i/second)
        
        x = np.linspace(-RANGE,RANGE,PLOT_N)
        prime = np.linspace(-RANGE,RANGE,PLOT_N)
        prime[prime<0]=np.nan
        plt.xlabel("E[V/m]")
        plt.ylabel("D[C/m^2]")
        plt.hlines([0],-RANGE,RANGE,linestyle="dotted")
        plt.vlines([0],-RANGE,RANGE,linestyle="dotted")
        point = plt.scatter(a,a,color="limegreen",s=120)
        s = "E="+(str(round(a,1))).ljust(2,'0')
        line, = plt.plot(x,x,color="limegreen")
        value_E = plt.text(-1.5,1.5, s, horizontalalignment='center', verticalalignment='bottom',fontsize=20)

        ims.append([line,point,value_E])

def main():

    C_1 = 0
    C_2 = 0
    C_3 = 0
    print("PRESS 1:Ferroelectric ,PRESS 2:Paraelectric -->")
    C_1 = int(input())
    print("PRESS 1:Show Video ,PRESS 2:Create Video -->")
    C_2 = int(input())
    if C_2 ==2:
        print("PRESS 1:.mp4 ,PRESS 2:.gif -->")
        C_3 = int(input())
    print("interval? -->")
    INTERVAL = int(input())

    ims = []
    fig = plt.figure()
    area = np.linspace(-RANGE,RANGE,PLOT_N)
    if C_1==1:
        ##O to right
        animate(prime,0,t_move,RANGE,0,ims,False)
        ##stop at right
        animate(RANGE,0,t_stop,RANGE,RANGE,ims,False)
        #right to Pr
        animate(X,1,t_move,RANGE,0,ims,True)
        ##stop at Pr
        animate(0,1,t_stop,0,0,ims,False)
        ##Pr to left
        animate(area,1,t_move,0,-RANGE,ims,True)
        #stop at left
        animate(-RANGE,1,t_stop,-RANGE,-RANGE,ims,False)
        ##left to -Pr
        animate(area,2,t_move,0,-2,ims,False)
        ##stop at -Pr
        animate(0,2,t_stop,0,0,ims,False)
    
    else:
        ##same movement of E as ferroelectric
        animate_2(prime,t_move,2,0,ims,False)
        animate_2(area,t_stop,RANGE,RANGE,ims,False)
        animate_2(area,t_move,RANGE,0,ims,True)
        animate_2(0,t_stop,0,0,ims,False)
        animate_2(area,t_move,0,-RANGE,ims,True)
        animate_2(-RANGE,t_stop,-RANGE,-RANGE,ims,False)
        animate_2(area,t_move,0,-RANGE,ims,False)
        animate_2(0,t_stop,0,0,ims,False)
    
    ani = animation.ArtistAnimation(fig,ims,interval=INTERVAL,repeat=False)
    
    if C_1 == 1 and C_3 == 1:
        ani.save("hysteresis_ferro.mp4",writer="ffmpeg")
    elif C_1 == 1 and C_3 == 2:
        ani.save("hysteresis_fer.gif",writer="pillow")
    elif C_1 == 2 and C_3 == 1:
        ani.save("hysteresis_para.mp4",writer="ffmpeg")
    elif C_1 == 2 and C_3 == 2:
        ani.save("hysteresis_para.gif",writer="pillow")
    else:
        plt.show()


if __name__=="__main__":
    main()


    
     