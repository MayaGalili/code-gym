# -*- coding: utf-8 -*-
"""
Script Goal:
Given a NXM matrix, print its cell in spiral way.

Created on Tue May 29 10:39:50 2018
@author: Maya Galili
"""

import numpy as np
import time

def index_to_coords(index, rows, cols):
    """Convert row-by-row index to matrix coordinates (row, col)"""
    return index // cols, index % cols

def coords_to_index(row, col, cols):
    """Convert matrix coordinates to row-by-row index"""
    return row * cols + col

def display_matrix(matrix, visited=None, current_cell=None, direction=""):
    """Display the matrix with visual indicators for visited cells"""
    rows, cols = matrix.shape
    
    # Calculate column widths for proper alignment
    max_width = len(str(matrix.max()))
    
    # Create visited set if not provided
    if visited is None:
        visited = set()
    
    print("┌" + "─" * (cols * (max_width + 2) - 1) + "┐")
    
    for i in range(rows):
        print("│", end="")
        for j in range(cols):
            cell_value = matrix[i][j]
            cell_pos = (i, j)
            
            if cell_pos == current_cell:
                # Currently being visited - highlight
                print(f" [{cell_value:>{max_width}}]", end="")
            elif cell_pos in visited:
                # Already visited - mark with brackets
                print(f" [{cell_value:>{max_width}}]", end="")
            else:
                # Not visited yet - normal display
                print(f"  {cell_value:>{max_width}} ", end="")
        print(" │")
    
    print("└" + "─" * (cols * (max_width + 2) - 1) + "┘")
    
    if direction:
        print(f"Direction: {direction}")
    print()

def spiralPrint(a, visual=False):
    
#   init vars
    N,M = a.shape  
    mat_sz = N*M
    i = 0 
    j = 0
    n = 0
    m = 0
    result = []
    visited = set()
    step = 1
    
    if visual:
        print("\n🔄 SPIRAL TRAVERSAL (Visual Step-by-step):")
        print("=" * 50)
        print("Legend: [X] = Visited,  X  = Current,  X  = Not visited")
        print()
        print("Initial matrix:")
        display_matrix(a, visited)
    
    while (mat_sz > 0):
        
#        go right
        if mat_sz > 0:
            if visual:
                print(f"Step {step}: → Moving RIGHT")
            for j in range(m,M) :
                if mat_sz > 0:
                    result.append(a[i][j])
                    visited.add((i, j))
                    if visual:
                        print(f"  Visiting cell ({i},{j}) = {a[i][j]}")
                        display_matrix(a, visited, (i, j), "→ Right")
                        time.sleep(1)
                    mat_sz = mat_sz - 1;
            n=n+1
            if visual:
                step += 1

#        go down  
        if (mat_sz > 0):
            if visual:
                print(f"Step {step}: ↓ Moving DOWN")
            for i in range(n,N) :
                if mat_sz > 0:
                    result.append(a[i][j])
                    visited.add((i, j))
                    if visual:
                        print(f"  Visiting cell ({i},{j}) = {a[i][j]}")
                        display_matrix(a, visited, (i, j), "↓ Down")
                        time.sleep(1)
                    mat_sz = mat_sz - 1;    
            M=M-1   
            if visual:
                step += 1
        
#        go left
        if (mat_sz > 0):           
            if visual:
                print(f"Step {step}: ← Moving LEFT")
            for j in range(M-1,m-1,-1) :  
                if mat_sz > 0:
                    result.append(a[i][j])
                    visited.add((i, j))
                    if visual:
                        print(f"  Visiting cell ({i},{j}) = {a[i][j]}")
                        display_matrix(a, visited, (i, j), "← Left")
                        time.sleep(1)
                    mat_sz = mat_sz - 1           
            N=N-1 
            if visual:
                step += 1

#        go up     
        if (mat_sz > 0):            
            if visual:
                print(f"Step {step}: ↑ Moving UP")
            for i in range(N-1,n-1,-1) :         
                if mat_sz > 0:
                    result.append(a[i][j])
                    visited.add((i, j))
                    if visual:
                        print(f"  Visiting cell ({i},{j}) = {a[i][j]}")
                        display_matrix(a, visited, (i, j), "↑ Up")
                        time.sleep(1)
                    mat_sz = mat_sz - 1;   
            m=m+1
            if visual:
                step += 1
    
    if visual:
        print("✅ Spiral traversal complete!")
        print(f"Final result: {' '.join(map(str, result))}")
        print()
    
    return result


# Driver Code
if __name__ == "__main__":
    a = np.array([
        [1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18], 
        [19, 20, 21, 22, 23, 24]
        ])
        
    result = spiralPrint(a)
    print(" ".join(map(str, result)))