
import uuid

class Room:
    def __init__(self,**kwargs):
        self.room_id=uuid.uuid1()
        try:
            self.amenities=kwargs["amenities"]
        except KeyError as error:
            print("Amenities is required for room")
        try:
            self.floor=kwargs["floor"]
        except KeyError as error:
            print("floor is required for room")

        try:
            self.time_slots=kwargs["time_slots"]
        except KeyError as error:
            self.time_slots=[i for i in range(24)]
            print("timestamp is required for room else taking 24 hours time slot")
        

