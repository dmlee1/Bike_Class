# Name: David Lee
# Purpose: The purpose of this program is to create a bike class and allow a user to create and modify
# different bike objects. This class can handle unexpected input and inform user of this accordingly.

from bike import Bike

new_bike = Bike()
#Set total number of gears to 12

new_bike.set_Num_Gears(12)

#Set current gear to 10
new_bike.set_Curr_Gear(10)
#Increase gear up by 2
new_bike.increase_Gear()
new_bike.increase_Gear()

#Try to increase gear again
new_bike.increase_Gear()

#Set current gear to 2
new_bike.set_Curr_Gear(2)
new_bike.decrease_Gear()
new_bike.decrease_Gear()

new_bike.set_Brake_Type("electric")

new_bike.reset_Gear()
