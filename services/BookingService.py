from entity.Booking import Booking

class BookingService:
    def book_room(room_id,start_time,end_time,user_id):
        user_role_enum=user.get_role_enum()
        user_role=role_service.find_role_by_role_enum(user_role_enum)
        if user_role.has_permission(Permission.WRITEFLOOR):
            try:
                floor=floor_repository.find_floor_by_number(floor_number)
                rooms=floor.get_all_rooms()
                for id in rooms:
                    room_service.delete_room_by_id(id,user)
                floor_repository.delete_floor_by_number(floor_number)
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user.get_uid() ,"does not have permission to delete floor")

    