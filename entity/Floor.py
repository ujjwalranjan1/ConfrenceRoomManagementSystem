
class Floor:
    def __init__(self,number):
        self.floor_number=number
        self.rooms=set()
    
    # def get_floor_number(self):
    #     return self.floor_number
    
    # def set_floor_number(self,number):
    #     self.floor_number=number

    def add_room(self,room_id):
        self.rooms.add(room_id)
    
    def remove_room(self,room_id):
        self.rooms.remove(room_id)
