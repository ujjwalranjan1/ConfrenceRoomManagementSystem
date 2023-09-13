from entity.TimeSlot import TimeSlot
class TimeSlotRepository:
    def __init__(self):
        self.timeslots=[]
        self.timeslots_hours=[]
        for i in range(24):
            self.timeslots.append(TimeSlot(i))
            self.timeslots_hours.append(i)
            
    def getTimeSlot(self,start_hour):
        return self.timeslots[start_hour]
    
    def get_all_time_slots_hours(self):
        return self.timeslots_hours
    
    def get_all_timeslot(self):
        return self.timeslots