from typing import Final
class Tank:
    def __init__(self, curr_tank_capacity, monthly_butyl_prod, monthly_ethyl_prod, tank_capacity, butyl_capacity, ethyl_capacity, butyl_prod_gal, ethyl_prod_gal, turnover) -> None:
        self.curr_tank_capacity = curr_tank_capacity
        self.monthly_butyl_prod = monthly_butyl_prod
        self.monthly_ethyl_prod = monthly_ethyl_prod
        # DOES NOT CHANGE
        self.TANK_CAPACITY: Final = tank_capacity
        self.BUTYL_CAPACITY: Final = butyl_capacity
        self.ETHYL_CAPACITY: Final = ethyl_capacity

        self.BUTYL_PROD_GAL_PER_DAY: Final = butyl_prod_gal
        self.ETHYL_PROD_GAL_PER_DAY: Final = ethyl_prod_gal

        self.turnover_streak = -1
        self.required_turnover = turnover
    def isTankFull(self):
        return self.curr_tank_capacity < self.TANK_CAPACITY
        # return 0

    def canProduceButyl(self):
        # return self.isTankFull(self) and self.monthly_butyl_prod <= self.BUTYL_CAPACITY
        return self.isTankFull(self) and self.monthly_butyl_prod + self.BUTYL_PROD_GAL_PER_DAY <= self.BUTYL_CAPACITY

    def canProduceEthyl(self):
        # return self.isTankFull(self) and self.monthly_ethyl_prod <= self.ETHYL_CAPACITY
        return self.isTankFull(self) and self.monthly_ethyl_prod + self.ETHYL_PROD_GAL_PER_DAY <= self.ETHYL_CAPACITY

    def canProduceEither(self):
        return self.canProduceButyl() or self.canProduceEthyl()

    def needsMoreTurnover(self):
        return self.turnover_streak > -1 and self.turnover_streak < self.required_turnover

    def incrementTurnover(self):
        self.turnover_streak = self.turnover_streak + 1

    def increaseEthylProd(self):
        self.monthly_ethyl_prod = self.monthly_ethyl_prod + self.ETHYL_PROD_GAL_PER_DAY
    
    def increaseButylProd(self):
        self.monthly_butyl_prod = self.monthly_butyl_prod + self.BUTYL_PROD_GAL_PER_DAY