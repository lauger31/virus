#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#simple epidemic model


Ndays3=90
Ndays2=60
Ndays1=30
#timestep in day
dt=0.01
#contagion time
Tcontagious=10
#contagisosity ratio in person/person
#Acontagious/Tcontagious is the contagious rate in person/day
#Acontagious is given in argument to step

def step(Acontagious):
    x[i+1]=x[i]+Acontagious/Tcontagious*dt*x[i]
    y[i+1]=Acontagious/Tcontagious*dt*x[i]
    if i>Ncontagious:
        x[i+1]=x[i+1]-y[i-Ncontagious-1]
    if x[i+1]<0:
        x[i+1]=0

Ncontagious=int(Tcontagious/dt)
N=int(Ndays3/dt)+1
x=np.zeros(N)
y=np.zeros(N)
print(N)
x[0]=1
x[0]=1
N1=int(Ndays1/dt)
N2=int(Ndays2/dt)
N3=int(Ndays3/dt)
#phase 1 epidemy high contagious rate
for i in range(0,N1):
    step(3.)
#phase 2 epidemy confinement cantagious rate is divided by 10
for i in range(N1,N2):
    step(0.3)
#phase 3 epidemy confinement cantagious rate is maintained below 1
for i in range(N2,N3):
    step(0.9)
plt.plot(x)
plt.show()


