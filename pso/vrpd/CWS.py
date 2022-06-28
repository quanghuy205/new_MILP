import readData as dt
from utils import *
'''
     Clarke and Wright Algorithm
'''



# print(len(dt.distance_matrix))
# print(dt.num_of_customers)


def createInitialRoutes(dt):
    """
    Each customer i goes to a new route r = (0, i, 0)
    that goes from the depot to the customer and returns to the depot
    :return: return the list with the n routes
    """
    routes = []  # solution
    for i in range(1, dt.num_of_customer):
        routes.append([i])  # add depot later
    return routes


def computeSavingsList(dt):
    """
    savings_list = {};
    foreach i, j ∈ V - {0} do
        Sij = C(0, i) + C(0, j) - C(i, j);
        savings_list <- Si, j;
    sort_decreasing(savings_list);
    return savings_list;
    :return: list of savings, sorted in descending order of savings
    """
    list = []
    for i in range(1, dt.num_of_customer):
        for j in range(1, dt.num_of_customer):
            if i != j:
                save = dt.distance_matrix[i][0] + dt.distance_matrix[0][j] - dt.distance_matrix[i][j]
                # sij = di0 + d0j − dij , for all i, j ≥ 1 and i != j;
                list.append([(i, j), save])

    list.sort(key=lambda x: x[1], reverse=True)
    return list
# routes = createInitialRoutes()
# list = computeSavingsList()
#
# print(routes)
print(list)

# sum up to obtain the total passengers belonging to a route
def sum_cap(route, dt):
    sum_cap = 0
    for node in route:
        sum_cap += dt.demand_matrix[node]
    return sum_cap

#sum up of arrival time to obtain the total passengers belonging to a route


def feasibleMerge(i, j, routes, dt):
    """
    For two routes (s and e) to be merged,
     i must be the last customer to be visited in route s
     j must be the first customer to be visited on route e

    and if the sum of the demands of the customers of the two routes does not exceed the maximum capacity
    """
    s, e = [], []  #start and ending route
    for route in routes:
        if route[0] == j:  #if route starts with j
            s = route  #initial route is now the route started with j
        elif route[-1] == i:  #if route ends with i
            e = route   #the final route is now the route that ends with i

        if s and e:  #if there was a route that started with j and another that ended with i
            if (sum_cap(s,dt) + sum_cap(e,dt) <= dt.truck_capacity):   #test if the sum of the demands of the two routes does not exceed the maximum capacity
                return True  #i

    return False


def mergeRoutes(i, j, routes):
    """
        It merges between routes r and s, being:
            e the route that contains j: r = (0, ..., j, 0)
            s the route that contains i: s = (0, i, ..., 0)
        """
    s, e = [], []
    for route in routes:
        if route[0] == j:
            s = route
        elif route[-1] == i:
            e = route

    routes.remove(s)  # remove s
    routes.remove(e)  # remove e
    routes.append(e + s)


def insertDepot(routes):

    for route in routes:
        route.insert(0, 0)
        route.append(0)

def ClarkeAndWright(dt):
    """
        1 - routes <- create_initial_routes(V);
        2 - savings_list = compute_savings_list(V);
        3 - foreach i, j ∈ savings_list do
            4 - if feasible_merge(i, j, Q) then
                5 - routes <- merge_routes(i, j)
        step 5 the algorithm tries to merge the routes to which i and j belong
        """
    solution = (createInitialRoutes(dt)).copy()

    listOfSaves = computeSavingsList(dt)
    for save in listOfSaves:
        print(solution)
        i, j = save[0]
        if feasibleMerge(i, j, solution, dt):
            mergeRoutes(i, j, solution)
            print("merge: ", i, j)

    insertDepot(solution)
    return solution
