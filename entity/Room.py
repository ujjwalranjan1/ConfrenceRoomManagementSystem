
import uuid
from enums.AmenityEnum import AmenityEnum

class Room:
    def __init__(self,**kwargs):

        self.room_id=uuid.uuid1()
        self.bookings=set()
        try:
            self.room_name=kwargs["room_name"]
        except KeyError as error:
            print("Room Name is required for room")

        try:
            self.amenities=kwargs["amenities"]
        except KeyError as error:
            print("Amenities is required for room")

        try:
            self.floor=kwargs["floor"]
        except KeyError as error:
            print("floor is required for room")

        if kwargs["time_slots"]!=None:
            self.available_time_slots=kwargs["time_slots"]
        else:
            self.available_time_slots=[i for i in range(24)]
        
    def get_id(self):
        return self.room_id
    def get_name(self):
        return self.room_name
    def get_amenity_type(self):
        return self.amenities
    def set_amenity_type(self,amenity_type):
        self.amenities=amenity_type
    def get_floor(self):
        return self.floor
    def set_floor(self,floor_number):
        self.floor=floor_number

    def add_booking(self,booking_id):
        self.bookings.add(booking_id)

    def get_bookings(self):
        return self.bookings
    
    def delete_booking(self,booking_id):
        self.bookings.discard(booking_id)
    
    def check_booking(self,booking_id):
        return booking_id in self.bookings


