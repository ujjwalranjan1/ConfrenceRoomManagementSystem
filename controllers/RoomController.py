from beans.RoomServiceBean import room_service
from beans.AmenityServiceBean import amenity_service
from beans.TimeSlotServiceBean import timeslot_service
from beans.FloorServiceBean import floor_service
from beans.BookingControllerBean import booking_controller
from beans.UserServiceBean import user_service
from enums.PermissionEnum import Permission
class RoomController:

    def create_room(self,room_name,amenity_type,floor_number,user_email):
        if user_service.check_permission(user_email,Permission.WRITEROOM):
            room_id=room_service.create_room(room_name,amenity_type,floor_number)
            amenity_service.add_room_associated_with_amenity(room_id,amenity_type)
            timeslot_service.add_room_all_time_slot(room_id)
            floor_service.add_room_on_floor(room_id,floor_number)
        else:
            print("no permission for user")

    def delete_room_by_name(self,room_name,user_email):
        if user_service.check_permission(user_email,Permission.WRITEROOM):
            room=room_service.get_room_by_name(room_name)
            if room!=None:
                self.delete_room_by_id(room.get_id(),user_email)
        else:
            print("no permission for user")
        
    def delete_room_by_id(self,room_id,user_email):
        if user_service.check_permission(user_email,Permission.WRITEROOM):
            room=room_service.get_room_by_id(room_id)
            if room!=None:
                amenity_service.delete_room_associated_with_amenity(room_id,room.get_amenity_type())
                timeslot_service.remove_room_all_time_slot(room_id)
                bookings=room.get_bookings()
                for id in bookings:
                    booking_controller.delete_booking(id,user_email)
                floor_service.remove_room_on_floor(room_id,room.get_floor())
        else:
            print("no permission for user")

    def get_room(self,room_name,user_email):
        if user_service.check_permission(user_email,Permission.READROOM):
            return room_service.get_room_by_name(room_name)
        else:
            print("no permission for user")
    
    def  get_all_available_room_for_timeslot(self,start_hour,end_hour,user_email):
        if user_service.check_permission(user_email,Permission.READROOM):
            timeslot_hour=[i for i in  range(start_hour,end_hour)]
            rooms_id= room_service.get_all_available_room_for_timeslot(timeslot_hour)
            rooms_list=[]
            for id in rooms_id:
                room=room_service.get_room_by_id(id)
                rooms_list.append(room)
            return rooms_list
        else:
            print("no permission for user")
        

    def get_all_available_room_with_timeslots_and_amenity(self,start_hour,end_hour,amenity_type,user_email):
        if user_service.check_permission(user_email,Permission.READROOM):
            timeslot_hour=[i for i in  range(start_hour,end_hour)]
            rooms_id= room_service.get_all_available_room_with_timeslots_and_amenity(timeslot_hour,amenity_type)
            rooms_list=[]
            for id in rooms_id:
                room=room_service.get_room_by_id(id)
                rooms_list.append(room)
            return rooms_list
        else:
            print("no permission for user")

