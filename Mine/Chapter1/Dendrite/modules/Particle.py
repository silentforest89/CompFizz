#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:---------- GrowDendrite - Particle class

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: Initialize a 'doodlebug' or random-walking particle on a 
    square grid.

"""

import numpy as np
    
class particle: 

    """
    Initialization takes 2 arguments:
    1: the grid
    2: params: i.e. the simulation parameters. Within params are:
        1: num_particles. The number of particles to be launched. This is used
            to creat an array to store the arrival rates.
        2: starting_edge. it can be 'random' so that the particle starts
            on a random edge or 'top', 'bottom', 'left', or 'right'. These
            will start it on the specified edge. OR it can be an integer,
            in which case it will be used as the index within a column to start
            the particle on.
        3: starting_point. it can be 'random' so that a random point is chosen
            along the 'starting_edge' above, or it can be an integer so the 
            particle will start at the specified along the starting edge.
            Note that if 'starting_edge' is an integer, starting_point is the 
            index within a row so that the starting_edge=INTEGER, 
            starting_point=INTEGER pair form indicies to initialize that particle 
            at an arbitrary point on the grid.
        4: step. this can be 'rectilinear' or 'euclidean'. If rectilinear is 
            chosen, the particle can only step in the +/-x and +/-y directions.
            It CANNOT step along a diagonal. Note also that it wont 'land' if there
            is a filled site along a diagonal: only when a filled site is along
            +/-x or +/-y. If euclidean is chosen, the particle can step along 
            diagonals in addition to the rectilinear step options. It can also 
            'land' when a neighbor is full.
    """

    def __init__(self,grid,params):
        """
        See the docstring for the class definition.
        """
        self.edge_len = params.gridsize
        self.step = params.step
        self.num_particles = params.num_particles
        
        ### if 'random', randomly choose a starting point along the specified edge
        if params.starting_point == 'random':
            starting_point = np.random.randint(0,self.edge_len)
        else:
            starting_point = params.starting_point

        ### select an edge to launch from or an arbitrary point 
        if params.starting_edge == 'random': # launch from a random edge
            edge = np.random.randint(1,5)
            if edge == 1: # top
                self.coord = [0,starting_point]
            elif edge == 2: # bottom
                self.coord = [self.edge_len-1,starting_point]
            elif edge == 3: # left
                self.coord = [starting_point,0]
            else: # right
                self.coord = [starting_point,self.edge_len-1]
        elif params.starting_edge == 'top': # only launch from the top
            self.coord = [0,starting_point]
        elif params.starting_edge == 'bottom': # only launch from bottom
            self.coord = [self.edge_len-1,starting_point]
        elif params.starting_edge == 'left': # only launch from the left
            self.coord = [starting_point,0]
        elif params.starting_edge == 'right': # only launch from the right
            self.coord = [starting_point,self.edge_len-1]

        ### hack to allow arbitrary staring position
        else: # starting_edge is the row, starting_point is the column
            self.coord = [params.starting_edge,starting_point]
    

    ###############################################################################
    def check_neighbors(self,grid):
        """
        check if a neighboring site is full and break the random_walk loop if it is.
        """
        ### check if neighbors along diaganol are filled
        if self.step == 'euclidean':
            if self.coord[0] == 0: # on top edge
                if self.coord[1] == 0: # top left corner
                    if (grid.grid[self.coord[0]+1,self.coord[1]+1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                elif self.coord[1] == self.edge_len-1: # top right corner
                    if (grid.grid[self.coord[0]+1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                else: # somewhere on the top edge
                    if (grid.grid[self.coord[0]+1,self.coord[1]+1] != 0 or
                        grid.grid[self.coord[0]+1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
            elif self.coord[0] == self.edge_len-1: # on bottom edge
                if self.coord[1] == 0: # bottom left corner
                    if (grid.grid[self.coord[0]-1,self.coord[1]+1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                elif self.coord[1] == self.edge_len-1: # bottom right corner
                    if (grid.grid[self.coord[0]-1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                else: # somewhere on the bottom edge
                    if (grid.grid[self.coord[0]-1,self.coord[1]+1] != 0 or 
                        grid.grid[self.coord[0]-1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
            else: # not on top or bottom edge
                if self.coord[1] == 0: # somewhere on left edge
                    if (grid.grid[self.coord[0]-1,self.coord[1]+1] != 0 or
                        grid.grid[self.coord[0]+1,self.coord[1]+1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                elif self.coord[1] == self.edge_len-1: # somewhere on right edge
                    if (grid.grid[self.coord[0]+1,self.coord[1]-1] != 0 or 
                        grid.grid[self.coord[0]-1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True
                else:
                    if (grid.grid[self.coord[0]+1,self.coord[1]+1] != 0 or
                        grid.grid[self.coord[0]+1,self.coord[1]-1] != 0 or
                        grid.grid[self.coord[0]-1,self.coord[1]+1] != 0 or
                        grid.grid[self.coord[0]-1,self.coord[1]-1] != 0):
                        grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                        return True

        ### check is neighbors along cartesian axes are filled
        ### have to check these for rectilinear and euclidean
        if self.coord[0] == 0: # on top edge
            if self.coord[1] == 0: # top left corner
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            elif self.coord[1] == self.edge_len-1: # top right corner
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            else: # somewhere on the top edge
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
        elif self.coord[0] == self.edge_len-1: # on bottom edge
            if self.coord[1] == 0: # bottom left corner
                if (grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            elif self.coord[1] == self.edge_len-1: # bottom right corner
                if (grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            else: # somewhere on the bottom edge
                if (grid.grid[self.coord[0]-1,self.coord[1]] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
        else: # not on top or bottom edge
            if self.coord[1] == 0: # somewhere on left edge
                if (grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            elif self.coord[1] == self.edge_len-1: # somewhere on right edge
                if (grid.grid[self.coord[0],self.coord[1]-1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
            else:
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True


    ###############################################################################
    def random_walk(self,grid):
        """
        random walk (either rectilinear or euclidean steps, see the class docstring)
        until it lands next to a filled site. It calls 'check_neighbors' to determine
        if a neighboring site is filled.
        """
        
        ### check if neighbor is filled or if on an edge or corner before moving
        if self.check_neighbors(grid) == True:
            return True

        ### pick allowable steps, i.e. cant step off the edge
        if self.coord[0] == 0: # on top edge
            if self.coord[1] == 0: # top left corner
                row_steps = [0,1]
                col_steps = [0,1]
            elif self.coord[1] == self.edge_len-1: # top right corner
                row_steps = [-1,0]
                col_steps = [0,1]
            else: # somewhere on the top edge
                row_steps = [-1,0,1]
                col_steps = [0,1]
        elif self.coord[0] == self.edge_len-1: # on bottom edge
            if self.coord[1] == 0: # bottom left corner
                row_steps = [0,1]
                col_steps = [-1,0]
            elif self.coord[1] == self.edge_len-1: # bottom right corner
                row_steps = [-1,0]
                col_steps = [-1,0]
            else: # somewhere on the bottom edge
                row_steps = [-1,0,1]
                col_steps = [-1,0]
        else: # not on top or bottom edge
            if self.coord[1] == 0: # somewhere on left edge
                row_steps = [0,1]
                col_steps = [-1,0,1]
            elif self.coord[1] == self.edge_len-1: # somewhere on right edge
                row_steps = [-1,0]
                col_steps = [-1,0,1]
            else:
                row_steps = [-1,0,1]
                col_steps = [-1,0,1]

        ### randomly sample the next step
        if self.step == 'rectilinear':
            choice = np.random.choice([0,1])
            if choice == 0: # take a random x-step
                self.coord[1] = self.coord[1]+np.random.choice(row_steps)
            if choice == 1: # take a random y-step
                self.coord[0] = self.coord[0]+np.random.choice(col_steps)
        else:                        
            self.coord[1] = self.coord[1]+np.random.choice(row_steps) # x-step
            self.coord[0] = self.coord[0]+np.random.choice(col_steps) # y-step
        
        return False
         
