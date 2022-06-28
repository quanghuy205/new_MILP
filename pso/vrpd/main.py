import CWS
import readData as dt
import VRPtoVRPD
from utils import *
'''read Data'''
dt = dt.Data()
dt.get_data("input/P/P-n19-k2.vrp")

'''init VRP'''
vrp_solution = CWS.ClarkeAndWright(dt)
print("vrp solution", vrp_solution)

'''convert to initial VRPD solution'''
truck_routes, cargo_drone_routes = VRPtoVRPD.convert(dt, vrp_solution)
print("truck routes", truck_routes)
print("cargo_drones routes", cargo_drone_routes)

print(cost_drone(dt, cargo_drone_routes[0]))
print(cost_truck(dt, truck_routes[0]))