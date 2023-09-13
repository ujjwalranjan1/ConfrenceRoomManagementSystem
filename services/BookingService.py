from entity.Booking import Booking
from beans.BookingRepositoryBean import booking_repository
from enums.PermissionEnum import Permission
from entity.User import User

class BookingService:

    def book_room(self,room_id,timeslots_hour,user_id,org_id):
        # print(timeslots_hour)
        booking_id=booking_repository.create_booking(user_id,org_id,timeslots_hour,room_id)
        return booking_id
    
    def get_booking_by_id(self,booking_id):
         booking=booking_repository.get_booking_by_booking_id(booking_id)
         return booking


    def delete_booking(self,booking_id):
       booking_repository.delete_booking(booking_id)




    