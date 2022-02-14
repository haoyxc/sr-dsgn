from typing import List
from api.helpers.Acetate import Acetate

class Schedule:
    def __init__(self) -> None:
        self.schedule = []

        self.total_production = 0
        self.last_acetate = None
    
    def addToSchedule(self, toAdd : Acetate, production):
        self.schedule.append(toAdd)
        self.total_production = self.total_production + production
        # Track the last acetate that is not downtime or turnover
        if (toAdd != Acetate.DOWNTIME and toAdd != Acetate.TURNOVER):
            self.last_acetate = toAdd
        
    def getSchedule(self) -> List:
        return self.schedule
    