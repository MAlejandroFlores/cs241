"""
File: assign03.py
Alejandro Flores Medina
Purpose: Robot model enviroment
"""
import sys

class Robot:

    ''' CONSTRUCTOR '''
    def __init__(self):
        self.x_coodinate = 10
        self.y_coodinate = 10
        self.fuel = 100

    ''' SETTERS '''
    def set_x(self, x):
        self.x_coodinate += x

    def set_y(self, y):
        self.y_coodinate += y

    def rest_fuel(self, fuel):
        if self.get_fuel() >= fuel:
            self.fuel -= fuel
            return True
        else:
            print('Insufficient fuel to perform action')
            return False

    ''' GETTERS '''
    def get_x(self):
        return self.x_coodinate

    def get_y(self):
        return self.y_coodinate

    def get_fuel(self):
        return self.fuel

    def move_left(self):
        if self.rest_fuel(5):
            self.set_x(-1)
        

    def move_right(self):
        if self.rest_fuel(5):
            self.set_x(1)
        

    def move_up(self):
        if self.rest_fuel(5):
            self.set_y(-1)
        

    def move_down(self):
        if self.rest_fuel(5):
            self.set_y(1)
        

    def status(self):
        print('(' + str(self.get_x()) + ', ' + str(self.get_y()) + ') - Fuel: ' + str(self.get_fuel()))


    def fire(self):
        if self.rest_fuel(15):
            print('Pew! Pew!')

def status(robot):
    robot.status()

       
def prompt_command():
    command = input('Enter command: ')
    return command

def exec_command(command, robot):
    command = command.lower()
    if command == 'quit':
        print('Goodbye.')
        sys.exit()
    elif command == 'left':
        robot.move_left()
    elif command == 'right':
        robot.move_right()
    elif command == 'down':
        robot.move_down()
    elif command == 'up':
        robot.move_up()
    elif command == 'status':
        robot.status()
    elif command == 'fire':
        robot.fire()


def main():
    robot = Robot()
    while True:
        command = prompt_command()
        exec_command(command, robot)

    
# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
