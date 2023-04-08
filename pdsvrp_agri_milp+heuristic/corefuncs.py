from verypy.routedata import RouteData
from verypy.cvrp_io import read_TSPLIB_CVRP
from verypy.classic_heuristics.parallel_savings import parallel_savings_init
from verypy.classic_heuristics.mole_jameson_insertion import mole_jameson_insertion_init,objf
from verypy.util import sol2routes
from verypy.local_search.intra_route_operators import do_2opt_move,do_3opt_move
from verypy.local_search.inter_route_operators import do_2point_move
from verypy.util import objf as route_l
from verypy.util import totald as route_d
from verypy.classic_heuristics import *
from verypy.classic_heuristics.cheapest_insertion import cheapest_insertion_init
from verypy.util import objf


import numpy as np
import readData as dt
from utils import *
from Solution import Solution
from copy import deepcopy
import random


'''read Data'''
dt = dt.Data()
dt.get_data("input/test1/P-n8-k2.vrp")
dt.update_params()

def initSol(dt):


    unvisitedNodes = deepcopy(dt.C)
    print(unvisitedNodes)
    bestSol = Solution()

    while unvisitedNodes:

        i = unvisitedNodes[0]
        print(i)

        tempSol = Solution()

        minCost = 1000000000
        print(minCost)
        tempSol = deepcopy(bestSol)
        for k in range(dt.num_of_truck):
            print('k = ', k)
            for p in range(len(tempSol.truckTours[k]) + 1):
                print('p = ', p)
                tempSol.insertTruckNode(k, p, i)

                print(tempSol.totalCost(), minCost)
                if tempSol.totalCost() < minCost and tempSol.capacity_feasible():
                    bestSol = deepcopy(tempSol)
                    minCost = bestSol.totalCost()

                tempSol.removeTruckNode(k,p,i)


        if i in dt.CD and dt.QD >= dt.Q[i]:

            for d in dt.D:
                tempSol.insertDroneNode(d, i)
                print('d = ', d)

                if tempSol.totalCost() < minCost :
                    bestSol = deepcopy(tempSol)
                    minCost = bestSol.totalCost()
                tempSol.removeDroneNode(d, i)


        unvisitedNodes.remove(i)
    # print(bestSol.truckTours)
    # print(bestSol.droneTours)
    #
    # print(bestSol.cost_drone())
    return bestSol







def destroy(sol):

    print('sdfsdfsd', sol.truckTours)
    num_truck_destroy = int(random.randint(1, sol.num_truck_node())/2)



    '''---'''
    # print(num_truck_destroy)
    # print(num_drone_destroy)

    '---'
    list_truck = []
    list_drone = []

    list_truck_destroy = []
    list_drone_destroy = []

    '''joint truck lists and drone lists'''
    for route in sol.truckTours:
        list_truck += route

    for route in sol.droneTours:
        list_drone += route


    '''get destroy list'''
    list_truck_destroy = random.sample(list_truck, num_truck_destroy)
    if sol.num_drone_node():
        num_drone_destroy = int(random.randint(1, sol.num_drone_node())/2)
        list_drone_destroy = random.sample(list_drone, num_drone_destroy)
    # print('truck des: ', list_truck_destroy)
    # print('drone des: ', list_drone_destroy)
    '''remove nodes from sol'''
    for node in list_truck_destroy:
        for route in sol.truckTours:
            if node in route:
                route.remove(node)
    for node in list_drone_destroy:
        for route in sol.droneTours:
            if node in route:
                route.remove(node)


    '''all node'''
    num_all_destroy = int(random.randint(1, sol.num_drone_node() + sol.num_truck_node())/2)
    list_all = []
    for route in sol.truckTours:
        list_all += route

    for route in sol.droneTours:
        list_all += route
    list_all_destroy = []
    # print(num_all_destroy)
    list_all_destroy = random.sample(list_all, num_all_destroy)
    # print('all des', list_all_destroy)
    for route in sol.truckTours:
        list_all += route
    for route in sol.droneTours:
        list_all += route

    for node in list_all_destroy:
        for route in sol.truckTours:
            if node in route:
                route.remove(node)
        for route in sol.droneTours:
            if node in route:
                route.remove(node)
    return sol, list_truck_destroy, list_drone_destroy, list_all_destroy


def repair(sol, des_list):

    '''s1 repair'''
    while des_list:
        s1 = deepcopy(sol)
        s2 = deepcopy(sol)

        '''truck tour insertion'''
        node = random.choice(des_list)
        des_list.remove(node)
        s1 = cheapest_insertion_truck(node, s1)
        '''drone tour insertion'''
        if node in sol.dt.CD:
            s2 = cheapest_insertion_drone(node, s2)
        else:
            s2 = deepcopy(s1)
        if s1.totalCost() > s2.totalCost():
            sol = deepcopy(s2)
        else:
            sol = deepcopy(s1)
    return sol
