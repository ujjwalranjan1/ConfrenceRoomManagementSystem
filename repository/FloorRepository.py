from entity.Floor import Floor

class FloorRepository:
    def __init__(self):
        self.floor_by_floor_number={}
        self.floor_by_floor_name={}

    def create_floor(self,number,name):
        floor=Floor(number,name)
        self.floor_by_floor_number[number]=floor
        self.floor_by_floor_name[name]=floor

    def find_floor_by_number(self,number):
        return self.floor_by_floor_number[number]
    
    def find_floor_by_name(self,name):
        return self.floor_by_floor_name[name]
    
    def delete_floor_by_number(self,number):
        floor=self.find_floor_by_number(number)
        self.floor_by_floor_name.pop(floor.get_floor_name())
        self.floor_by_floor_number.pop(number)

    def delete_floor_by_name(self,name):
        floor=self.find_floor_by_name(name)
        self.floor_by_floor_name.pop(name)
        self.floor_by_floor_number.pop(floor.get_floor_number)

        
