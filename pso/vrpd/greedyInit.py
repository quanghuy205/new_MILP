import CWS
import readData as dt
import VRPtoVRPD
from utils import *
import numpy as np
'''read Data'''
dt = dt.Data()
dt.get_data("input/P/P-n19-k2.vrp")
solution = [[i for i in range(dt.num_of_customer)] ]
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
        newMinObj = np.inf
        move = []
        for i in unvisitedCustomers:
            for k in range(dt.num_of_truck):
                for p in range(truckTours[k]):
                tempTours = truckTours[k]
                objImprovement = max(objVal,  )



def computeObjVal(dt, solution):
    theta = 0.5
    TDV = 0
    makespan = 0
    cost = theta*TDV + (1-theta)*makespan
    return cost



route = [1 ,2,3]
print(dt.drone_time_matrix)
print(cost_small_drone(dt,route))
