from covidsim import Cell, Simulator, State
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_c(s):
        if s == State.Normal:
            return 'b'
        elif s==State.Infected:
            return 'r'
        elif s==State.Recovered:
            return 'g'
        return 'k'

def main():
    sim = Simulator(((0.0,50.0),(0.0,50.0)))
    #sim.add_cells(50,0.1,1.0)
    sim.add_cells(50,0.1,0.2,maxboundlen=10.0)
    result = sim.simulate(maxstep=1000)

    show_result(result)

def show_result(simdata):
    fig = plt.figure()
    ims = []
    for r in simdata:
        t = {State.Normal:[],State.Infected:[],State.Recovered:[],State.Dead:[]}
        for cpos,cstate in r:
            t[cstate].append(cpos)
        
        temp = []
        for s in State:
            t[s] = np.array(t[s]).T
            if t[s].size!=0:
                temp.append(plt.scatter(t[s][0],t[s][1],c=get_c(s)))
        ims.append(temp)

    ani = animation.ArtistAnimation(fig, ims, interval=30)
    plt.show()    
           

if __name__ == "__main__":
    main()