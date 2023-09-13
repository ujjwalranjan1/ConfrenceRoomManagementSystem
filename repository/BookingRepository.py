from entity.Booking import Booking
from collections import defaultdict

class BookingRepository:
    
    def __init__(self):
        self.booking_by_booking_id={}
    
    def create_booking(self,user_id,organization_id,timeslots,room_id):
        booking=Booking(room_id,timeslots,user_id,organization_id)
        self.booking_by_booking_id[booking.get_booking_id()]=booking
        return booking.get_booking_id()
    
    def delete_booking(self,booking_id):
        self.booking_by_booking_id.pop(booking_id)
    def get_booking_by_booking_id(self,book_id):
        return self.booking_by_booking_id[book_id]

