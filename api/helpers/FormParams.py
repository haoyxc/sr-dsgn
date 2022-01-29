from math import tan
from api.helpers.Acetate import Acetate


class FormParams:
    def __init__(self, req_tank_initial, req_tank_capacity, req_downtime, req_butyl_demand, req_butyl_capacity, req_butyl_density, req_butyl_prod, req_ethyl_demand, req_ethyl_capacity, req_ethyl_density, req_ethyl_prod) -> None:
        self.tank_initial = float(req_tank_initial)
        self.tank_capacity = float(req_tank_capacity)
        self.downtime = float(req_downtime)

        # Don't want to store pounds. only in gallons. 
        # self.butyl_demand = float(req_butyl_demand)
        # self.butyl_capacity = float(req_butyl_capacity)
        self.butyl_density = float(req_butyl_density)
        self.butyl_prod = float(req_butyl_prod)

        # Don't want to store in pounds. only in gallons.
        # self.ethyl_demand = float(req_ethyl_demand)
        # self.ethyl_capacity = float(req_ethyl_capacity)
        self.ethyl_density = float(req_ethyl_density)
        self.ethyl_prod = float(req_ethyl_prod)
        
        # demand & capacity in gallons, per month
        self.butyl_demand_gallons = req_butyl_demand / req_butyl_density
        self.ethyl_demand_gallons = req_ethyl_demand / req_ethyl_density
        self.butyl_capacity_gallons = req_butyl_capacity / req_butyl_density
        self.ethyl_capacity_gallons = req_ethyl_capacity / req_ethyl_density
        # production PER DAY in gallons
        self.butyl_prod_gal = req_butyl_prod / req_butyl_density
        self.ethyl_prod_gal = req_ethyl_prod / req_ethyl_density
    
    def getScheduler(self):
        return 0
    def scheduleMonth(self):
        return 0
    def isTankFull(self, tank_amount):
        return tank_amount < self.tank_capacity
    
    def canProduceButyl(self, tank_amount, butyl_month_total):
        return self.isTankFull(self, tank_amount) and butyl_month_total <= self.butyl_capacity_gallons

    def canProduceEthyl(self, tank_amount, ethyl_month_total):
        return self.isTankFull(self, tank_amount) and ethyl_month_total <= self.ethyl_capacity_gallons

    # if 
    def cantProduceEither(self, tank_amount, butyl_month_total, ethyl_month_total):
        return not (self.canProduceButyl(self, tank_amount, butyl_month_total) or self.canProduceEthyl(self, tank_amount, ethyl_month_total))

    def solveMonth(self, n, gallons_in_tank, butyl_month_total, ethyl_month_total):
        '''
        n: number of days in the month
        butyl_month_total: how much butyl was already produced that month
        ethyl_mont_total: how much ethyl was already produced that month
        '''
        # base case: tank is full
        if gallons_in_tank >= self.tank_capacity:
            return 0
        # base case: can't produce either
        if not self.canProduceButyl(self, gallons_in_tank, butyl_month_total) and not self.canProduceEthyl(self, gallons_in_tank, ethyl_month_total):
            return 0
        if n == 1:
            return n
        tank_remaining = self.tank_capacity - self.tank_initial # in gallons
        # to produce butyl: need to check that month capacity is < butyl capacity, butyl_prod per day < tank_remaining
        return 1
    def guessMonth(self, n):
        return 0