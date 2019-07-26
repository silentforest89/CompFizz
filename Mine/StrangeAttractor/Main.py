import numpy as np
import matplotlib.pyplot as plt
import Duffing

### time step, number of steps
dt = 0.0005
steps = int(100e3)
time = np.arange(0,steps)*dt

### initial conditions
particle_1 = Duffing.particle(
        position=0.5,
        velocity=0.0,
        mass=1.0,
        a=0.25,
        b=0.5,
        f0=2.0,
        omega=2.4,
        gamma=0.1)
particle_2 = Duffing.particle(
        position=0.5001,
        velocity=0.0,
        mass=1.0,
        a=0.25,
        b=0.5,
        f0=2.0,
        omega=2.4,
        gamma=0.1)

### data arrays
velocity_1 = np.zeros(steps)
position_1 = np.zeros(steps)
force_1 = np.zeros(steps)

velocity_2 = np.zeros(steps)
position_2 = np.zeros(steps)
force_2 = np.zeros(steps)

velocity_1[0] = particle_1.velocity
position_1[0] = particle_1.position
force_1[0] = particle_1.force

velocity_2[0] = particle_2.velocity
position_2[0] = particle_2.position
force_2[0] = particle_2.force

### integrate
for i in range(1,steps):
    particle_1.runge_kutta(dt)
    particle_2.runge_kutta(dt)

    velocity_1[i] = particle_1.velocity
    position_1[i] = particle_1.position
    force_1[i] = particle_1.force

    velocity_2[i] = particle_2.velocity
    position_2[i] = particle_2.position
    force_2[i] = particle_2.force

### save the data
data = np.append(time.reshape(steps,1),position_1.reshape(steps,1),axis=1)
data = np.append(data,velocity_1.reshape(steps,1),axis=1)
data = np.append(data,position_2.reshape(steps,1),axis=1)
data = np.append(data,velocity_2.reshape(steps,1),axis=1)
np.savetxt('duffing.csv',data)

### plot
fig, ax = plt.subplots()
fig.set_size_inches(5,4,forward=True)
fig.tight_layout(pad=2.5)

ax.plot(time,position_1,'r',lw=1.5,label=r'$x_0$=0.5')
ax.plot(time,position_2,'b',lw=1.5,label=r'$x_0$=0.5001')

# configure the plot
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(1.5)

ax.set_ylim(-3,3)
#ax.set_xlim(-0.02,0.52)

ax.minorticks_on()
ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=5)
ax.tick_params(which='minor', length=3, color='k')
ax.set_xlabel('time',labelpad=4,fontweight='normal',
              fontsize='large')
ax.set_ylabel('position',labelpad=4,fontweight='normal',
              fontsize='large')
ax.legend(frameon=False,prop={'size':'small'},ncol=2)
fig.suptitle('Duffing Oscillator',y=0.97)
plt.savefig('duffing.png',format='png',dpi=300,bbox_inches='tight')
plt.show()

