# -*- coding: utf-8 -*-
"""
Interactive UI for Parking Lot Simulation

This module provides a user-friendly interface for the parking lot simulation,
allowing users to configure the number of spots and vehicles with default values.

Created on Wed Jul  4 09:14:28 2018
@author: Maya Galili
"""

import sys
import os
import time
from random import shuffle

# Add the current directory to the path to import ParkingLot
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ParkingLot import ParkingLot, Motorcycle, Car, Bus

def get_user_input():
    """Get user input for parking lot configuration"""
    print("=" * 60)
    print("🅿️  PARKING LOT SIMULATION - INTERACTIVE UI")
    print("=" * 60)
    print("Configure your parking lot and vehicles below.")
    print("Press Enter to use default values (shown in parentheses).")
    print()
    
    # Get parking lot configuration
    print("📋 PARKING LOT CONFIGURATION")
    print("-" * 30)
    
    # Small spots
    while True:
        try:
            small_spots = input("Number of small spots (size 1) [default: 5]: ").strip()
            if not small_spots:
                small_spots = 5
            else:
                small_spots = int(small_spots)
            if small_spots < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Medium spots
    while True:
        try:
            med_spots = input("Number of medium spots (size 2) [default: 10]: ").strip()
            if not med_spots:
                med_spots = 10
            else:
                med_spots = int(med_spots)
            if med_spots < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Big spots
    while True:
        try:
            big_spots = input("Number of big spots (size 3) [default: 3]: ").strip()
            if not big_spots:
                big_spots = 3
            else:
                big_spots = int(big_spots)
            if big_spots < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print()
    print("🚗 VEHICLE CONFIGURATION")
    print("-" * 30)
    
    # Motorcycles
    while True:
        try:
            motorcycles = input("Number of motorcycles [default: 3]: ").strip()
            if not motorcycles:
                motorcycles = 3
            else:
                motorcycles = int(motorcycles)
            if motorcycles < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Cars
    while True:
        try:
            cars = input("Number of cars [default: 8]: ").strip()
            if not cars:
                cars = 8
            else:
                cars = int(cars)
            if cars < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Buses
    while True:
        try:
            buses = input("Number of buses [default: 2]: ").strip()
            if not buses:
                buses = 2
            else:
                buses = int(buses)
            if buses < 0:
                print("Please enter a non-negative number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return small_spots, med_spots, big_spots, motorcycles, cars, buses

def get_display_preferences():
    """Get user preferences for display options"""
    print()
    print("📺 DISPLAY OPTIONS")
    print("-" * 20)
    print("1. Show parking lot after each vehicle (step-by-step with 1s delay)")
    print("2. Show only final result")
    print("3. Show summary only (no visual display)")
    
    while True:
        choice = input("Choose display mode (1-3) [default: 1]: ").strip()
        if not choice:
            choice = "1"
        if choice in ['1', '2', '3']:
            break
        print("Please enter 1, 2, or 3.")
    
    # Set delay for step-by-step mode
    delay = 1.0 if choice == "1" else 0
    
    return int(choice), delay

def run_simulation(small_spots, med_spots, big_spots, motorcycles, cars, buses, display_mode, delay=0):
    """Run the parking lot simulation with given parameters"""
    
    # Create the parking lot
    print("\n" + "=" * 60)
    print("🏗️  CREATING PARKING LOT")
    print("=" * 60)
    
    PL = ParkingLot(small_spots, med_spots, big_spots)
    
    # Display parking lot setup
    print(f"Parking lot created with {PL.getTotalSpotsSz()} spots:")
    print(f"  • {small_spots} Small spots (size 1) - for motorcycles")
    print(f"  • {med_spots} Medium spots (size 2) - for cars")  
    print(f"  • {big_spots} Big spots (size 3) - for buses")
    print()
    
    # Create vehicles
    print("🚗 CREATING VEHICLES")
    print("-" * 20)
    
    vec_set = []
    
    # Add motorcycles
    for i in range(motorcycles):
        vec_set.append(Motorcycle())
    
    # Add cars
    for i in range(cars):
        vec_set.append(Car())
    
    # Add buses
    for i in range(buses):
        vec_set.append(Bus())
    
    # Shuffle the vehicles for random parking order
    shuffle(vec_set)
    
    print(f"Created {len(vec_set)} vehicles:")
    print(f"  • {motorcycles} Motorcycles")
    print(f"  • {cars} Cars")
    print(f"  • {buses} Buses")
    print()
    
    # Show initial empty parking lot
    if display_mode in [1, 2]:
        print("🅿️  INITIAL EMPTY PARKING LOT")
        print("-" * 30)
        PL.display_parking_lot()
    
    # Track parking results
    successful_parking = 0
    failed_parking = 0
    
    print("🚗 STARTING PARKING PROCESS")
    print("-" * 30)
    
    # Try to park all vehicles
    for i, vehicle in enumerate(vec_set):
        if PL.park_new_vec(vehicle):
            successful_parking += 1
        else:
            failed_parking += 1
        
        # Show updated parking lot status based on display mode
        if display_mode == 1:  # Step-by-step
            print(f"\nAfter vehicle {i+1}/{len(vec_set)}:")
            PL.display_parking_lot()
            if delay > 0 and i < len(vec_set) - 1:  # Don't delay after the last vehicle
                time.sleep(delay)
        elif display_mode == 2 and i == len(vec_set) - 1:  # Final result only
            print(f"\n🏁 FINAL PARKING LOT STATE")
            print("-" * 30)
            PL.display_parking_lot()
    
    # Display final summary
    print("\n" + "=" * 60)
    print("📊 PARKING SUMMARY")
    print("=" * 60)
    print(f"Total Spots Available: {PL.getTotalSpotsSz()}")
    print(f"  • Small spots: {small_spots}")
    print(f"  • Medium spots: {med_spots}")
    print(f"  • Big spots: {big_spots}")
    print()
    print(f"Vehicles Attempted: {len(vec_set)}")
    print(f"  • Motorcycles: {motorcycles}")
    print(f"  • Cars: {cars}")
    print(f"  • Buses: {buses}")
    print()
    print(f"Successfully Parked: {successful_parking}")
    print(f"Failed to Park: {failed_parking}")
    print(f"Remaining Open Spots: {PL.getOpenSpotsSz()}")
    
    if len(vec_set) > 0:
        efficiency = (successful_parking / len(vec_set)) * 100
        print(f"Parking Efficiency: {efficiency:.1f}%")
    
    # Show spot utilization
    print(f"\nSpot Utilization:")
    print(f"  • Small spots: {small_spots - sum(1 for spot in PL.getAllSpots() if spot.getSpotSize() == 1 and spot.is_open())}/{small_spots}")
    print(f"  • Medium spots: {med_spots - sum(1 for spot in PL.getAllSpots() if spot.getSpotSize() == 2 and spot.is_open())}/{med_spots}")
    print(f"  • Big spots: {big_spots - sum(1 for spot in PL.getAllSpots() if spot.getSpotSize() == 3 and spot.is_open())}/{big_spots}")
    
    print("=" * 60)
    
    return successful_parking, failed_parking, PL

def main():
    """Main function with interactive UI"""
    try:
        while True:
            # Get user input
            small_spots, med_spots, big_spots, motorcycles, cars, buses = get_user_input()
            
            # Validate that we have at least some spots or vehicles
            total_spots = small_spots + med_spots + big_spots
            total_vehicles = motorcycles + cars + buses
            
            if total_spots == 0:
                print("\n❌ Error: You need at least one parking spot!")
                continue
            
            if total_vehicles == 0:
                print("\n❌ Error: You need at least one vehicle!")
                continue
            
            # Get display preferences
            display_mode, delay = get_display_preferences()
            
            # Run the simulation
            successful, failed, parking_lot = run_simulation(
                small_spots, med_spots, big_spots, 
                motorcycles, cars, buses, display_mode, delay
            )
            
            # Ask if user wants to try again
            print()
            while True:
                again = input("Would you like to run another simulation? (y/n): ").lower().strip()
                if again in ['y', 'n', 'yes', 'no']:
                    break
                print("Please enter 'y' or 'n'.")
            
            if again in ['n', 'no']:
                print("\n👋 Thanks for using the Parking Lot Simulator! Goodbye!")
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
