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
import time

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
    print("1. Show only spiral output")
    print("2. Show visual step-by-step matrix progression (with 1s delay)")
    
    while True:
        choice = input("Choose display mode (1-2) [default: 2]: ").strip()
        if not choice:
            choice = "2"
        if choice in ['1', '2']:
            break
        print("Please enter 1 or 2.")
    
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

def run_simulation(rows, cols, display_mode):
    """Run the spiral matrix simulation with given parameters"""
    
    # Create the matrix
    print("\n" + "=" * 60)
    print("🏗️  CREATING MATRIX")
    print("=" * 60)
    
    matrix = create_matrix(rows, cols)
    
    # Display matrix if requested
    if display_mode == 2:
        display_matrix_simple(matrix)
    
    # Run spiral print based on display mode
    if display_mode == 1:  # Show only spiral output
        print("🔄 SPIRAL OUTPUT:")
        print("-" * 20)
        result = spiralPrint(matrix)
        print(" ".join(map(str, result)))
        print("\n")
        
    elif display_mode == 2:  # Show visual step-by-step
        result = spiralPrint(matrix, visual=True)
    
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
