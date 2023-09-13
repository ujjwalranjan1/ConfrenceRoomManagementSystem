from entity.Floor import Floor

class FloorRepository:
    def __init__(self):
        self.floor_by_floor_number={}

    def create_floor(self,number):
        if self.floor_by_floor_number.get(number)!=None:
            raise KeyError("floor number already exist")
        floor=Floor(number)
        self.floor_by_floor_number[number]=floor

    def find_floor_by_number(self,number):
        try:
            return self.floor_by_floor_number[number]
        except:
            print("floor_does not exist")
    
    
    def delete_floor_by_number(self,number):
        #check key as cerate_floor (will done later)
        floor=self.find_floor_by_number(number)
        self.floor_by_floor_number.pop(number)


    def get_all_floor(self):
        return self.floor_by_floor_number.values()
