from entity.Room import Room
from config import room_repository,role_service,amenity_service,floor_service,timeslot_service
from entity.User import User
from entity.Permission import Permission

class RoomServices:

    def add_room(self,user:User,room_name,amenity_type,floor_id):
        user_role_enum=user.get_role_enum()
        user_role=role_service.find_role_by_role_enum(user_role_enum)
        if user_role.has_permission(Permission.WRITEFLOOR):
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
            print("user with user_id: ",user.get_uid() ,"does not have permission to add floor")



    def delete_room_by_id(self,room_id,user):
        user_role_enum=user.get_role_enum()
        user_role=role_service.find_role_by_role_enum(user_role_enum)
        if user_role.has_permission(Permission.WRITEFLOOR):
            try:
                room=room_repository.get_room_by_id(room_id)
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
            print("user with user_id: ",user.get_uid() ,"does not have permission to add floor")

    def delete_room_by_name(self,room_name,user):
        user_role_enum=user.get_role_enum()
        user_role=role_service.find_role_by_role_enum(user_role_enum)
        if user_role.has_permission(Permission.WRITEFLOOR):
            try:
                room=room_repository.get_room_by_name(room_name)
                room_id=room.get_id()
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
            print("user with user_id: ",user.get_uid() ,"does not have permission to add floor")

#get all room 
    def get_all_room(self):
        return room_repository.get_all_room()
#changes in room functions will be addedd later