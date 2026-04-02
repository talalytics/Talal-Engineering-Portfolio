
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

MagnitudePlant= pd.read_csv("manitude_double_intergrator_plant.csv")
PhasePlant = pd.read_csv("phase_double_intergrator_plant.csv")

MagnitudeLoop= pd.read_csv("magnitude_double_intergrator_loop.csv")
PhaseLoop = pd.read_csv("phase_double_integrator_loop.csv")

list(MagnitudePlant)
list(PhasePlant)
list(MagnitudeLoop)
list(PhaseLoop)

freq_Plant = np.array(MagnitudePlant['Frequency (Hz) - y0 (u0)'])
mag_Plant = np.array(MagnitudePlant['Magnitude (abs) - y0 (u0)'])
phase_Plant = np.array(PhasePlant['Phase (deg) - y0 (u0)'])

freq_Loop = np.array(MagnitudeLoop['Frequency (Hz) - y0 (u0)'])
mag_Loop = np.array(MagnitudeLoop['Magnitude (abs) - y0 (u0)'])
phase_Loop = np.array(PhaseLoop['Phase (deg) - y0 (u0)'])

#Plant

fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig1.suptitle('Frequency Response Plant', fontsize=16)
   

ax1.semilogx(freq_Plant,20*np.log10(mag_Plant),'.b')
ax2.semilogx(freq_Plant,phase_Plant,'.r')


ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('Magnitude [dB]')

ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('degrees °')


plt.show()

#Loop

fig2, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
fig2.suptitle('Frequency Response Loop', fontsize=16)
   

ax1.semilogx(freq_Loop,20*np.log10(mag_Loop),'.b')
ax2.semilogx(freq_Loop,phase_Loop,'.r')


ax1.set_xlabel('Frequency [Hz]')
ax1.set_ylabel('Magnitude [dB]')

ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('degrees °')


plt.show()


# step response

CloseLoop= pd.read_csv("double_intergrator_close_loop_step_response.csv")

list(CloseLoop)

time = np.array(CloseLoop['Time - Plot 1'])
amp = np.array(CloseLoop['Amplitude - Plot 1'])
square_input = np.array(CloseLoop['Amplitude - Plot 0'])

# for i in range(len(time)):
#     time[i]=(time[i]-time[0])/500
# for j in range (len(time)):
#     if time[j]>=16:
        
    
    
    
fig_step = plt.figure(figsize = (15,15))
plt.xlabel('time [s]')
plt.ylabel('output voltage, V0 [V]')
plt.title('Step Response of the Close Loop')
plt.xticks(np.arange(min(time), max(time)+0.01, 0.05))

plt.plot(time,square_input,'g-', label = 'square wave input')
plt.plot(time,amp, label = 'output (step response)')

# plt.grid()
plt.show()




