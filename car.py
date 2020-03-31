RIGHT = 1
LEFT = -1
REVERSE_DIRECTION = -6
FORWARD = 1
REVERSE = 0

import pdb

#gears and allowable speeds are as follows:
    #zero (reverse) (speed -1 to -10). Max reverse speed of car is -10
    #one (speed 0 to 10)
    #two (speed 5 to 25)
    #three (speed 20 to 40)
    #four (speed 40 to 60)
    #five (speed 45 to 80). Max speed of car is 80
    #gears change automatically, one gear at a time

#direction values are similar to numbers on clock face
#0 = 12 = straight on. All other directions = 1-11

class Car:
    def __init__(self):
        self.speed = 0
        self.gear = 1
        self.direction = 0
        self.broken = False #indicates whether car is broken
        self.simulation = []
        self.simulation_loaded = False

    def accelerate(self):
        print("Accelerating...")
        if self.broken == True:
            return
        if self.gear > 0:
            self.speed += 5
        elif self.gear == 0:
            self.speed -= 5

        if self.speed > 80:
            self.speed = 80

        if self.speed < -10:
            self.speed = -10

        self.change_gear()
        self.display_stats()

    def brake(self):
        if self.broken == True:
            return
        if self.gear != 0:
            self.speed -= 5

        self.change_gear()
        self.display_stats()

    def turn_steering_wheel(self, direction_change):
        if self.broken == True:
            return
        direction_value = 0
        if direction_change == "LEFT":
            direction_value = LEFT
        else:
            direction_value = RIGHT

        if self.gear == 0:
            self.direction += REVERSE_DIRECTION + direction_value
        else:
            self.direction += direction_value

        self.display_stats()

    def change_gear(self, selected_gear = FORWARD): #selected_gear is either FORWARD or REVERSE
        if self.broken == True:
            return
        desired_gear = 0
        direction_change = False

        if self.gear > 0 and selected_gear == 0 or self.gear == 0 and selected_gear == 1:
            direction_change = True
            desired_gear = selected_gear

        if direction_change == False:
            print("Changing Up")
            if -1 >= self.speed >= -10:
                self.gear = 0
            elif 0 <= self.speed <= 10:
                self.gear = 1
            elif 5 <= self.speed <= 25:
                self.gear = 2
            elif 20 <= self.speed <= 40:
                self.gear = 3
            elif 40 <= self.speed <= 60:
                self.gear = 4
            elif 45 <= self.speed <= 80:
                self.gear = 5
            print(f"Current Gear: {self.gear}")
        else:
            for x in range(0, self.gear):
                self.gear -= 1
                print(f"Current Gear: {self.gear}")

    def display_stats(self):
        return print(f"Speed: {self.speed}, Gear: {self.gear}, Direction: {self.direction}")

    def load_simulation(self, filename):
        print("Loading simulation...")
        with open(filename, "r") as a_file:
            for line in a_file:
                self.simulation.append(line.strip())

        self.simuation_loaded = True

    def run_simulation(self):
        for action in self.simulation:
            if action == 'FORWARD':
                self.change_gear(FORWARD)
            elif action == 'ACCELERATE':
                self.accelerate()
            elif action == 'LEFT':
                self.turn_steering_wheel(LEFT)
            elif action == 'RIGHT':
                self.turn_steering_wheel(RIGHT)
            elif action == 'BRAKE':
                self.brake()
            elif action == 'REVERSE':
                self.change_gear(REVERSE)

if __name__ == '__main__':
    my_car = Car()
    my_car.load_simulation("simulation.txt")
    my_car.run_simulation()

