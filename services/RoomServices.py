from entity.Room import Room
from config import room_repository,amenity_service,floor_service,timeslot_service,user_service
from entity.User import User
from entity.Permission import Permission

class RoomServices:

    def add_room(self,user_id,room_name,amenity_type,floor_id):
        if user_service.check_permission(user_id,Permission.WRITEROOM):
            try:
                room_id=room_repository.create_room(
                    room_name=room_name,
                    amenitites=amenity_type,
                    floor=floor_id,
                )
                amenity_service.add_room_associated_with_amenity(room_id,amenity_type)
                floor_service.add_room_on_floor(room_id,floor_id)
                timeslots_id=timeslot_service.get_all_timeslots_hour()
                for timeslot in timeslots_id:
                    timeslot_service.add_room(timeslot,room_id)

                print("Room successfully added")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")



    def delete_room_by_id(self,room_id,user_id):
        if user_service.check_permission(user_id,Permission.WRITEROOM):
            try:
                room=room_repository.get_room_by_id(room_id)
                bookings=room.get_bookings()
                #delete all bookings associated with room
                amenity_service.delete_room_associated_with_amenity(room_id,room.get_amenity_type())
                floor_service.remove_room_on_floor(room_id,room.get_floor())
                timeslots_id=timeslot_service.get_all_timeslots_hour()
                for timeslot in timeslots_id:
                    timeslot_service.cancel_book_room(timeslot,room_id)
                room_repository.delete_room_by_id(room_id)

                print("Room successfully removed")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")

    def delete_room_by_name(self,room_name,user_id):
        if user_service.check_permission(user_id,Permission.WRITEROOM):
            try:
                room=room_repository.get_room_by_name(room_name)
                room_id=room.get_id()
                bookings=room.get_bookings()
                #delete all bookings associated with room
                amenity_service.delete_room_associated_with_amenity(room_id,room.get_amenity_type())
                floor_service.remove_room_on_floor(room_id,room.get_floor())
                timeslots_id=timeslot_service.get_all_timeslots_hour()
                for timeslot in timeslots_id:
                    timeslot_service.cancel_book_room(timeslot,room_id)
                room_repository.delete_room_by_name(room_id)

                print("Room successfully removed")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")

#get all room 
    def get_all_room(self):
        return room_repository.get_all_room()
    
    def get_all_available_room_for_timeslot(self,timeslot_hour):
        return timeslot_service.get_all_available_room_for_timeslot(timeslot_hour)
    
    def get_all_available_room_with_timeslot_and_amenity(self,timeslot_hour,amenity_type):
        rooms_with_amenity=amenity_service.get_room_associated_with_amenity(amenity_type)
        available_rooms_for_timeslot=self.get_all_available_room_for_timeslot(timeslot_hour)
        return set.intersection(rooms_with_amenity,available_rooms_for_timeslot)
#changes in room functions will be addedd later

    def book_room(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        room.add_booking(booking_id)

    def cancel_booking(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        room.delete_booking(booking_id)

    def check_booking(self,room_id,booking_id):
        room=room_repository.get_room_by_id(room_id)
        room.check_booking(booking_id)

