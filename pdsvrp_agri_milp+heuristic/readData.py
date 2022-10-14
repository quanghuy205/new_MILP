import math

class Data():
    def __init__(self):
        self.num_of_customer = None #including depot
        self.X = None
        self.Y = None
        self.num_of_truck = 2
        self.num_of_cargo_drone = 1
        self.num_of_drone = 2
        self.truck_capacity = None
        self.small_drone_capacity = None
        self.distance_matrix = None
        self.m_distance_matrix = None
        self.truck_time_matrix = None
        self.drone_time_matrix = None
        self.demand_matrix = None
        self.sp = 1.5 #speed factor


        '''----------------PARAMS----------------'''

        self.n = None

        self.C = None
        self.C_0 = None
        self.C_plus = None
        self.N = None
        self.K = None
        self.D = None
        self.Q = None
        self.Q = None

        self.CL = None
        self.CH = None
        self.QT = None
        self.QD = None
        self.TL = None
        self.TH = None

        self.cost_t = None
        self.cost_td = None
        self.M = None
        self.theta = None
        self.phi_low = None
        self.phi_high = None
        self.CD = None
    def get_data(self, instance_name):
        a1 = open(instance_name, 'r')
        # reading content of a1 and storing in a2
        a2 = a1.read()
        # splitting contents in a2 into list from where newline is started
        a2 = a2.split('\n')
        # For reading number of customers, splitting values in third index of a2 list into new list
        temp_customer = a2[3].split()
        # converting a list value to integer which gives total customers
        self.num_of_customer = int(temp_customer[2])
        # reading vehicle capacity which is in five index of list b2
        temp_capacity = a2[5].split()
        self.truck_capacity = int(temp_capacity[2])
        self.small_drone_capacity = self.truck_capacity/1.5
        a1.close()
        length = self.num_of_customer
        # initializing array matrices of demand of customers, X coordinate , Y coordinate using compact for loop
        self.X = [0 for j in range(self.num_of_customer)]
        self.Y = [0 for j in range(self.num_of_customer)]
        self.demand_matrix = [0 for j in range(length)]
        # -----------reading values of x,y nodes of customers as well as their demand by splitting into lists from the respective indices of their start-----
        for j in range(0, length):
            x_y_values = a2[j + 7].split()
            self.demand_matrix[j] = int(float(a2[self.num_of_customer + 8 + j].split()[1]))
            self.X[j] = int(float(x_y_values[1]))
            self.Y[j] = int(float(x_y_values[2]))

        # ------------------------------[calculating distance between nodes and computing the distance matrix]--------------------------------------------

        # initializing 2-d distance matrix that computes distance between customers and customer & depot
        self.distance_matrix = [[0 for i in range(self.num_of_customer)] for j in range(self.num_of_customer)]
        for i in range(self.num_of_customer):
            for j in range(self.num_of_customer):
                if i == j:
                    self.distance_matrix[i][j] = 0
                elif i > j:  # since this matrix is symmetrical
                    self.distance_matrix[i][j] = self.distance_matrix[j][i]
                else:
                    self.distance_matrix[i][j] = math.sqrt((self.X[j] - self.X[i]) ** 2 + (self.Y[j] - self.Y[i]) ** 2)
        self.truck_time_matrix = self.distance_matrix
        # initializing drone time matrix
        self.drone_time_matrix = [[0 for i in range(self.num_of_customer)] for j in range(self.num_of_customer)]
        for i in range(self.num_of_customer):
            for j in range(self.num_of_customer):
                self.drone_time_matrix[i][j] = self.distance_matrix[i][j];

        for i in range(self.num_of_customer):
            for j in range(self.num_of_customer):
                self.drone_time_matrix[i][j] = round(self.drone_time_matrix[i][j], 2)
                self.distance_matrix[i][j] = round(self.distance_matrix[i][j], 2)

        for i in range(self.num_of_customer):
            self.distance_matrix[i].append(self.distance_matrix[i][0])


        for i in range(self.num_of_customer):
            self.drone_time_matrix[i].append(self.drone_time_matrix[i][0])
        # initializing drone time matrix
        for i in range(self.num_of_customer):
            for j in range(self.num_of_customer):
                self.drone_time_matrix[i][j] = self.drone_time_matrix[i][j] / self.sp
        for i in range(self.num_of_customer):
            for j in range(self.num_of_customer):
                self.drone_time_matrix[i][j] = round(self.drone_time_matrix[i][j], 2)
        self.update_params()

    def update_params(self):
        self.n = self.num_of_customer - 1

        self.C = [i for i in range(1, self.n + 1)]
        self.C_0 = [i for i in range(0, self.n + 1)]
        self.C_plus = [i for i in range(1, self.n + 2)]
        self.N = [i for i in range(0, self.n + 2)]
        self.K = [i for i in range(self.num_of_truck)]
        self.D = [i for i in range(self.num_of_drone)]
        self.Q = self.demand_matrix
        self.Q = self.demand_matrix
        self.Q.append(0)
        self.CL = [i for i in range(5, 10)]
        self.CH = [i for i in range(1, 5)]
        self.QT = self.truck_capacity
        self.QD = 17
        self.TL = 50
        self.TH = 100
        self.sp = 2
        self.cost_t = self.m_distance_matrix
        self.cost_td = self.distance_matrix
        self.M = 10000000
        self.theta = 1
        self.phi_low = 0.002
        self.phi_high = 0.02
        self.sp = 1.5
        self.CD = self.C