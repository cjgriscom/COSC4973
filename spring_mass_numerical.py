# filename: spring_mass.py
# author: Daniel Barnette
# date: Aug 25, 2016
#
# purpose: plot the exact solution for a spring-mass system
#======================================

# imports
import matplotlib.pyplot as plt	    # for plots
#from pylab import plot,show, title, xlabel, ylabel, legend, savefig
import pylab                        # for plot labels, legends, etc)
import math						    # for sines, cosines, and other math functions

# define Booleans
DEBUG = True
DEBUG = False

# define constants
timeStart = 0.0  					# seconds
timeEnd = 10.0						# seconds
uZero = 0.							# inches, initial displacement
vZero = 10.0						# inches/second, initial velocity
naturalPeriod = 2.					# seconds/cycle, natural frequency
omegaN = 2.*math.pi/naturalPeriod	# radians/second, undamped circular natural frequency
deltaT = 0.0001						# seconds, time step for plotting exact equation
deltaTN = 0.0001                       # seconds, time step for marching approximate numerical equation

# exact equation
def exact(time, uZero, vZero, omegaN):
    u = uZero*math.cos(omegaN*time) + (vZero/omegaN)*math.sin(omegaN*time)
    return u

# numerical equation
def approximate(omegaN, u, udot, deltaTN):
    udotNew =  udot - deltaTN*omegaN**2*u
    uNew = u + deltaTN*udot
    return (uNew, udotNew)
    
# main program

# EXACT SOLUTION

# define lists for storing plot variables
time = []
u = []

# initial value for u at time t=0
uDisplacement = exact(0,uZero,vZero,omegaN)

# store plot variable
time.append(timeStart)
u.append(uDisplacement)

# loop until finished
t = timeStart
while t < timeEnd + 0.001 :
    t = t + deltaT
    uDisplacement = exact(t,uZero,vZero,omegaN)
    time.append(t)
    u.append(uDisplacement)
    
if DEBUG:
    print('time:\n')
    print(time)
    print()
    print('u:\n')
    print(u)
    print()
    
# NUMERICAL SOLUTION
# define lists for storing plot variables
timeN = []
uNum = []
udotNum = []

# stor initial plot variables
timeN.append(timeStart)
uNum.append(uZero)
udotNum.append(vZero)

# loop until finished
t = timeStart
uN = uZero
udotN = vZero
while t < timeEnd + 0.001:
    t = t + deltaTN
    (uNDisplacement, vNDisplacement) = approximate(omegaN, uN, udotN, deltaTN)
    timeN.append(t)
    uNum.append(uNDisplacement)
# reset variables for next iteration
    uN = uNDisplacement
    udotN = vNDisplacement

# plot the exact results
pylab.title('Position of Mass vs Time, dt = %s sec dtN = %s sec' % (deltaT,deltaTN))
pylab.xlabel('Time (sec)')
pylab.ylabel('Position (inches)')
pylab.grid('on')
filename1 = 'graph_position_vs_time_dt_'+str(deltaT)+'_dtN_'+str(deltaTN)+'_sec.png'
plt.plot(time,u,color='r')
plt.plot(timeN,uNum,color='b')
pylab.legend(['exact','approx'],loc='best')
pylab.savefig(filename1)
plt.show()


# indicate end of program
print('\n --- Program spring_mass.py ended successfully ---\n')
