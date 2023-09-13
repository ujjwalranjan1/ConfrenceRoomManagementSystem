from beans.RoomServiceBean import room_service
from beans.AmenityServiceBean import amenity_service
from beans.TimeSlotServiceBean import timeslot_service
from beans.FloorServiceBean import floor_service
from beans.BookingControllerBean import booking_controller
class RoomController:

    def create_room(self,room_name,amenity_type,floor_number):
        room_id=room_service.create_room(room_name,amenity_type,floor_number)
        amenity_service.add_room_associated_with_amenity(room_id,amenity_type)
        timeslot_service.add_room_all_time_slot(room_id)
        floor_service.add_room_on_floor(room_id,floor_number)

    def delete_room_by_name(self,room_name):
        room=room_service.get_room_by_name(room_name)
        if room!=None:
            self.delete_room_by_id(room.get_id())
        
    def delete_room_by_id(self,room_id):
        room=room_service.get_room_by_id(room_id)
        if room!=None:
            amenity_service.delete_room_associated_with_amenity(room_id,room.get_amenity_type())
            timeslot_service.remove_room_all_time_slot(room_id)
            bookings=room.get_bookings()
            for id in bookings:
                 booking_controller.delete_booking(id)
            floor_service.remove_room_on_floor(room_id,room.get_floor())

    def get_room(self,room_name):
        return room_service.get_room_by_name(room_name)

