from repository.AmenitiesRepository import AmenitiesRepository
from repository.RoleRepository import RoleRepository
from repository.BookingRepository import BookingRepository
from repository.FloorRepository import FloorRepository
from repository.OrganizationRepository import OrganizationRepository
from repository.RoomRepository import RoomRepository
from repository.TimeSlotRepository import TimeSlotRepository
from repository.UserRepository import UserRepository
from enums.RoleEnum import RoleEnum
from services.RoomServices import RoomServices
from services.AmenityService import AmenityService
from services.FloorServices import FloorService
from services.RoleService import RoleService
from services.TimeSlotService import TimeSlotService

amenity_repository=AmenitiesRepository()
role_repository=RoleRepository()
booking_repository=BookingRepository()
floor_repository=FloorRepository()
organization_repository=OrganizationRepository()
room_repository=RoomRepository()
timeslot_repository=TimeSlotRepository()
user_repository=UserRepository()

room_service=RoomServices()
amenity_service=AmenityService()
floor_service=FloorService()
role_service=RoleService()
timeslot_service=TimeSlotService()


super_user=user_repository.create_user(
    first_name="super",
    last_name="user",
    email="contollermanagement@superuser.com",
    organization_id=0,
    role_enum=RoleEnum.Admin
    
)