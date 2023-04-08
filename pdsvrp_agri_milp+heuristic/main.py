from corefuncs import *
import readData as dt
import VRPtoVRPD
from utils import *
from Solution import Solution
import time
from copy import deepcopy
import os
import pandas as pd
# i_max = 100
# t_max = 5000
#
dt = dt.Data()
dt.get_data("input/test1/P-n8-k2.vrp")
dt.update_params()
def run(dt):
    '''read Data'''

    '''init VRP'''
    S_vrdp_ap = initSol(dt)

    print("vrdp init solution: ", 'truck tours = ', S_vrdp_ap.truckTours,'drone tours =', S_vrdp_ap.droneTours,  'total cost', S_vrdp_ap.totalCost() )
    #
    # S_vrdp_ap, list_truck_des, list_drone_des, list_all_des = destroy(deepcopy(S_vrdp_ap))
    # print("vrdp destroy solution: ", 'truck tours = ', S_vrdp_ap.truckTours,'drone tours =', S_vrdp_ap.droneTours)
    # des_list = list_truck_des + list_drone_des + list_all_des
    # S_vrdp_ap = repair(S_vrdp_ap, list_truck_des, list_drone_des, list_all_des)
    # print("vrdp repaired solution: ", 'truck tours = ', S_vrdp_ap.truckTours,'drone tours =', S_vrdp_ap.droneTours, 'total cost', S_vrdp_ap.totalCost())
    #
    S_best = Solution()
    S_current = Solution()
    S_best = deepcopy(S_vrdp_ap)
    S_current = deepcopy(S_vrdp_ap)

    t = 0
    i = 0
    i_max = 20
    t_max = 100
    S_temp = Solution()
    S_temp_s = Solution()
    print(S_current.totalCost())
    start = time.time()         #starting time
    t = 0                       #elapsed time
    while t < t_max:
        while i < i_max:
            print(i)

            S_temp, list_truck_des, list_drone_des, list_all_des = destroy(deepcopy(S_current))
            des_list = list_truck_des + list_drone_des + list_all_des
            S_temp = repair(deepcopy(S_current),des_list)
            print("Stemp", S_temp.truckTours)
            S_temp_s = deepcopy(S_temp)
            S_temp_s = local_search(S_temp_s)

            print(S_temp_s.totalCost())
            if S_temp_s.totalCost() < S_current.totalCost():
                print('trueeeee'
                      ''
                      ''
                      ''
                      ''
                      ''
                      ''
                      '')
                S_current = deepcopy(S_temp_s)
                i = 0
            else:
                i = i + 1

        if S_current.totalCost() < S_best.totalCost():
            bestime = time.time() - start
            print('zzo',bestime)
            return
            S_best = deepcopy(S_current)
            print('best', S_best.truckTours, S_best.droneTours)
        else:
            S_current = pertubate(dt)

            print('asdfsdafasdfafs')
            i = 0
        t = time.time() - start
    print('best', S_best.truckTours, S_best.droneTours)
    print(S_best.totalCost())

    #
    #
    return S_best.totalCost()
n = 10
obj = []
dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.DataFrame()

for i in range(n):
    obj.append(run(dt))
df['obj'] = obj
df.to_csv(dir_path + '/result/' + 'n8k2', index=False, header=False)
