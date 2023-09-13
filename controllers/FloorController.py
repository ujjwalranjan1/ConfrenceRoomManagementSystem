from entity.Floor import Floor 
from entity.Room import Room
from beans.FloorServiceBean import floor_service
from beans.RoomServiceBean import room_service
from beans.AmenityServiceBean import amenity_service
from beans.TimeSlotServiceBean import timeslot_service
from beans.BookingControllerBean import booking_controller

class FloorController:
    def add_floor(self,floor_number):
        floor_service.add_floor(floor_number)

    def delete_floor(self,floor_number):
        floor=floor_service.get_floor_by_id(floor_number)
        if floor!=None:
            rooms=floor.get_all_rooms()
            for room_id in rooms:
                room=room_service.get_room_by_id(room_id)
                if room!=None:
                    amenity_service.delete_room_associated_with_amenity(room_id,room.get_amenity_type())
                    timeslot_service.remove_room_all_time_slot(room_id)
                    bookings=room.get_bookings()
                    for id in bookings:
                        booking_controller.delete_booking(id)
                        room_service.delete_room_by_id(room_id)
            floor_service.delete_floor(floor_number)