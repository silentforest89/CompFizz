import numpy as np
import matplotlib.pyplot as plt
import Duffing

data = np.loadtxt('duffing.csv')

### plot
fig, ax = plt.subplots()
fig.set_size_inches(6,4,forward=True)
fig.tight_layout(pad=2.5)

#ax.plot(data[:,0],data[:,1],'r',lw=1.5,label=r'$x_0$=0.5')
#ax.plot(data[:,0],data[:,3],'b',lw=1.5,label=r'$x_0$=0.5001')

ax.scatter(data[:,1],data[:,2],s=1)

# configure the plot
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(1.5)

#ax.set_ylim(0,80)
#ax.set_xlim(-0.02,0.52)

ax.minorticks_on()
ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=5)
ax.tick_params(which='minor', length=3, color='k')
ax.set_xlabel('Position',labelpad=4,fontweight='normal',
              fontsize='large')
ax.set_ylabel('Momentum',labelpad=4,fontweight='normal',
              fontsize='large')
ax.legend(frameon=False,prop={'size':'small'},ncol=2)
fig.suptitle('Strange Attractor',y=0.97)
#plt.savefig('strange_attractor.png',format='png',dpi=300,bbox_inches='tight')
plt.show()

