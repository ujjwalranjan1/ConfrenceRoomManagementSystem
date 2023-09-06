from entity.Booking import Booking
from collections import defaultdict

class BookingRepository:
    def __init__(self):
        self.booking_by_user_id=defaultdict(set)
        self.booking_by_organization_id=defaultdict(set)
        self.booking_by_timeslots=defaultdict(set)
        self.booking_by_room_id=defaultdict(set)
        self.booking_by_booking_id={}
    
    def create_booking(self,user_id,organization_id,timeslots,room_id):
        booking=Booking(room_id,timeslots,user_id,organization_id)
        self.booking_by_user_id[user_id].add(booking)
        self.booking_by_organization_id[organization_id].add(booking)
        for timeslot in timeslots:
            self.booking_by_timeslots[timeslot].add(booking)
        self.booking_by_room_id[room_id].add(booking)
        self.booking_by_booking_id[booking.get_booking_id()]=booking
