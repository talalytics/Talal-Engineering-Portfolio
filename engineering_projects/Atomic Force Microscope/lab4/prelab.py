
import numpy as np
from numpy import array
from numpy import sign
import matplotlib.pyplot as plt



def f(i,x2,a_max):
    if sign(x2[i]) != -1:
        val = -0.5 * (x2[i]**2)/(1*a_max)
    else:
        val = -0.5 * (x2[i]**2)/(-1*a_max)
    return val

def trap_traj(a_max,v_max,x_end,f_s):
    dt = 1/f_s
    i = 0
    x_t = 0 # initialize as x_start
    v_t = 0 # intialize initial velocity
    x1 = [x_t - x_end]
    x2 = [v_t]
    a = [0]
    tol = 1e-11
    while(True):
        x2[i]
        if x1[i] < f(i,x2,a_max):
            if x2[i] < v_max:
                a[i] = a_max
            else:
                a[i] = 0
        else:
            if x2[i] > -v_max:
                a[i] = -a_max
            else:
                a[i] = 0
        
        x2.append(x2[i] + a[i]*dt)
        a.append(a[i])
        x1.append(x1[i] + x2[i+1]*dt)
        i +=1
        if x2[i] == 0 and abs(x1[i]) < tol:
            break
    vec = np.array([x1,x2,a]) # x1, x2, and acceleration points
    return vec
def main():
    output = trap_traj(320000,64000,12800,2000)
    
    disp = output[0] + 12800 # note that output 0 is negative tracking error
    velo = output[1]
    acc = output[2]
    time = np.arange(0,len(disp),1) * 1/2000 # index * sampling perior
    
    fig, axs = plt.subplots(3)
    fig.suptitle('Trapezoidal Trajectory Plots')
    plt.subplots_adjust(left=0.1,bottom=0.1,right=0.9,top=0.9,wspace=0.4,
                    hspace=0.4) # plot spacing
    

    axs[0].plot(time,disp)
    axs[0].set_title('Displacement')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Pulses')
    
    axs[1].plot(time, velo)
    axs[1].set_title('Velocity')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Pulses/sec')
    
    
    axs[2].plot(time,acc)
    axs[2].set_title('Acceleration')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Pulses/(sec^2)')
    
main()
    

            
                
        
        