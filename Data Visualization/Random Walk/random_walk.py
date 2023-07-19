from random import choice

class RandomWalk():

    def __init__(self, num_points= 5000):
        self.num_points = num_points

        '''The walk starts at the coordinate (0,0)'''
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Calculate the points in the walk'''

        #Randomly deciding which direction to go, and how far
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1]) #decides movement in the left, right, or vertical direction
            x_distance = choice([0,1,2,3,4]) #decides the distance to be walked in the chosen direction
            x_walk = x_distance *x_direction

            y_direction = choice([1,-1]) #decides upward, downward, or horizontal movement
            y_distance = choice([0,1,2,3,4])
            y_walk = y_distance *y_direction

            if x_walk == 0 and y_walk == 0:
                continue

            x = self.x_values[-1] + x_walk
            y = self.y_values[-1] + y_walk

            self.x_values.append(x)
            self.y_values.append(y)