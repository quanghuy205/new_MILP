import CWS
import readData as dt
import VRPtoVRPD
from utils import *
import numpy as np

class Solution:
    def __init__(self, dt):
        self.truckTours = [[0] for k in range(dt.num_of_truck)]

        self.droneTours = [[] for sd in range(dt.num_of_small_drone)]

        self.U = [i for i in range(dt.num_of_customer - 1)]

    def cost(self):
        cost = 0
        for truckTour in self.truckTours:
            truckTour.append(0)
            cost += cost_truck(dt,truckTour)
        for cargoDroneTour in self.cargoDroneTours:
            cargoDroneTour.append(0)

    def deterioration_cost(self):
        pass
