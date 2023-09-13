from entity.User import User
from enums.PermissionEnum import Permission
from entity.Floor import Floor 
from beans.FloorRepositorybean import floor_repository

class FloorService:
    
    def add_floor(self,floor_num):
        floor_repository.create_floor(floor_num)
    
    def delete_floor(self,floor_number):
        floor_repository.delete_floor_by_number(floor_number)
            
    def get_all_floor(self):
        return floor_repository.get_all_floor()

    def add_room_on_floor(self,room_id,floor_id):
        floor=floor_repository.find_floor_by_number(floor_id)
        if floor!=None:
            floor.add_room(room_id)
    
    def remove_room_on_floor(self,room_id,floor_id):
        floor=floor_repository.find_floor_by_number(floor_id)
        if floor!=None:
            floor.remove_room(room_id)

    def get_floor_by_id(self,floor_id):
        return floor_repository.find_floor_by_number(floor_id)