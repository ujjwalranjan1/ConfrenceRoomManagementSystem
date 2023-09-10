from entity.TimeSlot import TimeSlot
from config import timeslot_repository

class TimeSlotService:

    def add_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.add_room(room_id)

    def remove_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.remove_room(room_id)


    def book_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.book_room(room_id)
    
    def cancel_book_room(self,timeslot_hour,room_id):
        timeslot=timeslot_repository.getTimeSlot(timeslot_hour)
        timeslot.cancel_booked_room

    def get_all_timeslots_hour(self):
        return timeslot_repository.get_all_time_slots_hours()