def cheapest_insertion_truck(node, sol):
    tempSol = deepcopy(sol)

    minCost = 1000000

    for k in range(tempSol.dt.num_of_truck):
        # print('k = ', k)
        for p in range(len(tempSol.truckTours[k]) + 1):
            # print('p = ', p)
            tempSol.insertTruckNode(k, p, node)

            # print(tempSol.totalCost(), minCost)
            if tempSol.totalCost() < minCost and tempSol.capacity_feasible():
                sol = deepcopy(tempSol)
                minCost = sol.totalCost()

            tempSol.removeTruckNode(k, p, node)
    return sol

def cheapest_insertion_drone(node, sol):
    tempSol = deepcopy(sol)
    minCost = 1000000
    if node in sol.dt.CD and sol.dt.QD >= sol.dt.Q[node]:
        for d in sol.dt.D:
            tempSol.insertDroneNode(d, node)
            # print('d = ', d)
            if tempSol.totalCost() < minCost:
                sol = deepcopy(tempSol)
                minCost = sol.totalCost()
            tempSol.removeDroneNode(d, node)
    return sol
# sol = Solution()
# sol.droneTours[0].append(1)
# # sol.truckTours[0].append(3)
# sol = cheapest_insertion_drone(11, sol)
# # sol = cheapest_insertion_truck(4,sol)
# # sol = cheapest_insertion_truck(10,sol)
# print(sol.droneTours)
def local_search(sol):
    path = r"input/test1/P-n8-k2.vrp"
    problem = read_TSPLIB_CVRP(path)
    '''do 2 opt moove'''
    sol.insertDepot(sol.truckTours)
    for i in range(len(sol.truckTours)):
        route = sol.truckTours[i]
        if route != [0,0]:
            rel, delta_f = do_2opt_move(route, D=problem.distance_matrix)
            if rel is not None:
                sol.truckTours[i] = rel
    sol.removeDepot(sol.truckTours)
    '''do 3opt move'''
    sol.insertDepot(sol.truckTours)
    print(sol.truckTours)
    for i in range(len(sol.truckTours)):
        route = sol.truckTours[i]
        if route != [0, 0]:
            rel, delta_f = do_3opt_move(route, D=problem.distance_matrix)
            print(rel)
            if rel is not None:
                sol.truckTours[i] = rel
    sol.removeDepot(sol.truckTours)

    '''do 2 point move inter route exchange'''
    sol.insertDepot(sol.truckTours)
    print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',sol.truckTours)
    r1rd = RouteData(sol.truckTours[0], route_l(sol.truckTours[0], D=problem.distance_matrix),
                     route_d(sol.truckTours[0], d=problem.customer_demands), None)
    r2rd = RouteData(sol.truckTours[1], route_l(sol.truckTours[1], D=problem.distance_matrix),
                     route_d(sol.truckTours[1], d=problem.customer_demands), None)
    # print('r1rd', r1rd.route)
    # print('r2rd', r2rd.route)

    # result = do_2point_move(r1rd, r2rd, D=problem.distance_matrix)
    # r1rd, r2rd, delta = result
    # print('r1rd', r1rd.route)
    # print('r2rd', r2rd.route)
    while True:
        # print('a')
        result = do_2point_move(r1rd, r2rd, D=problem.distance_matrix)
        if result[0] is None:
            break
        r1rd, r2rd, delta = result
        # print('r1rd', r1rd.route)
        # print('r2rd', r2rd.route)
        sol.truckTours[0] = deepcopy(r1rd.route)
        sol.truckTours[1] = deepcopy(r2rd.route)
    sol.removeDepot(sol.truckTours)
    print(sol.truckTours)
    return sol
def pertubate(dt):


    unvisitedNodes = deepcopy(dt.C)
    print(unvisitedNodes)
    bestSol = Solution()
    random.shuffle(unvisitedNodes)
    while unvisitedNodes:

        i = unvisitedNodes[0]
        print(i)

        tempSol = Solution()

        minCost = 1000000000
        print(minCost)
        tempSol = deepcopy(bestSol)
        for k in range(dt.num_of_truck):
            print('k = ', k)
            for p in range(len(tempSol.truckTours[k]) + 1):
                print('p = ', p)
                tempSol.insertTruckNode(k, p, i)

                print(tempSol.totalCost(), minCost)
                if tempSol.totalCost() < minCost and tempSol.capacity_feasible():
                    bestSol = deepcopy(tempSol)
                    minCost = bestSol.totalCost()

                tempSol.removeTruckNode(k,p,i)


        if i in dt.CD and dt.QD >= dt.Q[i]:

            for d in dt.D:
                tempSol.insertDroneNode(d, i)
                print('d = ', d)

                if tempSol.totalCost() < minCost :
                    bestSol = deepcopy(tempSol)
                    minCost = bestSol.totalCost()
                tempSol.removeDroneNode(d, i)


        unvisitedNodes.remove(i)
    # print(bestSol.truckTours)
    # print(bestSol.droneTours)
    #
    # print(bestSol.cost_drone())
    return bestSol
print(pertubate(dt).truckTours)

# print(rel)