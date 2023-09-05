
class Floor:
    def __init__(self,number,name):
        self.floor_number=number
        self.floor_name=name
        self.rooms=set()
    
    def get_floor_number(self):
        return self.floor_number
    def get_floor_name(self):
        return self.floor_name
    
    def set_floor_number(self,number):
        self.floor_number=number
    def set_floor_name(self,name):
        self.floor_name=name

    def add_room(self,room_id):
        self.rooms.add(room_id)
    
    def remove_room(self,room_id):
        self.rooms.remove(room_id)
