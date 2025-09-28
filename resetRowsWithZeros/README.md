# Reset Rows and Columns with Zeros

## What is this project?
A simple script that takes a binary matrix (containing only 0s and 1s) and produces a new matrix where any row or column containing at least one zero gets completely zeroed out. This is useful for getting ground truth results when trying to solve this problem manually.

## Files
- `reset_rows_and_cols_with_zeros.py` - The core algorithm implementation
- `reset_rows_ui.py` - Simple command-line interface for easy testing
- `test_reset_rows_and_cols_with_zeros.py` - Unit tests

## How to use

### Option 1: Interactive CLI (Recommended)
Run the simple command-line interface:
```bash
python reset_rows_ui.py
```

This will show you a menu with options to:
1. Generate a random binary matrix
2. Load the example matrix
3. Input your own matrix manually
4. Exit

### Option 2: Direct function import
```python
from reset_rows_and_cols_with_zeros import reset_rows_with_zeros
import numpy as np

# Example matrix
matrix = np.array([
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1]
])

# Process the matrix
result = reset_rows_with_zeros(matrix.copy())
print(result)
```

## Algorithm
The algorithm works by:
1. Calculating the sum of each row and column
2. If a row's sum is less than the matrix size, it contains at least one zero
3. If a column's sum is less than the matrix size, it contains at least one zero
4. Zero out any row or column that contains at least one zero

## Example
Input matrix:
```
0 1 1 1 1
0 1 1 1 0
1 1 0 0 1
1 1 1 1 1
1 1 0 1 1
```

Output matrix:
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
```
