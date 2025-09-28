#!/usr/bin/env python3
"""
Simple CLI for the Reset Rows and Columns with Zeros script
A command-line interface that allows users to input a binary matrix and see the results
"""

import numpy as np
from reset_rows_and_cols_with_zeros import reset_rows_with_zeros


def print_matrix(matrix, title="Matrix"):
    """Print a matrix in a nice format"""
    print(f"\n{title}:")
    print("-" * (len(title) + 1))
    for row in matrix:
        print(" ".join(f"{val:2d}" for val in row))
    print()


def get_matrix_size():
    """Get matrix size from user"""
    while True:
        try:
            size = int(input("Enter matrix size (2-10): "))
            if 2 <= size <= 10:
                return size
            else:
                print("Size must be between 2 and 10")
        except ValueError:
            print("Please enter a valid integer")


def generate_random_matrix(size):
    """Generate a random binary matrix"""
    return np.random.randint(2, size=(size, size))


def load_example_matrix():
    """Load the example matrix from the original script"""
    return np.array([
        [0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1]
    ])


def input_matrix_manually(size):
    """Let user input matrix manually"""
    print(f"\nEnter {size}x{size} matrix (0s and 1s only):")
    print("Enter each row as space-separated numbers")
    print("Example: 1 0 1 0 1")
    
    matrix = []
    for i in range(size):
        while True:
            try:
                row_input = input(f"Row {i+1}: ").strip()
                if not row_input:
                    print("Please enter a row")
                    continue
                
                row = [int(x) for x in row_input.split()]
                if len(row) != size:
                    print(f"Row must have exactly {size} numbers")
                    continue
                
                if not all(x in [0, 1] for x in row):
                    print("All numbers must be 0 or 1")
                    continue
                
                matrix.append(row)
                break
                
            except ValueError:
                print("Please enter valid integers separated by spaces")
    
    return np.array(matrix)


def show_menu():
    """Show the main menu"""
    print("\n" + "="*50)
    print("Reset Rows and Columns with Zeros")
    print("="*50)
    print("This tool takes a binary matrix (containing only 0s and 1s)")
    print("and creates a new matrix where any row or column containing")
    print("at least one zero gets completely zeroed out.")
    print("\nChoose an option:")
    print("1. Generate random matrix")
    print("2. Load example matrix")
    print("3. Input matrix manually")
    print("4. Exit")


def main():
    """Main function"""
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                # Generate random matrix
                size = get_matrix_size()
                matrix = generate_random_matrix(size)
                print_matrix(matrix, "Generated Random Matrix")
                
            elif choice == "2":
                # Load example matrix
                matrix = load_example_matrix()
                print_matrix(matrix, "Example Matrix")
                
            elif choice == "3":
                # Input matrix manually
                size = get_matrix_size()
                matrix = input_matrix_manually(size)
                print_matrix(matrix, "Input Matrix")
                
            elif choice == "4":
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                continue
            
            # Process the matrix
            print("Processing matrix...")
            result = reset_rows_with_zeros(matrix.copy())
            print_matrix(result, "Result Matrix")
            
            # Ask if user wants to continue
            continue_choice = input("\nPress Enter to continue or 'q' to quit: ").strip().lower()
            if continue_choice == 'q':
                print("Goodbye!")
                break
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()