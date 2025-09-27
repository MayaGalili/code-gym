# Parking Lot Simulation

A classic object-oriented programming exercise that simulates a parking lot with different vehicle types and spot sizes. The simulation demonstrates OOP principles including inheritance, polymorphism, and encapsulation.

## 🚗 What It Does

This simulation models a parking lot with three types of spots and three types of vehicles:

### Vehicle Types
- **Motorcycles** (2 wheels) - can park in any spot
- **Cars** (4 wheels) - can park in medium or big spots
- **Buses** (6 wheels) - can only park in big spots

### Spot Types
- **Small spots** `( )` - size 1, for motorcycles only
- **Medium spots** `[ ]` - size 2, for motorcycles and cars
- **Big spots** `{ }` - size 3, for all vehicle types

### Features
- **Visual Display**: Shows parking lot status with different brackets for spot types
- **Interactive UI**: Configure number of spots and vehicles with default values
- **Step-by-step Animation**: Watch vehicles park in real-time with 1-second delays
- **Statistics**: Track parking efficiency, spot utilization, and success rates
- **Multiple Display Modes**: Choose between step-by-step, final result, or summary only

## 🏃‍♂️ How to Run

### Interactive UI (Recommended)
```bash
python parking_lot_ui.py
```

The interactive UI will guide you through:
1. **Parking Lot Configuration**: Set number of small, medium, and big spots
2. **Vehicle Configuration**: Set number of motorcycles, cars, and buses
3. **Display Options**: Choose how to view the simulation
4. **Run Simulation**: Watch vehicles park with visual feedback

### Default Values
- **Spots**: 5 small, 10 medium, 3 big
- **Vehicles**: 3 motorcycles, 8 cars, 2 buses
- **Display**: Step-by-step with 1-second delay

### Direct Execution
```bash
python ParkingLot.py
```
Runs a predefined simulation with fixed parameters.

## 📊 Example Output

```
🅿️  Current Parking Lot Status:
┌─────────────────────────────────────────────────────────────┐
│ (M) [C] {B} ( ) [ ] { } [C] (M) [ ] {C} [B] ( ) [ ] { } [C] │
└─────────────────────────────────────────────────────────────┘
Legend: ( )=Small spot, [ ]=Medium spot, { }=Big spot
        M=Motorcycle, C=Car, B=Bus
```

## 🏗️ Architecture

### Classes
- **`Vehicle`**: Base class for all vehicles
- **`Motorcycle`**, **`Car`**, **`Bus`**: Specific vehicle types
- **`Spot`**: Base class for parking spots
- **`SmallSpot`**, **`MedSpot`**, **`BigSpot`**: Specific spot types
- **`ParkingLot`**: Manages the parking lot and parking logic

### Key Methods
- `park_new_vec()`: Attempts to park a vehicle
- `display_parking_lot()`: Shows current parking lot status
- `getOpenSpotsSz()`: Returns number of available spots

## 🎯 Learning Objectives

This project demonstrates:
- **Inheritance**: Vehicle and Spot hierarchies
- **Polymorphism**: Different vehicle/spot behaviors
- **Encapsulation**: Private attributes with getters
- **Object Composition**: ParkingLot contains Spots and Vehicles
- **Algorithm Design**: Parking assignment logic
- **User Interface Design**: Interactive command-line interface

## 📁 Files

- `ParkingLot.py` - Core parking lot classes and logic
- `parking_lot_ui.py` - Interactive user interface
- `README.md` - This documentation

## 🚀 Getting Started

1. Make sure you have Python 3.6+ installed
2. Navigate to the parkinglot directory
3. Run `python parking_lot_ui.py`
4. Follow the prompts to configure your simulation
5. Watch the magic happen! 🎉
