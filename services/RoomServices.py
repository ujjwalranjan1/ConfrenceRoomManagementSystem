from entity.Room import Room
from beans.RoomRepositoryBean import room_repository
from beans.AmenityRepositoryBean import amenity_repository
from entity.User import User
from enums.PermissionEnum import Permission

class RoomServices:

    def create_room(self,room_name,amenity_type,floor_id):
        room_id=room_repository.create_room(
            room_name=room_name,
            amenities=amenity_type,
            floor=floor_id,
        )
        return room_id

    def get_room_by_name(self,room_name):
       return room_repository.get_room_by_name(room_name)
    
    def get_room_by_id(self,room_id):
        return room_repository.get_room_by_id(room_id)
    
    def get_all_bookings(self,room_id):
        room=self.get_room_by_name(room_id)
        if room!=None:
            return room.get_bookings()

    def delete_room_by_id(self,room_id):
        room_repository.delete_room_by_id(room_id)

    def delete_room_by_name(self,room_name):
       room_repository.delete_room_by_name(room_name)

         
#get all room 
    def get_all_room(self):
        return room_repository.get_all_room()
    
    # def get_all_available_room_for_timeslot(self,timeslot_hour):
    #     return timeslot_service.get_all_available_room_for_timeslot(timeslot_hour)
    
    # def get_all_available_room_with_timeslots_and_amenity(self,timeslot_hour,amenity_type):
    #     rooms_with_amenity=amenity_service.get_room_associated_with_amenity(amenity_type)
    #     for timeslot in timeslot_hour:
    #         rooms_with_amenity=set.intersection(rooms_with_amenity,self.get_all_available_room_for_timeslot(timeslot))
    #     return rooms_with_amenity
#changes in room functions will be addedd later

    def book_room(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        if room!=None:
            room.add_booking(booking_id)

    def cancel_booking(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        if room!=None:
            room.delete_booking(booking_id)

    def check_booking(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        if room!=None:
            room.check_booking(booking_id)

