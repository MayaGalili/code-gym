# -*- coding: utf-8 -*-
"""
Design a parking lot using object-oriented principles. 


Created on Wed Jul  4 09:14:28 2018
@author: Maya Galili
"""

#%%  vehicle

from random import shuffle

class Vehicle:
       
    def __init__(self,wheel_num,car_type):
        self._car_type = car_type
        self._wheel_num = wheel_num

    # getters       
    def getType(self):
        return self._car_type
    
    def getWheelNum(self):
        return self._wheel_num

class Motorcycle(Vehicle): 
        def __init__(self):
            Vehicle.__init__(self,2,'MOTORCYCLE')

class Car(Vehicle):  
        def __init__(self):
            Vehicle.__init__(self,4,'CAR')
            
class Bus(Vehicle):  
        def __init__(self):
            Vehicle.__init__(self,6,'BUS')

#%% parking lot
class ParkingLot:
    
    def __init__(self,small_spot_sz, med_spot_sz,big_spot_sz):          
        self._vehicle_set = []
        self._total_spots = self.generateOpenSpots(small_spot_sz, med_spot_sz,big_spot_sz)

    # creat a parking lot with X1 small spots, x2 medium spots and x3 big spots    
    def generateOpenSpots(self,small_spot_sz, med_spot_sz,big_spot_sz):
        self._total_spots = []   

        for i in range(small_spot_sz):
            self._total_spots.append(SmallSpot())
        for i in range(med_spot_sz):
            self._total_spots.append(MedSpot())
        for i in range(big_spot_sz):
            self._total_spots.append(BigSpot())
            
        shuffle(self._total_spots)         
        return self._total_spots
      
    # find next open spot and park the given car if posible
    # if there is no good spot, enter the next car
    def park_new_vec(self, new_vehicle):
        print(f"🚗 {new_vehicle.getType()} trying to park...")
        
        total_spots_sz = self.getTotalSpotsSz()
        parked = False
        
        for i in range(total_spots_sz):
            if self._total_spots[i].is_open():
                #set spot to hold the car
                if self._total_spots[i].park_vehicle(new_vehicle):
                    print(f"✅ {new_vehicle.getType()} parked in spot {i} (size {self._total_spots[i].getSpotSize()})")
                    # add car to the parkingLot cars list
                    self._vehicle_set.append(new_vehicle)
                    parked = True
                    break
                else:
                    print(f"   Spot {i} (size {self._total_spots[i].getSpotSize()}) too small for {new_vehicle.getType()}")
        
        if not parked:
            print(f"❌ {new_vehicle.getType()} could not find a suitable spot!")
        
        return parked
                
    def is_park_open(self):
        return (self.getOpenSpotsSz() > 0)
    
    # getters
    def getTotalSpotsSz(self):
        return len(self._total_spots)
    
    def getVehicleSet(self):
        return self._vehicle_set
    
    def getOpenSpotsSz(self):
        return self.getTotalSpotsSz() - len(self.getVehicleSet())
    
    def getAllSpots(self):
        return self._total_spots
    
    def display_parking_lot(self):
        """Display the current parking lot status visually"""
        spots = self._total_spots
        total_spots = len(spots)
        
        print("🅿️  Current Parking Lot Status:")
        
        # If too many spots, display in multiple rows
        if total_spots > 20:
            spots_per_row = 20
            rows = (total_spots + spots_per_row - 1) // spots_per_row
            
            for row in range(rows):
                start_idx = row * spots_per_row
                end_idx = min(start_idx + spots_per_row, total_spots)
                row_spots = spots[start_idx:end_idx]
                
                print("┌" + "─" * (len(row_spots) * 4 - 1) + "┐")
                print("│", end="")
                
                for spot in row_spots:
                    if spot.is_open():
                        print(" [ ]", end="")
                    else:
                        vehicle = spot.getParkedVec()
                        if vehicle.getType() == "MOTORCYCLE":
                            print(" [M]", end="")
                        elif vehicle.getType() == "CAR":
                            print(" [C]", end="")
                        elif vehicle.getType() == "BUS":
                            print(" [B]", end="")
                        else:
                            print(" [?]", end="")
                
                print(" │")
                print("└" + "─" * (len(row_spots) * 4 - 1) + "┘")
        else:
            # Single row display for smaller parking lots
            print("┌" + "─" * (total_spots * 4 - 1) + "┐")
            print("│", end="")
            
            for i, spot in enumerate(spots):
                if spot.is_open():
                    print(" [ ]", end="")
                else:
                    vehicle = spot.getParkedVec()
                    if vehicle.getType() == "MOTORCYCLE":
                        print(" [M]", end="")
                    elif vehicle.getType() == "CAR":
                        print(" [C]", end="")
                    elif vehicle.getType() == "BUS":
                        print(" [B]", end="")
                    else:
                        print(" [?]", end="")
            
            print(" │")
            print("└" + "─" * (total_spots * 4 - 1) + "┘")
        
        print("Legend: M=Motorcycle, C=Car, B=Bus, [ ]=Empty")
        print()

