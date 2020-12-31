"""
Hydraulic Spider Simulation Ver.1 (2020/12/31)
"""

##########################################################################
###PARAMETERS###

## Simulation Time and Steps
time = 5 
step = 1000

## Coeficcients in the Model
N = 2        ## Number of Legs
C = 0.2      ## Coefficient of Hemolymph(=u)
a = 1        ## Coefficient of Elastic Pressure
tau = 0.1    ## Time Constant of Pressure Dynamics
omega = 10    ## Motivation of Pump(related in Target Pressure in Pump)

## Initial Value Settings
u_pump = 0.5 ## Initial Hemolymph in Central Pump
u_leg = 0.1  ## Initial Hemolymph in Leg

p_init = 10  ## Initial Pressure in Body

##########################################################################

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,time,step)


def main():

    u,p = calc_results()
    show_results(u)
    ##show_results(p,ylab="p")


def calc_results():

    u = [[] for _ in range(N+1)] ## u[0] : Central Pump , u[1]~u[N] : Leg
    p = [[] for _ in range(N+1)] ## same as u

    for i in range(step):
        delta_u,delta_p = update_deltas(u,p)
        u[i].append(u[i][-1]+delta_u[i])
        p[i].append(p[i][-1]+delta_p[i])
    
    return u,p


def update_deltas(u,p):

    du = []
    dp = []

    ##du update
    for i in range(N+1):
        if i == 0:##pump
            delta = C*(sum(p[i][-1] for i in range(1,N+1))-N*p[0][-1]) ## d(u_pump)/dt = Σ_i C(p_leg_i - p_pump)
        else:##leg
            delta = C*(p[0][-1]-p[i][-1]) ## d(u_leg_i)/dt = C(p_pump - p_leg)
        du.append(delta)

    ##dp update
    for i in range(N+1):
        if i == 0:##pump
            target_p = omega*(1+np.sin(omega*time[len(p[0])]))
        else:##leg
            target_p =  ## p-model
            ## target_p =  ## u-model

        delta = 1/tau*(p[i][-1]-target_p) ## dp/dt = 1/τ(p_bar - p)
        dp.append(delta+p[i][-1]+a*u[i][-1]) ## p = p_mus + p_elas = (p_mus + Δp_mus) + a*u_i

    return du,dp


def show_results(a,ylab="u"):
    


    plt.xlabel("time(a.u.)")
    plt.ylabel(ylab+"(a.u.)")
    
    for i in range(len(a)):
        if i == 0:
            plot_label = "Central Pump"
        else:
            plot_label = "Leg "+str(i)
        plt.plot(t,a[i],label=plot_label)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()