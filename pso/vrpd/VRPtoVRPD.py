import random
import numpy as np

def convert(data, vrp_solution):
    # num_of_hybrid_trucks = data.num_of_hybrid_trucks
    num_of_trucks = data.num_of_truck
    num_of_cargo_drones = data.num_of_cargo_drone
    # num_of_trucks = 3
    # num_of_cargo_drones = 2
    # vrp_solution = [[0, 23, 2, 3, 17, 19, 31, 21, 0], [0, 20, 5, 25, 10, 15, 29, 27, 0], [0, 16, 7, 13, 1, 12, 0], [0, 26, 6, 18, 28, 4, 11, 8, 9, 22, 14, 0], [0, 24, 30, 0]]
    # num_of_vrp_routes = len(vrp_solution)
    # print(num_of_vrp_routes)
    # init tour vectors for all types of vehicle
    truck_routes = []
    cargo_drone_routes = []
    # print(vrp_solution)
    # random tour for all types of vehicles
    while num_of_trucks:
        rand = random.randint(0, len(vrp_solution) - 1)
        truck_routes.append(vrp_solution[rand])
        vrp_solution.pop(rand)
        num_of_trucks = num_of_trucks - 1

    # print(truck_routes)
    while num_of_cargo_drones:
        rand = random.randint(0, len(vrp_solution) - 1)
        cargo_drone_routes.append(vrp_solution[rand])
        vrp_solution.pop(rand)
        num_of_cargo_drones = num_of_cargo_drones - 1

    # print(cargo_drone_routes)

    return truck_routes, cargo_drone_routes
