import readData as dt


class Solution:
    def __init__(self, dt):
        self.dt = dt
        self.truckTours = [[] for _ in range(self.dt.num_of_truck)]

        self.droneTours = [[] for _ in range(self.dt.num_of_drone)]

        self.U = [i for i in range(1, self.dt.num_of_customer)]

    def insertDepot(self, routes):

        for route in routes:
            route.insert(0, 0)
            route.append(0)

    def cost_truck(self):
        cost = 0
        for route in self.truckTours:
            for i in range(len(route) - 1):
                cost += self.dt.truck_time_matrix[route[i]][route[i + 1]]
                # print(route[i], route[i + 1])
        return cost

    def cost_drone(self):
        cost = 0
        for route in self.droneTours:
            for i in route:
                # print(i)
                cost += 2 * dt.drone_time_matrix[0][i]
        return cost

    def time_cost(self):
        return self.cost_truck() + self.cost_drone()



    def QDV_truck(self):
        qdv_truck_high = 0
        qdv_truck_low = 0
        t_ki = [[] for i in range(len(self.truckTours))]
        print(type(t_ki))
        print(self.truckTours)
        for k, route in enumerate(self.truckTours):
            arrival_time = 0
            t_ki[k].append(0)
            for i in range(len(route) - 1):
                arrival_time += self.dt.truck_time_matrix[route[i]][route[i + 1]]
                t_ki[k].append(arrival_time)

        for k, route in enumerate(self.truckTours):
            for i in range(len(route)):
                if route[i] in self.dt.CH:
                    qdv_truck_high = qdv_truck_high + self.dt.Q[route[i]] * self.dt.phi_high * t_ki[k][i]
                else:
                    qdv_truck_low = qdv_truck_low + self.dt.Q[route[i]] * self.dt.phi_low * t_ki[k][i]
        return qdv_truck_low + qdv_truck_high
    def QDV_drone(self):
        qdv_drone_high = 0
        qdv_drone_low = 0
        for k, route in enumerate(self.truckTours):
            for i in range(len(route)):
                if route[i] in self.dt.CH:
                    qdv_drone_high = qdv_drone_high + self.dt.Q[route[i]] * self.dt.phi_high * self.dt.drone_time_matrix[0][route[i]]
                else:
                    qdv_drone_low = qdv_drone_low + self.dt.Q[route[i]] * self.dt.phi_low * self.dt.drone_time_matrix[0][route[i]]
        return qdv_drone_high + qdv_drone_low

    def totalCost(self):
        return self.cost_truck() + self.cost_drone() + self.QDV_truck() + self.QDV_drone()
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
dt = dt.Data()
dt.get_data("input/P/P-n19-k2.vrp")
dt.update_params()
sol = Solution(dt)
sol.truckTours[0].append(2)
sol.droneTours[0].append(2)
sol.insertDepot(sol.truckTours)
print(sol.QDV_drone())
