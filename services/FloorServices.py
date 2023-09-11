from entity.User import User
from config import floor_repository,role_service,room_service,user_service
from enums.PermissionEnum import Permission
from entity.Floor import Floor 

class FloorService:

    def add_floor(self,user_id,floor_num):
        if user_service.check_permission(user_id,Permission.WRITEFLOOR):
            try:
                floor_repository.create_floor(floor_num)
                print("floor successfully added")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")
    
    def delete_floor(self,user_id,floor_number):
        if user_service.check_permission(user_id,Permission.WRITEFLOOR):
            try:
                floor=floor_repository.find_floor_by_number(floor_number)
                rooms=floor.get_all_rooms()
                for id in rooms:
                    room_service.delete_room_by_id(id,user_id)
                floor_repository.delete_floor_by_number(floor_number)
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to delete floor")

    def get_all_floor(self):
        return floor_repository.get_all_floor()

    def add_room_on_floor(self,room_id,floor_number:int):
        floor=floor_repository.find_floor_by_number(floor_number)
        floor.add_room(room_id)
    
    def remove_room_on_floor(self,room_id,floor_number):
        floor=floor_repository.find_floor_by_number(floor_number)
        floor.remove_room(room_id)
