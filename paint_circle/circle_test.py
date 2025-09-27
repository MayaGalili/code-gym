# -*- coding: utf-8 -*-
"""
Function goal is to generate a circle with R as a radius around cell (x0,y0),
on matrix M.

Created on Tue Jul  3 15:46:17 2018
@author: Maya Galili
"""
import numpy as np

''' init step '''
def paint_circle(M, R, x0,y0):
    get_next_best_cell(x0,y0, x0-R,y0,R,M,3)
    
''' recursive step'''
def get_next_best_cell(x0,y0, x1,y1,R,M,pos_flag):
    pos_arr = calc_pos_arr( x1,y1,pos_flag)
    dist_arr = np.array([find_dist(x0,y0,x2,y2) for (x2,y2) in pos_arr])   
    pos_idx = np.argmin(abs(dist_arr - R))
    
    # change direction if needed
    if pos_idx == 3:
        pos_flag = (pos_flag+1)%4
    [x1,y1] = pos_arr[pos_idx]
    
    # stop condition
    if M[x1,y1] == 1:
        return M
    else:
        M[x1,y1] = 1
        get_next_best_cell(x0,y0, x1,y1,R,M,pos_flag)

''' pythagoras function '''
def find_dist(x0,y0,x2,y2):
    r=((x2-x0)**2+(y2-y0)**2)**0.5
    return r

''' calculate the positions array according to given direction'''
def calc_pos_arr(x1,y1, pos_flag):
    if pos_flag == 0: #down
        pos_arr =  [(x1+1,y1-1),(x1+1, y1), (x1+1,y1+1), (x1,y1+1)]
    elif pos_flag == 1: #right
        pos_arr =  [(x1+1,y1+1),(x1,y1+1), (x1-1,y1+1), (x1-1,y1)]
    elif pos_flag == 2: #up
        pos_arr = [(x1-1,y1+1),(x1-1,y1), (x1-1, y1-1),(x1,y1-1)]
    elif pos_flag == 3: #left
        pos_arr = [(x1-1,y1-1),(x1,y1-1), (x1+1,y1-1), (x1+1,y1)]
    return pos_arr


''' running example '''
R=5
[x0, y0]=(15,15)
M=np.zeros((50,50))
paint_circle(M, R, x0, y0)