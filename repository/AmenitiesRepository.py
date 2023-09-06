from enums.AmenityEnum import AmenityEnum
from entity.Amenities import Amenities

class AmenitiesRepository:

    def __init__(self):
        self.amenities={}
        self.amenities[AmenityEnum.Small]=Amenities(
            capacity=25,
            fan_count=4,
            camera_count=2,
            screen_count=1,
            projector_count =1,
            computer_count =2,
            phone_count =2
        )
        self.amenities[AmenityEnum.Medium]=Amenities(
            capacity=50,
            fan_count=8,
            camera_count=5,
            screen_count=3,
            projector_count =3,
            computer_count =5,
            phone_count =4
        )
        self.amenities[AmenityEnum.Small]=Amenities(
            capacity=100,
            fan_count=15,
            camera_count=10,
            screen_count=10,
            projector_count =10,
            computer_count =15,
            phone_count = 6
        )
    def get_amenity(self,amenity_enum):
        return self.amenities[amenity_enum]