#%%  spot
            
class Spot:
    
    def __init__(self,spot_sz):
        self._spot_size = spot_sz
        self._spot_car = None
        
    def is_open(self):
        return self._spot_car == None
    
    def park_vehicle(self,new_vec):
        can_park = new_vec.getWheelNum()/2 <= self.getSpotSize()
        if can_park:
            self._spot_car = new_vec
        return can_park              

    # getters        
    def getParkedVec(self):
        return self._spot_car
    
    def getSpotSize(self):
        return self._spot_size    
    
class SmallSpot(Spot):
    def __init__(self):
        Spot.__init__(self,1)
    
class MedSpot(Spot):
    def __init__(self):
        Spot.__init__(self,2)
        
class BigSpot(Spot):
    def __init__(self):
        Spot.__init__(self,3)
#%%
                              
''' running example:
1) creat the parking lot with X1 small spots, x2 medium spots and x3 big spots
2) creat a set of vihacles with y1 bickles y2 cars and y3 busses
3) for each vihacle in its turn - 
    find a suitable sopt and park it
    first randomly and at the next code iteration try to consider other vehicles
'''
if __name__ == "__main__":
    # creat the parking lot
    small_spot_sz= 2
    med_spot_sz = 10
    big_spot_sz = 2

    PL = ParkingLot(small_spot_sz, med_spot_sz,big_spot_sz)

    # creat a rand set of vihacles   
    cycle_sz = 2
    cars_sz = 5
    buses_sz = 1

    vec_set = []
    for i in range(cycle_sz):
        vec_set.append(Motorcycle())
    for i in range(cars_sz):
        vec_set.append(Car())            
    for i in range(buses_sz):
        vec_set.append(Bus())
    shuffle(vec_set)

    # Display parking lot setup
    print("=" * 50)
    print("🅿️  PARKING LOT SIMULATION")
    print("=" * 50)
    print(f"Parking lot created with {PL.getTotalSpotsSz()} spots:")
    print(f"  • {small_spot_sz} Small spots (size 1)")
    print(f"  • {med_spot_sz} Medium spots (size 2)")  
    print(f"  • {big_spot_sz} Big spots (size 3)")
    print()
    print(f"Vehicles to park: {len(vec_set)}")
    print(f"  • {cycle_sz} Motorcycles")
    print(f"  • {cars_sz} Cars")
    print(f"  • {buses_sz} Buses")
    print()
    print("Starting parking process...")
    print("-" * 30)
    
    # Track parking results
    successful_parking = 0
    failed_parking = 0
    
    # Show initial empty parking lot
    PL.display_parking_lot()
    
    # try to park all cars
    for i in range(len(vec_set)):
        if PL.park_new_vec(vec_set[i]):
            successful_parking += 1
        else:
            failed_parking += 1
        
        # Show updated parking lot status after each vehicle
        PL.display_parking_lot()
    
    # Final summary
    print("=" * 50)
    print("📊 PARKING SUMMARY")
    print("=" * 50)
    print(f"Total Spots Available: {PL.getTotalSpotsSz()}")
    print(f"Vehicles Attempted: {len(vec_set)}")
    print(f"Successfully Parked: {successful_parking}")
    print(f"Failed to Park: {failed_parking}")
    print(f"Remaining Open Spots: {PL.getOpenSpotsSz()}")
    
    if len(vec_set) > 0:
        efficiency = (successful_parking / len(vec_set)) * 100
        print(f"Parking Efficiency: {efficiency:.1f}%")
    
    print("=" * 50)