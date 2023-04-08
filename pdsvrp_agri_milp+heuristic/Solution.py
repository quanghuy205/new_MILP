import readData as dt


class Solution:
    def __init__(self):
        self.dt = dt.Data()
        self.dt.get_data('input/P/P-n19-k2.vrp')
        self.dt.update_params()
        self.truckTours = [[] for _ in range(self.dt.num_of_truck)]

        self.droneTours = [[] for _ in range(self.dt.num_of_drone)]

        self.U = [i for i in range(1, self.dt.num_of_customer)]

    def insertTruckNode(self, trucktour, position, node):
        self.truckTours[trucktour].insert(position, node)

    def removeTruckNode(self, trucktour, position, node):
        self.truckTours[trucktour].remove(node)

    def insertDroneNode(self, dronetour, node):
        self.droneTours[dronetour].append(node)

    def removeDroneNode(self, dronetour, node):
        self.droneTours[dronetour].remove(node)

    def insertDepot(self, routes):
        for route in routes:
            if route is None:
                route = []
            route.insert(0, 0)
            route.append(0)
    def removeDepot(self, routes):
        for route in routes:
            if route is None:
                route = []
            if route:
                route.pop(0)
                route.pop()

    def cost_truck(self):
        self.insertDepot(self.truckTours)


        cost = 0
        for route in self.truckTours:
            if route is None:
                route = []
            for i in range(len(route) - 1):
                cost += self.dt.truck_time_matrix[route[i]][route[i + 1]]
                # print(route[i], route[i + 1])

        self.removeDepot(self.truckTours)
        return cost

    def cost_drone(self):


        cost = 0
        for route in self.droneTours:
            for i in route:
                # print(i)
                cost +=  self.dt.drone_time_matrix[0][i]

        return cost

    def time_cost(self):
        return self.cost_truck() + self.cost_drone()



    def QDV_truck(self):
        qdv_truck = 0

        t_ki = [[] for i in range(len(self.truckTours))]
        # print(type(t_ki))
        # print(self.truckTours)
        self.insertDepot(self.truckTours)
        for k, route in enumerate(self.truckTours):
            arrival_time = 0

            t_ki[k].append(0)
            for i in range(len(route) - 1):
                # print(route)
                arrival_time += self.dt.truck_time_matrix[route[i]][route[i + 1]]
                t_ki[k].append(arrival_time)
        # print(t_ki)
        # self.insertDepot(self.truckTours
        for k, route in enumerate(self.truckTours):
            for i in range(len(route)-1):
                    # print(i)
                    qdv_truck = qdv_truck + self.dt.Q[route[i]] * self.dt.phi * t_ki[k][i]
                    # qdv_truck = qdv_truck + t_ki[k][i]
        self.removeDepot(self.truckTours)
        return qdv_truck
    def QDV_drone(self):
        qdv_drone = 0

        for k, route in enumerate(self.droneTours):
            for i in route:
                    qdv_drone = qdv_drone + self.dt.Q[i] * self.dt.phi * 2 * self.dt.drone_time_matrix[0][i]

        return qdv_drone

    def totalCost(self):
        return self.cost_truck() + self.cost_drone()

    def num_truck_node(self):
        n = 0
        for route in self.truckTours:
            n += len(route)
        return n
    def num_drone_node(self):
        n = 0
        for route in self.droneTours:
            n += len(route)
        return n
    def capacity_feasible(self):

        for route in self.truckTours:
            cap = 0
            for node in route:
                cap += self.dt.Q[node]
            # print('cap =', cap)
            if cap > self.dt.QT:
                return False
        return True

    # def QDV(self):
    #
    #     t_ki = [[0 for c in self.truckTours[c]] for k in self.dt.K]
    #     t_di = [[0 for c in self.droneTours[d]] for d in self.dt.D]
    #
    #     for k in self.truckTours:
    #         for i in range(len(k) - 1):
    #             t_ki[k][i] = t_ki[k][i] + self.dt.truck_time_matrix[i][j]
    #
    #     QDV = 0
    #     for truckTour in self.truckTours:
    #         for i in truckTour:
    #             if i in dt.CH:
    #                 QDV = QDV + self.dt.Q[i] * self.dt.phi_high *

'''read Data'''
# dt = dt.Data()
# dt.get_data("input/P/P-n19-k2.vrp")
# dt.update_params()
# sol = Solution()
# sol.truckTours[0].append(1)
# sol.truckTours[0].append(3)
#
# print(sol.QDV_truck())
# print(sol.truckTours)