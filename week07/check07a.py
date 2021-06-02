"""
Checkpoint 07 A
Alejandro Flores Medina
"""

# TODO: Create a base car class here
class Car:
    def __init__(self):
        self.name = "Unknown model"

    def get_door_specs(self):
        door_specs = "Unknown doors"
        
        return door_specs

# TODO: Create a civic class here
class Civic(Car):
    def __init__(self):
        super().__init__()
        self.name = "Civic"

    def get_door_specs(self):
        door_specs = "4 doors"
        return door_specs

# TODO: Create an odyssey class here
class Odyssey(Car):
    def __init__(self):
        super().__init__()
        self.name = "Odyssey"

    def get_door_specs(self):
        door_specs = "2 front doors, 2 sliding doors, 1 tail gate"
        return door_specs

# TODO: Create a Ferrari class here
class Ferrari(Car):
    def __init__(self):
        super().__init__()
        self.name = "Ferrari"

    def get_door_specs(self):
        door_specs = "2 butterfly doors"
        return door_specs

# TODO: Create your attach_doors function here
# It should accept any type of car and use its
# name and get_door_specs function to print out
# the necessary data.
# It should not be a member function of any class,
# but rather just a "regular" function.

def attach_doors(Car):
    car = Car.name
    doors = Car.get_door_specs()
    print("Attaching doors to " + car + " - " + doors)
    


def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)

if __name__ == "__main__":
    main()