from entity.User import User
from config import floor_repository,role_service,room_service
from entity.Permission import Permission
from entity.Floor import Floor 

class FloorService:

    def add_floor(self,user:User,floor_num):
        #add this in user service
        user_role_enum=user.get_role_enum()
        user_role=role_service.find_role_by_role_enum(user_role_enum)
        if user_role.has_permission(Permission.WRITEFLOOR):
            try:
                floor_repository.create_floor(floor_num)
                print("floor successfully added")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user.get_uid() ,"does not have permission to add floor")
    
    def delete_floor(self,user:User,floor_number):
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

    def get_all_floor(self):
        return floor_repository.get_all_floor()

    def add_room_on_floor(self,room_id,floor_number:int):
        floor=floor_repository.find_floor_by_number(floor_number)
        floor.add_room(room_id)
    
    def remove_room_on_floor(self,room_id,floor_number):
        floor=floor_repository.find_floor_by_number(floor_number)
        floor.remove_room(room_id)
