class Amenities:
    def __init__(self,**kwargs):
        self.rooms_id=set()
        try:
            self.capacity=kwargs["capacity"]
        except KeyError as error:
            print("capacity is manadatory")
    
        if kwargs["fan_count"] !=None:
            self.fan_count = kwargs["fan_count"]
        if kwargs["camera_count"] !=None:
            self.camera_count = kwargs["camera_count"]
        if kwargs["screen_count"] !=None:
            self.screen_count = kwargs["screen_count"]
        if kwargs["projector_count"] !=None:
            self.projector_count = kwargs["projector_count"]
        if kwargs["computer_count"] !=None:
            self.computer_count = kwargs["computer_count"]
        if kwargs["phone_count"] !=None:
            self.phone_count = kwargs["phone_count"]

    def get_fan_count(self):
        return self.fan_count
    def set_fan_count(self,fan_count):
        self.fan_count=fan_count
    def get_camera_count(self):
        return self.camera_count
    def set_camera_count(self,camera_count):
        self.fan_count=camera_count
    def get_screen_count(self):
        return self.screen_count
    def set_screen_count(self,screen_count):
        self.screen_count=screen_count
    def get_projector_count(self):
        return self.projector_count
    def set_projector_count(self,projector_count):
        self.projector_count=projector_count
    def get_computer_count(self):
        return self.computer_count
    def set_computer_count(self,computer_count):
        self.computer_count=computer_count
    def get_phone_count(self):
        return self.phone_count
    def set_phone_count(self,phone_count):
        self.phone_count=phone_count
        
    def add_room_id(self,room_id):
        self.rooms_id.add(room_id)
    def remove_room_id(self,room_id):
        self.rooms_id.remove(room_id)
    def get_room_ids(self):
        return list(self.rooms_id)