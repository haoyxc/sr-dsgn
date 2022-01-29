from api.helpers.Acetate import Acetate

class Schedule:
    def __init__(self, start_acetate, num_days) -> None:
        self.start_acetate = start_acetate
        self.num_days = num_days
        self.schedule = []