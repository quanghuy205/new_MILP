from utils import *
from Solution import Solution
# '''read Data'''
# dt = dt.Data()
# dt.get_data("input/P/P-n19-k2.vrp")
# solution = [[i for i in range(dt.num_of_customer)] ]

def initSol(dt):
    initial_sol = Solution(dt)
    truckTours = initial_sol.truckTours
    droneTours = initial_sol.droneTours

    unvisitedCustomers = [i for i in range(1, dt.num_of_customer)]
    tempSol = Solution(dt)
    C_d = []
    truckCost = 0
    droneCost = 0
    objVal = 0

    while unvisitedCustomers:
        bestPos = {}
        for i in unvisitedCustomers:
            for k in range(dt.num_of_truck):
                for p in range(truckTours[k]):
                tempSol.truckTours
                temp_obj = tempTours.totalCost()




def computeObjVal(dt, 0):
    theta = 0.5
    TDV = 0
    makespan = 0
    cost = theta*TDV + (1-theta)*makespan
    return cost



def destroy(sol):
    pass
def repair(sol):
    pass
def local_search(sol):
    pass
def pertubate(sol):
    pass

