import CWS
import readData as dt
import VRPtoVRPD
from utils import *
import numpy as np
def DP(dt):
    truckTours = [[0] for k in range(dt.num_of_truck)]
    cargoDroneTours = [[0] for cd in range(dt.num_of_cargo_drone)]
    smallDroneTours = [[None] for sd in range(dt.num_of_cargo_drone)]
    unvisitedCustomers = [i for i in range(1, dt.num_of_customer)]
    C_d = []
    truckCost = 0
    droneCost = 0
    objVal = 0

    while unvisitedCustomers:
        newObj = np.inf
        move = []
        for i in unvisitedCustomers:
            for k in range(dt.num_of_truck):
                tempTours = truckTours[k]
                objImprovement = max(objVal,  )


'''read Data'''
dt = dt.Data()
dt.get_data("input/P/P-n19-k2.vrp")
def computeObjVal(dt, truckTours, cargoDroneTours, smalldroneTours):
    pass

c


