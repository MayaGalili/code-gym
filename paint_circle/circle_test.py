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

def get_user_input():
    """Get user input for circle parameters"""
    print("=" * 50)
    print("CIRCLE DRAWING PROGRAM")
    print("=" * 50)
    
    while True:
        try:
            # Get radius
            R = int(input("Enter the radius of the circle (1-20): "))
            if 1 <= R <= 20:
                break
            else:
                print("Please enter a radius between 1 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get matrix size
    while True:
        try:
            size = int(input("Enter the matrix size (20-100, default 50): ") or "50")
            if 20 <= size <= 100:
                break
            else:
                print("Please enter a size between 20 and 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get center coordinates
    while True:
        try:
            x0 = int(input(f"Enter X coordinate for center (0-{size-1}, default {size//2}): ") or str(size//2))
            y0 = int(input(f"Enter Y coordinate for center (0-{size-1}, default {size//2}): ") or str(size//2))
            if 0 <= x0 < size and 0 <= y0 < size:
                break
            else:
                print(f"Please enter coordinates within the matrix bounds (0-{size-1}).")
        except ValueError:
            print("Please enter valid numbers.")
    
    # Check if circle fits in matrix
    if x0 - R < 0 or x0 + R >= size or y0 - R < 0 or y0 + R >= size:
        print(f"Warning: Circle with radius {R} at center ({x0}, {y0}) may not fit completely in {size}x{size} matrix.")
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            return get_user_input()  # Restart input
    
    return R, x0, y0, size

def main():
    """Main function with user interface"""
    try:
        # Get user input
        R, x0, y0, size = get_user_input()
        
        # Create matrix
        M = np.zeros((size, size))
        
        print(f"\nDrawing circle with radius {R} at center ({x0}, {y0})...")
        M = paint_circle(M, R, x0, y0)
        
        # Ask user what they want to see
        print("\nWhat would you like to see?")
        print("1. Text representation")
        print("2. Matplotlib plot")
        print("3. Both")
        
        while True:
            choice = input("Enter your choice (1-3): ")
            if choice in ['1', '2', '3']:
                break
            print("Please enter 1, 2, or 3.")
        
        if choice in ['1', '3']:
            print_circle_text(M, x0, y0)
        
        if choice in ['2', '3']:
            plot_circle(M, x0, y0, R)
        
        # Print statistics
        marked_cells = np.sum(M == 1)
        print(f"\nCircle statistics:")
        print(f"Radius: {R}")
        print(f"Center: ({x0}, {y0})")
        print(f"Matrix size: {size}x{size}")
        print(f"Number of marked cells: {marked_cells}")
        
        # Ask if user wants to try again
        while True:
            again = input("\nWould you like to draw another circle? (y/n): ").lower()
            if again in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")
        
        if again == 'y':
            main()
        else:
            print("Goodbye!")
            
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")

''' running example '''
if __name__ == "__main__":
    main()