# -*- coding: utf-8 -*-
"""
Interactive UI for Spiral Matrix Printer

This module provides a user-friendly interface for the spiral matrix printer,
allowing users to configure matrix size and display options.

Created on Tue May 29 10:39:50 2018
@author: Maya Galili
"""

import numpy as np
import sys
import os

# Add the current directory to the path to import spiral_printer
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from spiral_printer import spiralPrint

def get_user_input():
    """Get user input for matrix configuration"""
    print("=" * 60)
    print("🔄 SPIRAL MATRIX PRINTER - INTERACTIVE UI")
    print("=" * 60)
    print("Configure your matrix dimensions below.")
    print("Press Enter to use default values (shown in parentheses).")
    print()
    
    # Get matrix dimensions
    print("📐 MATRIX CONFIGURATION")
    print("-" * 30)
    
    # Rows
    while True:
        try:
            rows = input("Number of rows (2-20) [default: 4]: ").strip()
            if not rows:
                rows = 4
            else:
                rows = int(rows)
            if 2 <= rows <= 20:
                break
            else:
                print("Please enter a number between 2 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Columns
    while True:
        try:
            cols = input("Number of columns (2-20) [default: 6]: ").strip()
            if not cols:
                cols = 6
            else:
                cols = int(cols)
            if 2 <= cols <= 20:
                break
            else:
                print("Please enter a number between 2 and 20.")
        except ValueError:
            print("Please enter a valid number.")
    
    return rows, cols

def get_display_preferences():
    """Get user preferences for display options"""
    print()
    print("📺 DISPLAY OPTIONS")
    print("-" * 20)
    print("1. Show matrix and spiral output")
    print("2. Show only spiral output")
    print("3. Show visual step-by-step matrix progression")
    print("4. Show text step-by-step with directions")
    
    while True:
        choice = input("Choose display mode (1-4) [default: 3]: ").strip()
        if not choice:
            choice = "3"
        if choice in ['1', '2', '3', '4']:
            break
        print("Please enter 1, 2, 3, or 4.")
    
    return int(choice)

def create_matrix(rows, cols):
    """Create a matrix with sequential numbers"""
    matrix = np.zeros((rows, cols), dtype=int)
    counter = 1
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = counter
            counter += 1
    return matrix

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

def display_matrix_simple(matrix):
    """Display the matrix in a simple formatted way"""
    print("\n📊 ORIGINAL MATRIX:")
    print("-" * 30)
    rows, cols = matrix.shape
    
    # Calculate column widths for proper alignment
    max_width = len(str(matrix.max()))
    
    for i in range(rows):
        print("│", end="")
        for j in range(cols):
            print(f" {matrix[i][j]:>{max_width}}", end="")
        print(" │")
    
    print(f"Matrix size: {rows}×{cols}")
    print()

def spiral_print_visual_step_by_step(matrix):
    """Print matrix in spiral with visual step-by-step matrix display"""
    rows, cols = matrix.shape
    mat_sz = rows * cols
    i = 0
    j = 0
    n = 0
    m = 0
    step = 1
    N, M = rows, cols
    visited = set()
    
    print("\n🔄 SPIRAL TRAVERSAL (Visual Step-by-step):")
    print("=" * 50)
    print("Legend: [X] = Visited,  X  = Current,  X  = Not visited")
    print()
    
    # Show initial empty matrix
    print("Initial matrix:")
    display_matrix(matrix, visited)
    
    while mat_sz > 0:
        # Go right
        if mat_sz > 0:
            print(f"Step {step}: → Moving RIGHT")
            for j in range(m, M):
                if mat_sz > 0:
                    visited.add((i, j))
                    print(f"  Visiting cell ({i},{j}) = {matrix[i][j]}")
                    display_matrix(matrix, visited, (i, j), "→ Right")
                    mat_sz -= 1
            n += 1
            step += 1
        
        # Go down
        if mat_sz > 0:
            print(f"Step {step}: ↓ Moving DOWN")
            for i in range(n, N):
                if mat_sz > 0:
                    visited.add((i, j))
                    print(f"  Visiting cell ({i},{j}) = {matrix[i][j]}")
                    display_matrix(matrix, visited, (i, j), "↓ Down")
                    mat_sz -= 1
            M -= 1
            step += 1
        
        # Go left
        if mat_sz > 0:
            print(f"Step {step}: ← Moving LEFT")
            for j in range(M - 1, m - 1, -1):
                if mat_sz > 0:
                    visited.add((i, j))
                    print(f"  Visiting cell ({i},{j}) = {matrix[i][j]}")
                    display_matrix(matrix, visited, (i, j), "← Left")
                    mat_sz -= 1
            N -= 1
            step += 1
        
        # Go up
        if mat_sz > 0:
            print(f"Step {step}: ↑ Moving UP")
            for i in range(N - 1, n - 1, -1):
                if mat_sz > 0:
                    visited.add((i, j))
                    print(f"  Visiting cell ({i},{j}) = {matrix[i][j]}")
                    display_matrix(matrix, visited, (i, j), "↑ Up")
                    mat_sz -= 1
            m += 1
            step += 1
    
    print("✅ Spiral traversal complete!")
    result = spiralPrint(matrix)
    print(f"Final result: {' '.join(map(str, result))}")
    print()

def spiral_print_step_by_step(matrix):
    """Print matrix in spiral with step-by-step visualization (text only)"""
    rows, cols = matrix.shape
    mat_sz = rows * cols
    i = 0
    j = 0
    n = 0
    m = 0
    step = 1
    N, M = rows, cols
    
    print("\n🔄 SPIRAL TRAVERSAL (Text Step-by-step):")
    print("-" * 40)
    
    while mat_sz > 0:
        # Go right
        if mat_sz > 0:
            print(f"\nStep {step}: → Right: ", end="")
            for j in range(m, M):
                print(f"{matrix[i][j]} ", end="")
                mat_sz -= 1
            n += 1
            step += 1
        
        # Go down
        if mat_sz > 0:
            print(f"\nStep {step}: ↓ Down:  ", end="")
            for i in range(n, N):
                print(f"{matrix[i][j]} ", end="")
                mat_sz -= 1
            M -= 1
            step += 1
        
        # Go left
        if mat_sz > 0:
            print(f"\nStep {step}: ← Left:  ", end="")
            for j in range(M - 1, m - 1, -1):
                print(f"{matrix[i][j]} ", end="")
                mat_sz -= 1
            N -= 1
            step += 1
        
        # Go up
        if mat_sz > 0:
            print(f"\nStep {step}: ↑ Up:    ", end="")
            for i in range(N - 1, n - 1, -1):
                print(f"{matrix[i][j]} ", end="")
                mat_sz -= 1
            m += 1
            step += 1
    
    print("\n")

def run_simulation(rows, cols, display_mode):
    """Run the spiral matrix simulation with given parameters"""
    
    # Create the matrix
    print("\n" + "=" * 60)
    print("🏗️  CREATING MATRIX")
    print("=" * 60)
    
    matrix = create_matrix(rows, cols)
    
    # Display matrix if requested
    if display_mode in [1, 3]:
        display_matrix_simple(matrix)
    
    # Run spiral print based on display mode
    if display_mode == 1:  # Show matrix and spiral output
        print("🔄 SPIRAL OUTPUT:")
        print("-" * 20)
        result = spiralPrint(matrix)
        print(" ".join(map(str, result)))
        print("\n")
        
    elif display_mode == 2:  # Show only spiral output
        print("🔄 SPIRAL OUTPUT:")
        print("-" * 20)
        result = spiralPrint(matrix)
        print(" ".join(map(str, result)))
        print("\n")
        
    elif display_mode == 3:  # Show visual step-by-step
        spiral_print_visual_step_by_step(matrix)
        
    elif display_mode == 4:  # Show text step-by-step
        spiral_print_step_by_step(matrix)
        
        print("🔄 FINAL SPIRAL OUTPUT:")
        print("-" * 30)
        result = spiralPrint(matrix)
        print(" ".join(map(str, result)))
        print("\n")
    
    # Display statistics
    print("=" * 60)
    print("📊 SIMULATION SUMMARY")
    print("=" * 60)
    print(f"Matrix dimensions: {rows}×{cols}")
    print(f"Total elements: {rows * cols}")
    print(f"Spiral pattern: Right → Down → Left → Up")
    print("=" * 60)

def main():
    """Main function with interactive UI"""
    try:
        while True:
            # Get user input
            rows, cols = get_user_input()
            
            # Get display preferences
            display_mode = get_display_preferences()
            
            # Run the simulation
            run_simulation(rows, cols, display_mode)
            
            # Ask if user wants to try again
            print()
            while True:
                again = input("Would you like to try another matrix? (y/n): ").lower().strip()
                if again in ['y', 'n', 'yes', 'no']:
                    break
                print("Please enter 'y' or 'n'.")
            
            if again in ['n', 'no']:
                print("\n👋 Thanks for using the Spiral Matrix Printer! Goodbye!")
                break
            else:
                print("\n" + "🔄 " + "=" * 50)
                print("STARTING NEW SIMULATION")
                print("=" * 50)
                
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try again.")

if __name__ == "__main__":
    main()
