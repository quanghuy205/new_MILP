from corefuncs import *
import readData as dt
import VRPtoVRPD
from utils import *
import Solution as S
import time

i_max = 100
t_max = 5000

'''read Data'''
dt = dt.Data()
dt.get_data("input/P/P-n19-k2.vrp")
dt.update_params()

'''init VRP'''
vrpd_solution = initSol(dt)

print("vrp solution", vrpd_solution)

S_best = vrpd_solution
S_current = vrpd_solution

t = 0
i = 0
S_temp = S.Solution(dt)
start = time.time()         #starting time
t = 0                       #elapsed time
while t < t_max:
    while i < i_max:
        S_temp = destroy(S_current)
        S_temp = repair(S_current)
        S_temp_s = local_search(S_temp)
        if S_temp_s.cost() < S_current.cost():
            S_current = S_temp_s
            i = 0
        else:
            i = i + 1
    if S_current.cost() < S_best.cost():
        S_best = S_current
        i = 0
    else:
        S_current = pertubate(S_current)

    t = time.time() - start




