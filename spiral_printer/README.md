# Spiral Matrix Printer

A classic algorithm that prints matrix elements in a spiral pattern, moving clockwise from the top-left corner: **right → down → left → up**.

## 🔄 What It Does

The script takes a 2D matrix (N×M) and prints its elements in a **spiral pattern**:
1. **Starts** at position (0,0) - top-left corner
2. **Moves right** across the top row
3. **Moves down** along the rightmost column  
4. **Moves left** across the bottom row
5. **Moves up** along the leftmost column
6. **Repeats** the pattern, moving inward with each iteration

## 🏃‍♂️ How to Run

### Interactive UI (Recommended)
```bash
python spiral_ui.py
```

The interactive UI allows you to:
- **Configure matrix size**: Choose rows and columns (2-20 each)
- **Select display mode**: 
  - Show only spiral output
  - Show visual step-by-step matrix progression (with 1s delay)
- **Use default values**: Press Enter for 4×6 matrix

### Direct Execution
```bash
python spiral_printer.py
```
Runs with a predefined 4×6 matrix example.

### Default Values
- **Matrix size**: 4 rows × 6 columns
- **Display**: Visual step-by-step with 1-second delay

## 📊 Example

For a 4×6 matrix:
```
[1,  2,  3,  4,  5,  6 ]
[7,  8,  9,  10, 11, 12]
[13, 14, 15, 16, 17, 18]
[19, 20, 21, 22, 23, 24]
```

**Spiral output:**
```
1 2 3 4 5 6 12 18 24 23 22 21 20 19 13 7 8 9 10 11 17 16 15 14
```

**Visual step-by-step matrix progression:**
```
Initial matrix:
┌─────────────────────┐
│   1    2    3    4  │
│   5    6    7    8  │
│   9   10   11   12  │
└─────────────────────┘

Step 1: → Moving RIGHT
  Visiting cell (0,0) = 1
┌─────────────────────┐
│  [1]   2    3    4  │
│   5    6    7    8  │
│   9   10   11   12  │
└─────────────────────┘
Direction: → Right
[1 second delay...]

  Visiting cell (0,1) = 2
┌─────────────────────┐
│  [1]  [2]   3    4  │
│   5    6    7    8  │
│   9   10   11   12  │
└─────────────────────┘
Direction: → Right
[1 second delay...]
```

## 🏗️ Algorithm

- Uses boundary variables (`n`, `m`, `N`, `M`) to track the current spiral layer
- Decrements `mat_sz` (remaining elements) after each print
- Adjusts boundaries after each direction to move inward
- Continues until all elements are printed

## 📁 Files

- `spiral_printer.py` - Core spiral algorithm
- `spiral_ui.py` - Interactive user interface
- `README.md` - This documentation

## 🎯 Learning Objectives

This project demonstrates:
- **Matrix traversal techniques**
- **Boundary management**
- **Directional movement patterns**
- **Algorithm design**
- **User interface design**

## 🚀 Getting Started

**Prerequisites:** See [setup.md](../setup.md) for complete environment setup instructions.

1. Set up the environment using uv (see [setup.md](../setup.md))
2. Navigate to the spiral_printer directory
3. Run `uv run python spiral_ui.py`
4. Follow the prompts to configure your matrix
5. Watch the spiral magic happen! 🌀

### Quick Run
```bash
# From the project root
uv run python spiral_printer/spiral_ui.py
```

---
**Author:** Maya Galili <https://github.com/MayaGalili>
