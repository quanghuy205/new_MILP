
def cost_truck(dt, solution):
    cost = 0
    for route in solution.truckTours:
        for i in range(len(route) - 1):
            cost += dt.m_distance_matrix[route[i]][route[i + 1]]
            # print(route[i], route[i + 1])
    return cost

def cost_small_drone(dt, solution):
    cost = 0
    for route in solution.droneTours:
        for i in route:
            # print(i)
            cost += 2 * dt.drone_time_matrix[0][i]
    return cost
