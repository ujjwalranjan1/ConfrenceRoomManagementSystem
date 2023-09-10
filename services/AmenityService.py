from entity.Amenities import Amenities
from enums.AmenityEnum import AmenityEnum
from config import amenity_repository

class AmenityService:

    def add_room_associated_with_amenity(self,room_id,amenity_type:AmenityEnum):
        amenity=amenity_repository.get_amenity(amenity_type)
        amenity.add_associated_room_id(room_id)

    def delete_room_associated_with_amenity(self,room_id,amenity_type):
        amenity=amenity_repository.get_amenity(amenity_type)
        amenity.remove_associated_room_id(room_id)

    def get_room_associated_with_amenity(self,amenity_type):
        amenity=amenity_repository.get_amenity(amenity_type)
        return amenity.get_associated_room_ids()
