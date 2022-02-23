from math import tan
from api.helpers.Acetate import Acetate
import random

from api.helpers.Schedule import Schedule
from api.helpers.Acetate import Acetate
from api.helpers.Tank import Tank


class FormParams:
    def __init__(self, req_tank_initial, req_tank_capacity, req_turnover, req_butyl_demand, req_butyl_capacity, req_butyl_density, req_butyl_prod, req_ethyl_demand, req_ethyl_capacity, req_ethyl_density, req_ethyl_prod) -> None:
        self.tank_initial = float(req_tank_initial)
        self.tank_capacity = float(req_tank_capacity)
        self.turnover = float(req_turnover)


        self.butyl_density = float(req_butyl_density)
        self.butyl_prod = float(req_butyl_prod)

        self.ethyl_density = float(req_ethyl_density)
        self.ethyl_prod = float(req_ethyl_prod)
        
        # demand & capacity in gallons, per month
        self.butyl_demand_gallons = float(req_butyl_demand) / req_butyl_density
        self.ethyl_demand_gallons = req_ethyl_demand / req_ethyl_density
        
        # production PER DAY in gallons
        butyl_prod_gal = req_butyl_prod / req_butyl_density
        ethyl_prod_gal = req_ethyl_prod / req_ethyl_density
        self.GALS_PER_DAY_LIST = [0, butyl_prod_gal, ethyl_prod_gal]

        # tank parameters
        print("initial: ", req_tank_initial)
        self.tank = Tank(req_tank_initial, 0, 0, float(req_tank_capacity), req_butyl_capacity / req_butyl_density, req_ethyl_capacity / req_ethyl_density, butyl_prod_gal, ethyl_prod_gal, req_turnover)
        # Stores the schedule 
        self.schedule = Schedule()

    def addEthyl(self, currSched: Schedule):
        self.tank.produceEutyl()
        currSched.addToSchedule(Acetate.ETHYL, self.GALS_PER_DAY_LIST[int(Acetate.ETHYL)])
    
    def addButyl(self, currSched: Schedule):
        self.tank.produceButyl()
        currSched.addToSchedule(Acetate.BUTYL, self.GALS_PER_DAY_LIST[int(Acetate.BUTYL)])

    # DECIDE WHETHER TO PRODUCE BUTYL OR ETHYL AFTER DOWNTIME.
    def decideBetweenButylAndEthyl(self, currSchedule: Schedule):
        return self.addButyl(currSchedule) if self.tank.BUTYL_PROD_GAL_PER_DAY > self.tank.ETHYL_PROD_GAL_PER_DAY else self.addEthyl(currSchedule)

    
    def handlePrevTurnoverTime(self, currSched: Schedule):
        '''
        If previously we had turnover. 
        '''
        # needs more turnover -> give it more turnover.
        if self.tank.needsMoreTurnover():
            # increment turnover and add turnover to the schedule
            self.tank.incrementTurnover()
            currSched.addToSchedule(Acetate.TURNOVER, self.GALS_PER_DAY_LIST[0])
            return
        # otherwise, turnover just finished. -> end the turnover.
        # Figure out which should be produced
        self.tank.endTurnover()
        self.addEthyl(currSched) if currSched.getLastScheduledAcetate == Acetate.BUTYL else self.addButyl(currSched)
                

    def handlePrevDowntime(self, currSched):
        '''
        If previously we had downtime, we want to see if we still need downtime or can produce something. 
        If the tank is at capacity OR both of the acetates are at capacity, then we would need downtime.
        '''
        # needs more downtime -> give it more downtime.
        if self.tank.needDowntime():
            currSched.addToSchedule(Acetate.DOWNTIME, 0)
        
        # Can only produce ethyl
        elif not self.tank.canProduceButyl():
            self.addEthyl(currSched)
        
        # can only produce butyl
        elif not self.tank.canProduceEthyl():
            self.addButyl(currSched)
        
        # otherwise, we can produce both. pick which one to produce.
        self.decideBetweenButylAndEthyl(currSchedule=currSched)
        


    def handlePrevAcetate(self, prev: Acetate, currSched: Schedule):
        '''
        prev: the previous acetate that was produced
        '''
        
        if prev == Acetate.ETHYL:
            if self.tank.canProduceEthyl():
                self.addEthyl(currSched)
            else:
                currSched.addToSchedule(Acetate.DOWNTIME, 0)
        if prev == Acetate.BUTYL:
            if self.tank.canProduceButyl():
                self.addButyl(currSched)
            else:
                currSched.addToSchedule(Acetate.DOWNTIME, 0)

        
        # can only produce butyl
        if self.tank.canProduceButyl() and prev == Acetate.BUTYL:
            self.tank.increaseButylProd()
            return Acetate.BUTYL
 
        tank_remaining = self.tank_capacity - self.tank_initial # in gallons
        # to produce butyl: need to check that month capacity is < butyl capacity, butyl_prod per day < tank_remaining
        return 1
    

    def handleDay(self, prev: Acetate, sched: Schedule):
        if (prev == Acetate.TURNOVER):
            self.handlePrevTurnoverTime(sched)
        elif (prev == Acetate.DOWNTIME):
            self.handlePrevDowntime(sched)
        else:
            self.handlePrevAcetate(prev, sched)
    
    # NAIVE METHOD: randomly guess and find the best one lol.
    def randomlyAssignMonth(self, num_days, prev: Acetate, sched: Schedule):
        '''
        Randomly assign schedule for ONE month. Assumes a month has num_days days
        prev: last acetate in previous month
        sched: the schedule object so far
        '''
        for i in range(num_days):
            self.handleDay(prev, sched=sched)
    
    def randomlyAssignSchedule(self, n) -> Schedule:
        '''
        Randomly assigns the schedule for n days
        at the end of the month, decrease the ethyl and butyl amount in the tank (subtract by the demand)
        '''
        #  Randomly select one of the other to start
        sched = Schedule()
        for i in range(n):
            self.randomlyAssignMonth(30, sched.getLastThingInSchedule(), sched)
            # Subtract the demand
            self.tank.decreaseByMonthlyDemand(self.butyl_demand_gallons, self.ethyl_demand_gallons)
        return sched