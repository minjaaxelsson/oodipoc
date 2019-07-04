#!/usr/bin/env python

"""
An emotion library for a robot.
"""
import numpy as np
__author__ = "@minjaaxelsson"
__license__ = "MIT"


class Emotion:

    #Initialize table full of empty objects. Set center and current to center.
    def __init__(self, size):
        self.size = int(round(size))
        self.emomatrix = np.empty([self.size,self.size], dtype=object)
        self.center = [int(round(self.size/2)), round(self.size/2)]
        self.current = self.center
        self.current_x = self.center[0]
        self.current_y = self.center[1]
        self.maximum = self.size-1
        self.minimum = 0

    #Create area with certain name into emotion table
    def create_area(self, name, x_start, y_start, x_end, y_end):
        for j in range (self.clamp(y_start), self.clamp(y_end+1)):
            for i in range (self.clamp(x_start), self.clamp(x_end+1)):
                self.emomatrix[i,j] = name

    #Return current emotion
    def get_emotion(self):
        return self.emomatrix[self.current_x, self.current_y]

    #Check index not out of bounds
    def clamp(self, clampthis):
        return max(min(self.maximum, clampthis), self.minimum)

    #Modify current emotion
    def mod_emotion(self, x_increment, y_increment):
        self.current_x = self.clamp(self.current_x + x_increment)
        self.current_y = self.clamp(self.current_y + y_increment)
        self.current = [self.current_x, self.current_y]
        return self.current

   
    #TESTING METHODS

    #Return emotion in certain place. Use for testing.
    def get_emotion_inplace(self,x,y):
        return self.emomatrix[x,y]

    #Print all emotions row at a time. Use for testing.
    def print_emotions(self):
        for j in range (0, self.size):
            for i in range (0, self.size):
                print(self.emomatrix[i,j])
