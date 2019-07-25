#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:----------(type name of code here)

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: (type code or project description here!)

"""

import numpy as np
import Grid 
import Walker
import matplotlib.pyplot as plt

# size of square grid
gridsize = 101
# number of particles 
numwalkers = 2500

# create the grid
grid = Grid.grid(gridsize)

# loop over the particles
for i in range(numwalkers):
    print('\n\tNow on walker {} out of {}\n'.format(i+1,numwalkers))

    # initialize the particle on a grid edge
    walker = Walker.walker(grid)

    # random walk until it runs into a filled grid element
    exitflag = True
    while exitflag == True:
        exitflag = walker.walk(grid)

# save the last run for plotting again
np.savetxt('last_run.csv',grid.grid)

# shift all non-zero data to a large number for use with imshow
mask = (grid.grid != 0).astype(int)*1000

# plot it all
fig, ax = plt.subplots()
ax.imshow(grid.grid+mask,cmap='magma')
for axis in ['top','bottom','left','right']:
  ax.spines[axis].set_linewidth(1.5)
ax.minorticks_on()
ax.tick_params(which='both', width=1)
ax.tick_params(which='major', length=5)
ax.tick_params(which='minor', length=3, color='k')
ax.set_xlabel('X-coord',labelpad=4,fontweight='normal',
              fontsize='large')
ax.set_ylabel('Y-coord',labelpad=3,fontweight='normal',
              fontsize='large')
fig.suptitle('N = {}, Grid = {}x{}'
             .format(numwalkers,gridsize,gridsize),y=0.95)
plt.savefig('dendrite.png',format='png',dpi=300,bbox_inches='tight')
plt.show()

