# -*- coding: utf-8 -*-
"""
Function goal is to generate a circle with R as a radius around cell (x0,y0),
on matrix M.

Created on Tue Jul  3 15:46:17 2018
@author: Maya Galili
"""
import numpy as np
import matplotlib.pyplot as plt

''' init step '''
def paint_circle(M, R, x0, y0):
    # Mark the center point
    M[x0, y0] = 1
    # Start drawing the circle
    get_next_best_cell(x0, y0, x0-R, y0, R, M, 3)
    return M
    
''' recursive step'''
def get_next_best_cell(x0, y0, x1, y1, R, M, pos_flag):
    # Check bounds
    if x1 < 0 or x1 >= M.shape[0] or y1 < 0 or y1 >= M.shape[1]:
        return M
    
    pos_arr = calc_pos_arr(x1, y1, pos_flag)
    # Filter out positions that are out of bounds
    valid_positions = []
    for (x2, y2) in pos_arr:
        if 0 <= x2 < M.shape[0] and 0 <= y2 < M.shape[1]:
            valid_positions.append((x2, y2))
    
    if not valid_positions:
        return M
    
    dist_arr = np.array([find_dist(x0, y0, x2, y2) for (x2, y2) in valid_positions])   
    pos_idx = np.argmin(abs(dist_arr - R))
    
    # change direction if needed
    if pos_idx == 3:
        pos_flag = (pos_flag + 1) % 4
    [x1, y1] = valid_positions[pos_idx]
    
    # stop condition - if we've already visited this cell
    if M[x1, y1] == 1:
        return M
    else:
        M[x1, y1] = 1
        return get_next_best_cell(x0, y0, x1, y1, R, M, pos_flag)

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


def print_circle_text(M, center_x, center_y):
    """Print the circle as text using characters"""
    print(f"Circle with center at ({center_x}, {center_y}):")
    print("=" * (M.shape[1] + 2))
    for i in range(M.shape[0]):
        print("|", end="")
        for j in range(M.shape[1]):
            if M[i, j] == 1:
                print("●", end="")  # Filled circle for marked cells
            else:
                print(" ", end="")  # Space for empty cells
        print("|")
    print("=" * (M.shape[1] + 2))

def plot_circle(M, center_x, center_y, radius):
    """Plot the circle using matplotlib"""
    plt.figure(figsize=(8, 8))
    plt.imshow(M, cmap='Blues', origin='upper')
    plt.plot(center_y, center_x, 'ro', markersize=8, label=f'Center ({center_x}, {center_y})')
    plt.title(f'Circle with radius {radius}')
    plt.xlabel('Y coordinate')
    plt.ylabel('X coordinate')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.colorbar(label='Cell value')
    plt.show()

''' running example '''
if __name__ == "__main__":
    R = 5
    x0, y0 = 15, 15
    M = np.zeros((50, 50))
    
    print("Drawing circle...")
    M = paint_circle(M, R, x0, y0)
    
    # Print text representation
    print_circle_text(M, x0, y0)
    
    # Show matplotlib plot
    plot_circle(M, x0, y0, R)
    
    # Print some statistics
    marked_cells = np.sum(M == 1)
    print(f"\nCircle statistics:")
    print(f"Radius: {R}")
    print(f"Center: ({x0}, {y0})")
    print(f"Number of marked cells: {marked_cells}")