# Name: David Lee
# Purpose: The purpose of this file to create a bike class. It can handle wrong input and will inform
# the user of any erroneous input.

#Attributes:
# Number of gears: set_Num_Gears(), get_Num_Gears()
# Current gear: set_Curr_Gear(), get_Curr_Gear()
# Number of wheels: set_Num_Wheels(), get_Num_Wheels()
# Brake type: set_Brake_Type(), get_Brake_Type()


#Methods (other than setters and getters above)
#increase_Gear()
#decrease_Gear()
#reset_Gear()


class Bike:


    __num_gears: int = 1
    __curr_gear: int = 1
    __num_wheels: int = 2
    __brake_type: str = ""

    def __init__(self,
                 num_g = 1,
                 cur_g = 1,
                 num_w = 2,
                 br_type = "hand brakes"):

        self.set_Num_Gears(num_g)
        self.set_Curr_Gear(cur_g)
        self.set_Num_Wheels(num_w)
        self.set_Brake_Type(br_type)

    ####### Setters ########

    #Sets the number of gears
    def set_Num_Gears(self, n_gears: int) -> None:
      try:
        if isinstance(n_gears,int) == False:
          raise ValueError()

        #Bike can only have 1-15 gears
        if 1 <= n_gears <= 15:
          self.__num_gears = n_gears

          if self.__num_gears == 1:
            print(f"Bike now has just {self.__num_gears} gear.\n")
          else:
            print(f"Bike now has {self.__num_gears} total gears.\n")

        else:
          print(f"The bike can only have 1-15 gears. Total number of gears is still {self.__num_gears}.\n")

      except ValueError:
          print(f"Invalid input. You entered in a {type(n_gears).__name__} value. The total number of gears must be an integer.\n")

    #Sets the current gear
    def set_Curr_Gear(self, c_gear: int) -> None:

      try:
        if isinstance(c_gear,int) == False:
          raise ValueError()

        #Current gear cannot exceed the total number of gears
        if c_gear > self.__num_gears:
          print(f"The current gear cannot exceed the number of gears on bike. Current gears is still gear {self.__curr_gear}.\n")
        elif c_gear <= 0:
          print("Current gear cannot be less than or equal to 0.\n")
        elif c_gear <= self.__num_gears:
            self.__curr_gear = c_gear
            print(f"Current gear is now gear {self.__curr_gear}.\n")

      except ValueError:
        print(f"Invalid input. You entered in a {type(c_gear).__name__} value. The current gear must be an integer.\n")

    #Sets the number of wheels
    def set_Num_Wheels(self, n_wheels: int) -> None:

      try:
        if isinstance(n_wheels,int) == False:
          raise ValueError()

        #Bike can only have 1-4 wheels
        if 1 <= n_wheels <= 4:
            self.__num_wheels = n_wheels
        else:
          print("The bike can only have between 1 to 4 wheels.\n")

      except ValueError:
        print(f"Invalid input. You entered in a {type(n_wheels).__name__} value.The total number of wheels must be an integer.\n")

    #Sets the brake type
    def set_Brake_Type(self, type_b: str) -> None:

      try:
        if isinstance(type_b,str) == False:
          raise ValueError()

        if type_b == "hand brakes" or type_b == "foot brakes":
            self.__brake_type = type_b
        else:
          print("The bike can only have either a hand braking system or a foot braking system.\n")

      except ValueError:
        print(f"Invalid input. You entered in a/an {type(type_b).__name__} value. The brake type must be a string.\n")


    ####### Getters ########

    #Returns the number of gears
    def get_Num_Gears(self) -> int:
        return self.__num_gears

    #Returns the current gear
    def get_Curr_Gear(self) -> int:
        return self.__curr_gear

    #Returns the number of wheels
    def get_Num_Wheels(self) -> int:
        return self.__num_wheels

    #Returns the brake type
    def get_Brake_Type(self) -> str:
        return self.__brake_type

     ####### Other methods ########

    #Increases the current gear by one
    def increase_Gear(self) -> None:
        if self.get_Curr_Gear() == self.get_Num_Gears():
            print(f"Current gear is gear {self.get_Curr_Gear()}, and the total number of gears is {self.get_Num_Gears()}. Cannot raise gear anymore.\n")
        else:
          self.__curr_gear += 1
          print(f"Gear increased by one. Current gear is now gear {self.get_Curr_Gear()}.\n")

    #Decreases the current gear by one
    def decrease_Gear(self) -> None:
        if self.get_Curr_Gear() == 1:
            print("Current gear is 1. Cannot lower it anymore.\n")
        else:
          self.__curr_gear -=1
          print(f"Gear decreased by one. Current gear is now gear {self.get_Curr_Gear()}.\n")

    #Resets current gear to one
    def reset_Gear(self) -> None:
      self.__curr_gear = 1
      print("Current gear reset to gear 1.")
