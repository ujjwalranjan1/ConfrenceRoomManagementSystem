from entity.TimeSlot import TimeSlot
class TimeSlotRepository:
    def __init__(self):
        self.timeslots=[]
        for i in range(24):
            self.timeslots.append(TimeSlot(i))
            
    def getTimeSlot(self,start_hour):
        return self.timeslots[start_hour]