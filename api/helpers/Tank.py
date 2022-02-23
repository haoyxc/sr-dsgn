from typing import Final
from xmlrpc.client import boolean

from api.helpers.Acetate import Acetate
class Tank:
    def __init__(self, curr_tank_capacity, monthly_butyl_prod, monthly_ethyl_prod, tank_capacity, butyl_capacity, ethyl_capacity, butyl_prod_gal, ethyl_prod_gal, turnover) -> None:
        # current gallons in the tank -- curr_tank_capacity is the sum of the other two
        self.curr_tank_capacity = curr_tank_capacity
        self.monthly_butyl_prod = monthly_butyl_prod
        self.monthly_ethyl_prod = monthly_ethyl_prod
        
        # DOES NOT CHANGE
        self.TANK_CAPACITY: Final = tank_capacity
        self.BUTYL_CAPACITY: Final = butyl_capacity
        self.ETHYL_CAPACITY: Final = ethyl_capacity

        self.BUTYL_PROD_GAL_PER_DAY: Final = butyl_prod_gal
        self.ETHYL_PROD_GAL_PER_DAY: Final = ethyl_prod_gal

        # if this is -1, we are NOT in a turnover period. turnover will start at 1. 
        self.turnover_streak = -1
        self.required_turnover = turnover
        self.last_acetate : Acetate = 0
    
    def getTurnoverStreak(self):
        return self.turnover_streak

    def getTotalTankAmont(self):
        return self.monthly_butyl_prod + self.monthly_ethyl_prod

    def isTankFull(self):
        print("curr capacity: ", self.curr_tank_capacity)
        print("Tank capacity: ", self.TANK_CAPACITY)
        print("is tank full: ", self.curr_tank_capacity < self.TANK_CAPACITY)
        return self.curr_tank_capacity >= self.TANK_CAPACITY
        # return 0

    def canProduceButyl(self):
        return not self.isTankFull() and self.monthly_butyl_prod + self.BUTYL_PROD_GAL_PER_DAY <= self.BUTYL_CAPACITY

    def canProduceEthyl(self):
        return not self.isTankFull() and self.monthly_ethyl_prod + self.ETHYL_PROD_GAL_PER_DAY <= self.ETHYL_CAPACITY

    def canProduceEither(self):
        print("can produce butyl: ", self.canProduceButyl())
        print("can produce ethyl: ", self.canProduceEthyl())
        return self.canProduceButyl() or self.canProduceEthyl()

    def needDowntime(self):
        '''
        we HAVE to schedule downtime.
        '''
        return self.isTankFull() or not self.canProduceEither()

    # Production functions
    def produceButyl(self):
        '''
        add the daily butyl production to monthly butyl total and tank capacity
        '''
        self.monthly_butyl_prod = self.monthly_butyl_prod + self.BUTYL_PROD_GAL_PER_DAY
        self.curr_tank_capacity = self.curr_tank_capacity + self.monthly_butyl_prod
    def produceEutyl(self):
        '''
        add the daily ethyl production to the month ethyl total and tank capacity
        '''
        self.monthly_ethyl_prod = self.monthly_ethyl_prod + self.ETHYL_PROD_GAL_PER_DAY
        self.curr_tank_capacity = self.curr_tank_capacity + self.monthly_ethyl_prod
    
    def reset(self):
        self.monthly_butyl_prod = 0
        self.monthly_ethyl_prod = 0
        self.curr_tank_capacity = 0

    def decreaseByMonthlyDemand(self, butylDemand, ethylDemand):

        self.monthly_butyl_prod = self.monthly_butyl_prod - butylDemand
        self.monthly_ethyl_prod = self.monthly_ethyl_prod - ethylDemand
        self.curr_tank_capacity = self.monthly_butyl_prod + self.monthly_ethyl_prod
    
    # --------------
    # Turnover related helper functions
    #----------------
    def needsMoreTurnover(self) -> boolean:
        return self.turnover_streak > -1 and self.turnover_streak < self.required_turnover

    def incrementTurnover(self):
        self.turnover_streak = self.turnover_streak + 1
    
    def endTurnover(self):
        self.turnover_streak = -1
    
    def startTurnover(self):
        self.turnover_streak = 1
    
    def isInTurnover(self) -> boolean:
        return self.turnover_streak != -1

    # def increaseEthylProd(self):
    #     self.monthly_ethyl_prod = self.monthly_ethyl_prod + self.ETHYL_PROD_GAL_PER_DAY
    
    # def increaseButylProd(self):
    #     self.monthly_butyl_prod = self.monthly_butyl_prod + self.BUTYL_PROD_GAL_PER_DAY