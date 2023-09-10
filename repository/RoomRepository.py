from entity.Room import Room

class RoomRepository:
    def __init__(self):
        self.room_by_id={}
        self.room_by_name={}

    def create_room(self,**kwargs):
        room=Room(**kwargs)
        self.room_by_name[room.get_id()]=room
        self.room_by_id[room.get_name()]=room
        return room.get_id()

    def delete_room_by_id(self,room_id):
        room=self.room_by_id[room_id]
        self.room_by_name.pop(room.get_name())
        self.room_by_id.pop(room_id)
    
    def delete_room_by_name(self,room_name):
        room=self.room_by_name[room_name]
        self.room_by_id.pop(room.get_id())
        self.room_by_name.pop(room_name)

    def get_room_by_id(self,room_id):
        return self.room_by_id[room_id]
    
    def get_room_by_name(self,room_name):
        return self.room_by_name[room_name]
    
    def get_all_room(self):
        return self.room_by_id.values()