import numpy as np
import matplotlib.pyplot as plt

eps = 10**-9

def f(x):

    ##return x**2+2*x-1
    return np.log(x)

def f_dash(x):

    ##return 2*x + 2
    return 1/x

def bisection_method(left,right):

    r = right
    l = left
    m = (r+l)/2
    step = [m]

    while abs(f(m)) > eps:
        if f(m)*f(l) < 0:
            r = m
        else:
            l = m
        step.append(m)
        m = (r+l)/2

    return step

def newton_method(start):

    a = start
    step = [a]

    while True:
        x = a - f(a)/f_dash(a)
        step.append(x)
        if abs(x-a) < eps:
            break
        a = x

    return step

def secant_method(left,right):

    r = right
    l = left
    step = [r]

    while True:
        x = r - f(r)*(r-l)/(f(r)-f(l))
        step.append(x)
        if abs(x-r) < eps:
            break
        r,l = x,r

    
    return step

def show_res(l,r):

    ##行数を一致させる処理
    bisection = bisection_method(l,r)
    newton = newton_method((l+r)/2)
    secant = secant_method(l,r)

    values = [len(bisection)-1,len(newton)-1,len(secant)-1]
    max_length = max(len(bisection),len(newton),len(secant))

    for _ in range(max_length-len(bisection)):
        bisection.append(np.nan)
    
    for _ in range(max_length-len(newton)):
        newton.append(np.nan)
    
    for _ in range(max_length-len(secant)):
        secant.append(np.nan)

    steps = [i+1 for i in range(max_length)]

    plt.plot(steps,bisection,label="bisection",marker="o")
    plt.plot(steps,newton,label="newton",marker="o")
    plt.plot(steps,secant,label="secant",marker="o")
    plt.title("Step-Value")
    plt.ylabel("value")
    plt.xlabel("step")
    plt.legend()
    plt.show()

    labels = ["bisection","newton","secant"]
    plt.bar(labels,values)
    plt.title("Calculation Steps")
    plt.ylabel("steps")
    plt.show()


if __name__ == "__main__":
    print("Enter l and r :",end=" ")
    l,r = map(float,input().split())
    show_res(l,r)



