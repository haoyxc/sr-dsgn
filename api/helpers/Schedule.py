from typing import List
from api.helpers.Acetate import Acetate

class Schedule:
    def __init__(self) -> None:
        self.schedule = []

        # total production over ALL of the months. This value is never decreased to 0
        self.total_production = 0
        self.last_acetate = Acetate.DOWNTIME
    
    def addToSchedule(self, toAdd : Acetate, production):
        print("PRODUCTION: ", production)
        self.schedule.append(toAdd)
        self.total_production = self.total_production + production
        # Track the last acetate that is not downtime or turnover
        if (toAdd != Acetate.DOWNTIME and toAdd != Acetate.TURNOVER):
            self.last_acetate = toAdd
        
    def getSchedule(self) -> List:
        return self.schedule

    def getLastScheduledAcetate(self) -> Acetate:
        return self.last_acetate

    def getLastThingInSchedule(self) -> Acetate:
        return Acetate.DOWNTIME if len(self.schedule) == 0 else self.schedule[-1]
    def getTotalProduction(self) -> float:
        return self.total_production

    