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

E_n51_k5_path = r"input/P/P-n19-k2.vrp"

problem = read_TSPLIB_CVRP(E_n51_k5_path)
print(problem.distance_matrix)
solution =  cheapest_insertion_init(

    D=problem.distance_matrix,
    d=problem.customer_demands,
    C=problem.capacity_constraint)

for route_idx, route in enumerate(sol2routes(solution)):
    print("Route #%d : %s"%(route_idx+1, route))
print(objf(solution, problem.distance_matrix))
# route = [0,1,2,3,4,0]
# print(objf(route,   D=problem.distance_matrix))
#
# sol, delta_f = do_2opt_move(route,D=problem.distance_matrix)
# print(objf(sol, D=problem.distance_matrix) )
# print(sol)
# rd = RouteData(route, route_l(route, D=problem.distance_matrix), route_d(route,     d=problem.customer_demands), None)
#
# print(objf(solution,D=problem.distance_matrix))
# # do_3opt_move(sol2routes(solution),D= problem.distance_matrix)
# # route = do_2opt_move(rd.route,D= problem.distance_matrix)
# print(rd.route)
r1rd = RouteData(sol2routes(solution)[0], route_l(sol2routes(solution)[0],D=problem.distance_matrix), route_d(sol2routes(solution)[0], d=  problem.customer_demands), None)
r2rd = RouteData(sol2routes(solution)[1], route_l(sol2routes(solution)[1],D=problem.distance_matrix), route_d(sol2routes(solution)[1], d=  problem.customer_demands), None)
result = do_2point_move(r1rd, r2rd, D= problem.distance_matrix)
r1rd, r2rd, delta = result
print(r1rd.cost + r2rd.cost)
# for route_idx, route in enumerate(sol2routes(solution)):
#     print("Route #%d : %s"%(route_idx+1, route))
#     print(r1rd.cost+ r2rd.cost)
#
#
#
# print(objf(solution,D=problem.distance_matrix))