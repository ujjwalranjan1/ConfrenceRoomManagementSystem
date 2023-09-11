from entity.Booking import Booking
from collections import defaultdict

class BookingRepository:
    def __init__(self):
        # self.booking_by_user_id=defaultdict(set)
        # self.booking_by_organization_id=defaultdict(set)
        # self.booking_by_timeslots=defaultdict(set)
        # self.booking_by_room_id=defaultdict(set)
        self.booking_by_booking_id={}
        # self.booking_by_room_timeslot={}
    
    def create_booking(self,user_id,organization_id,timeslots,room_id):
        booking=Booking(room_id,timeslots,user_id,organization_id)
        # self.booking_by_user_id[user_id].add(booking)
        # self.booking_by_organization_id[organization_id].add(booking)
        # for timeslot in timeslots:
        #     self.booking_by_timeslots[timeslot].add(booking)
        #     self.booking_by_room_timeslot[tuple([room_id,timeslot])]=booking
        # self.booking_by_room_id[room_id].add(booking)
        self.booking_by_booking_id[booking.get_booking_id()]=booking

    def delete_booking(self,booking_id):
        # booking=self.booking_by_booking_id[booking_id]
        #partial deletion
        # if set(timeslots)!=booking.get_timeslots():
        #     booking.delete_time_slots(timeslots)
        #     for timeslot in timeslots:
        #         self.booking_by_timeslots[timeslot].remove(booking)
        #         self.booking_by_room_timeslot.pop([tuple([room_id,timeslot])])
        # else:
        #     self.booking_by_user_id[booking.get_user_id()].remove(booking)
        #     self.booking_by_organization_id[booking.get_organization_id()].remove(booking)
        #     for timeslot in timeslots:
        #         self.booking_by_timeslots[timeslot].remove(booking)
        #         self.booking_by_room_timeslot.pop([tuple([room_id,timeslot])])
        #     self.booking_by_room_id[room_id].remove(booking)
        self.booking_by_booking_id.pop(booking_id)
    
    def get_booking_by_booking_id(self,book_id):
        return self.booking_by_booking_id[book_id]

