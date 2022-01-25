class FormParams:
    def __init__(self, req_tank_initial, req_tank_capacity, req_downtime, req_butyl_demand, req_butyl_capacity, req_butyl_density, req_butyl_prod, req_ethyl_demand, req_ethyl_capacity, req_ethyl_density, req_ethyl_prod) -> None:
        self.tank_initial = float(req_tank_initial)
        self.tank_capacity = float(req_tank_capacity)
        self.downtime = float(req_downtime)
        self.butyl_demand = float(req_butyl_demand)
        self.butyl_capacity = float(req_butyl_capacity)
        self.butyl_density = float(req_butyl_density)
        self.butyl_prod = float(req_butyl_prod)
        self.ethyl_demand = float(req_ethyl_demand)
        self.ethyl_capacity = float(req_ethyl_capacity)
        self.ethyl_density = float(req_ethyl_density)
        self.ethyl_prod = float(req_ethyl_prod)
        # demand & capacity in gallons
        self.butyl_demand_gallons = self.butyl_demand / self.butyl_density
        self.ethyl_demand_gallons = self.ethyl_demand / self.ethyl_density
        self.butyl_capacity_gallons = self.butyl_capacity / self.butyl_density
        self.ethyl_capacity_gallons = self.ethyl_capacity / self.ethyl_density
    
    def getScheduler(self):
        return 0
    def scheduleMonth(self):
        return 0