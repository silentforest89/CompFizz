#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title:---------- GrowDendrite - Grid class

Created on Mon Jul  1 13:13:23 2019

Author:---------Ty Sterling
Contact:--------ty.sterling@colorado.edu
Instituion:-----University of Colorado Boulder
Department:-----Material Science & Physics

Description: Creat a square grid to launch the 'doodlebug' or 
    random walking particle on. The grid stores which site are 
    filled (!= 0) or empty (== 0)

"""

import numpy as np

class grid:
    """
    A square grid with area == edge_length*edge_length.

    the seed method allows one to specify an arbitrary point
    on the grid to be initially filled. You can place as many
    seeds as you want!

    """
    def __init__(self,edge_length):
        self.grid = np.zeros((edge_length,edge_length))
    
    def seed(self,colindex,rowindex):
        self.grid[colindex,rowindex] = 1
