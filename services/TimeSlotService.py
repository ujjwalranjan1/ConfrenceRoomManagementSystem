from entity.TimeSlot import TimeSlot
from beans.TimeSlotRepositoryBean import timeslot_repository

class TimeSlotService:

    def add_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.add_room(room_id)

    def remove_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.remove_room(room_id)

    def add_room_all_time_slot(self,room_id):
        timeslots=timeslot_repository.get_all_timeslot()
        for timeslot in timeslots:
            timeslot.add_room(room_id)
    
    def remove_room_all_time_slot(self,room_id):
        timeslots=timeslot_repository.get_all_timeslot()
        for timeslot in timeslots:
            timeslot.remove_room(room_id)




    def book_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.book_room(room_id)
    
    def cancel_book_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.cancel_booked_room(room_id)
    
    def get_all_room_for_timeslot(self,timeslot_hour):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        return timeslot.get_all_room(timeslot_hour)
    
    def get_all_booked_room_for_time_slot(self,timeslot_hour):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        return timeslot.get_all_booked_room(timeslot_hour)
    
    def get_all_available_room_for_timeslot(self,timeslot_hour):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        return timeslot.get_all_available_room()
      

    def get_all_timeslots_hour(self):
        return timeslot_repository.get_all_time_slots_hours()