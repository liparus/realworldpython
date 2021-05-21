

#Preferred order of imports: sys, lib, user
import sys
import random
import itertools
import numpy as np
import cv2 as cv

#Assing constants (not truly immutable)
MAP_FILE = 'cape_python.png'

#Draw "search areas" on the image as rectangles,
#OpenCV will define each search area by the pixel number
#at the corner points.

#Assign a variable to hold these four points as tuple:"""
SA1_CORNERS = (130, 265, 180, 351) # (UL-X, UL-Y, LR-X, LR-Y)
SA2_CORNERS = (80, 255, 130, 305)  # (UL-X, UL-Y, LR-X, LR-Y)
SA3_CORNERS = (105, 205, 155, 255) # (UL-X, UL-Y, LR-X, LR-Y)

#Create class as a template for search and rescue mission
#that allows for three search areas:
class Search():
    """Bayesian Search & Rescue game with 3 search areas"""

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print("Could not load map file {}".format(MAP_FILE),
                    file=sys.stderr)
            sys.exit(1)
    
    self.area_actual = 0
    self.sailor_actual = [0, 0] #As "local" coords without search area

    self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3],
                        SA1_CORNERS[0] : SA1_CORNERS[2]]

    self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3],
                        SA2_CORNERS[0] : SA2_CORNERS[2]]

    self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3],
                        SA3_CORNERS[0] : SA3_CORNERS[2]]

    self.p1 = 0.2
    self.p2 = 0.5
    self.p3 = 0.3

    self.sep1 = 0
    self.sep2 = 0
    self.sep3 = 0





