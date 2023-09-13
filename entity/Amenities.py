class Amenities:
    def __init__(self,**kwargs):
        self.rooms_id=set()
        try:
            self.capacity=kwargs["capacity"]
        except KeyError as error:
            print("capacity is manadatory")
    
        if "fan_count" in kwargs:
            self.fan_count = kwargs["fan_count"]
        else:
            self.fan_count=0

        if "camera_count" in kwargs:
            self.camera_count = kwargs["camera_count"]
        else:
            self.camera_count=0

        if "screen_count" in kwargs:
            self.screen_count = kwargs["screen_count"]
        else:
            self.screen_count=0
        if "projector_count" in kwargs:
            self.projector_count = kwargs["projector_count"]
        else:
            self.projector_count=0
        if "computer_count" in kwargs:
            self.computer_count = kwargs["computer_count"]
        else:
            self.computer_count=0
        if "phone_count" in kwargs:
            self.phone_count = kwargs["phone_count"]
        else :
            self.phone_count=0
    def get_capacity(self):
        return self.capacity
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

    def add_associated_room_id(self,room_id):
        self.rooms_id.add(room_id)
    def remove_associated_room_id(self,room_id):
        self.rooms_id.remove(room_id)
    def get_associated_room_ids(self):
        return self.rooms_id
    
    def __str__(self):
        return str(self.__dict__)