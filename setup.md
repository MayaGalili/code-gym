# Code Gym - Setup Instructions

This repository contains three educational programming modules that demonstrate different algorithms and concepts. All modules use Python and can be run using `uv` for dependency management.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd code-gym
   ```

2. **Install uv (if not already installed):**
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

3. **Set up the environment:**
   ```bash
   uv sync
   ```

4. **Activate the environment:**
   ```bash
   uv shell
   ```

## 📦 Available Modules

### 1. Paint Circle
- **Location**: `paint_circle/`
- **Description**: Interactive circle drawing with user input
- **Run**: `python paint_circle/circle_test.py`

### 2. Parking Lot Simulation
- **Location**: `parkinglot/`
- **Description**: OOP parking lot simulation with vehicles and spots
- **Run**: `python parkinglot/parking_lot_ui.py`

### 3. Spiral Matrix Printer
- **Location**: `spiral_printer/`
- **Description**: Matrix spiral traversal with visual display
- **Run**: `python spiral_printer/spiral_ui.py`

## 🛠️ Development Setup

### Using uv for Development

1. **Install dependencies:**
   ```bash
   uv sync --dev
   ```

2. **Run a specific module:**
   ```bash
   # Paint Circle
   uv run python paint_circle/circle_test.py
   
   # Parking Lot
   uv run python parkinglot/parking_lot_ui.py
   
   # Spiral Printer
   uv run python spiral_printer/spiral_ui.py
   ```

3. **Add new dependencies:**
   ```bash
   uv add package-name
   ```

4. **Update dependencies:**
   ```bash
   uv sync
   ```

## 📋 Dependencies

The project uses the following main dependencies:
- **numpy**: For matrix operations and mathematical computations
- **matplotlib**: For plotting and visualization

All dependencies are managed through `pyproject.toml` and `uv.lock` files.

## 🎯 Learning Objectives

These modules demonstrate:
- **Object-Oriented Programming** (Parking Lot)
- **Algorithm Design** (Spiral Printer)
- **Mathematical Visualization** (Paint Circle)
- **User Interface Design** (All modules)
- **Dependency Management** (uv)

## 📚 Next Steps

1. Start with any module that interests you
2. Try different input values and configurations
3. Explore the source code to understand the algorithms
4. Modify the code to experiment with different approaches

Happy coding! 🚀
