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
    
class particle:
    def __init__(self,grid,starting_edge='random',starting_point='random'):
        self.edge_len = len(grid.grid[:,0])
        
        # if 'None', randomly choose a starting point along the specified edge
        if starting_point == 'random':
            starting_point = np.random.randint(0,self.edge_len)

        if starting_edge == 'random': # launch from a random edge
            edge = np.random.randint(1,5)
            if edge == 1: # top
                self.coord = [0,starting_point]
            elif edge == 2: # bottom
                self.coord = [self.edge_len-1,starting_point]
            elif edge == 3: # left
                self.coord = [starting_point,0]
            else: # right
                self.coord = [starting_point,self.edge_len-1]
        elif starting_edge == 'top': # only launch from the top
            self.coord = [0,starting_point]
        elif starting_edge == 'bottom': # only launch from bottom
            self.coord = [self.edge_len-1,starting_point]
        elif starting_edge == 'left': # only launch from the left
            self.coord = [starting_point,0]
        else: # only launch from the right
            self.coord = [starting_point,self.edge_len-1]
    
            
    def random_walk(self,grid):
        # check if neighbor is filled or if on an edge or corner before moving
        if self.coord[0] == 0: # on top edge
            if self.coord[1] == 0: # top left corner
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [2,3]
                
            elif self.coord[1] == self.edge_len-1: # top right corner
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [3,4]
                
            else: # somewhere on the top edge
                if grid.grid[self.coord[0]+1,self.coord[1]] != 0:
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [2,3,4]
                
        elif self.coord[0] == self.edge_len-1: # on bottom edge
            if self.coord[1] == 0: # bottom left corner
                if (grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,2]
                
            elif self.coord[1] == self.edge_len-1: # bottom right corner
                if (grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,4]
                
            else: # somewhere on the bottom edge
                if grid.grid[self.coord[0]-1,self.coord[1]] != 0:
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,2,4]
                
        else: # not on top or bottom edge
            if self.coord[1] == 0: # somewhere on left edge
                if grid.grid[self.coord[0],self.coord[1]+1] != 0:
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,2,3]
                
            elif self.coord[1] == self.edge_len-1: # somewhere on right edge
                if grid.grid[self.coord[0],self.coord[1]-1] != 0:
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,3,4]
                
            else:
                if (grid.grid[self.coord[0]+1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0]-1,self.coord[1]] != 0 or
                    grid.grid[self.coord[0],self.coord[1]-1] != 0 or
                    grid.grid[self.coord[0],self.coord[1]+1] != 0):
                    grid.grid[self.coord[0],self.coord[1]] = grid.grid.max()+1
                    return True
                allowed_steps = [1,2,3,4]
            
        # randomly select the next step out of allowed steps
        np.random.shuffle(allowed_steps)
        step = allowed_steps[0]
        
        if step == 1: # go up
            self.coord[0] = self.coord[0]-1
        elif step == 2: # go right
            self.coord[1] = self.coord[1]+1
        elif step == 3: # go down
            self.coord[0] = self.coord[0]+1
        else: # go left
            self.coord[1] = self.coord[1]-1
            
        return False
        

        
