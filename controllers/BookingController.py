from beans.BookingServiceBean import booking_service
from beans.UserServiceBean import user_service
from beans.RoomServiceBean import room_service
from beans.OrganizationServiceBean import organization_service
from beans.TimeSlotServiceBean import timeslot_service

class BookingController:
    def book_room(self,room_name,start_time,end_time,user_email):

        user=user_service.get_user_by_email(user_email)
        if user!=None:
            user_id=user.get_uid()
            org_id=user.get_organization_id()
            if organization_service.can_book_room(org_id,end_time-start_time):
                timeslots_hour=[i for i in range(start_time,end_time)]
                room=room_service.get_room_by_name(room_name)
                if room!=None:
                    room_id=room.get_id()
                    booking_id=booking_service.book_room(room_id,timeslots_hour,user_id,org_id)
                    user_service.book_room(user_id,booking_id)
                    organization_service.book_room(org_id,booking_id,end_time-start_time)
                    room_service.book_room(room_id,booking_id)
                    for hour in timeslots_hour:
                        timeslot_service.book_room(hour,room_id)

    def delete_booking(self,booking_id):
        booking=booking_service.get_booking_by_id(booking_id)
        timeslots_hour=booking.get_timeslots()
        user_service.cancel_booking(booking.get_user_id(),booking_id)
        organization_service.cancel_booking(booking.get_organization_id(),booking_id,len(timeslots_hour))
        room_service.cancel_booking(booking.get_room_id(),booking_id)
        for hour in timeslots_hour:
            timeslot_service.cancel_book_room(hour,booking.get_room_id())

