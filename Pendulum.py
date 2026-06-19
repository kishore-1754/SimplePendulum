## Import libraries
from RungeKutta import IntegrateUsingRK
import numpy as np
from math import sin
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

## Define Pendulum function
def Pendulum(time,state,L=1,g=9.8):
    theta=state[0]
    omega=state[1]
    dtheta=omega
    domega=-(g/L)*sin(theta)         ## θ'' + (g/L)sinθ = 0 and omega is the angular velocity
    return np.array([dtheta,domega],dtype=float)


## Get input values
L=int(input("Enter the length of the string:"))
T=int(input("Enter the pendulum duration in seconds:"))


## Calling functions for getting X and Y coordinates
time,state=IntegrateUsingRK(F=Pendulum,x=0,y=np.array([0.24,0.0],dtype=float),stopx=T,h=0.01,L=L,g=9.8)  ## where state = (theta, omega)
## Since x = L sinθ and y = -L cosθ
x=L*np.sin(state[:,0])
y=-L*np.cos(state[:,0])


## Calling built-in functions for comparision
timeSpan = (0,T)

y0 = [0.24, 0.0] ## Setting theta = 0.24 rad and omega = 0.0 rad / sec

sol = solve_ivp(
    Pendulum,
    t_span=timeSpan,
    y0=y0,
    method='RK45',   # Runge-Kutta method
    t_eval=time,
    args=(L,9.8)
)

thetaB = sol.y[0]
omegaB = sol.y[1]

## Finding error (Builtin - implemented)
error = state[:,0] - thetaB


xB = L * np.sin(thetaB)
yB = -L * np.cos(thetaB)
## Animation using matplotlib

fig, (ax1,ax2) = plt.subplots(2,1)
n = min(len(time), len(sol.t))

## Setting black background
fig.patch.set_facecolor('black')
ax1.set_facecolor('black')

## Creating bob and string before plotting
bBob,=ax1.plot([],[],'o',markersize=10,color="red",alpha=0.5,label="Scipy RK45")
stringB,=ax1.plot([],[],lw=3,color="red",alpha=0.5)
trailB,=ax1.plot([],[],color="red",alpha=0.5)
bob,=ax1.plot([],[],'o',markersize=14,color="#39ff14",label="Custom RK4",alpha=0.7)
string, = ax1.plot([], [], lw=2,color="#39ff14",alpha=0.7)
trail, = ax1.plot([], [], color='#39ff14',alpha=0.5)

## Set x and y axes limits, and horizontal line
ax1.legend()
ax1.set_xlim(-1.2*L,1.2*L)
ax1.set_ylim(-1.2*L,1.2*L)
ax1.axis("off")
ax1.axhline(y=0,color="white",linewidth=2)


## Show the evolution of error with time
errorLine,=ax2.plot([],[],color="red",label="Error")
ax2.set_title("Error v/s time plot")
ax2.legend()
ax2.grid()
ax2.set_xlim(0, T)
ax2.set_ylim(min(error)*1.1, max(error)*1.1)
ax2.set_facecolor('black') ## set black background
ax2.tick_params(colors='white')
ax2.xaxis.label.set_color('white')
ax2.yaxis.label.set_color('white')
ax2.title.set_color('white')
ax2.set_xlabel("Time")
ax2.set_ylabel("Error")
ax2.axhline(y=0,color="white",linewidth=1)

## Updation function using frames
def update(frame):
    bob.set_data([x[frame]],[y[frame]])
    string.set_data([0, x[frame]], [0, y[frame]])
    trail.set_data(x[:frame],y[:frame])
    bBob.set_data([xB[frame]],[yB[frame]])
    stringB.set_data([0,xB[frame]],[0,yB[frame]])
    trailB.set_data(xB[:frame],yB[:frame])

    errorLine.set_data(time[:frame],error[:frame])
    return bob,string,trail,bBob,stringB,trailB,errorLine

ani = FuncAnimation(
    fig,
    update,
    frames=range(0, n, 3),
    interval=10,
    blit=True
)
plt.show()


