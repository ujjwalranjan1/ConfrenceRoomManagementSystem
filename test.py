from beans.OrganizationControllerBean import organization_controller
from beans.OrganizationRepositoryBean import organization_repository

from beans.UserRepositoryBean import user_repository
from beans.UserControllerBean import user_controller

from beans.FloorControllerBean import floor_controller
from beans.FloorRepositorybean import floor_repository

from  beans.RoomControllerBean import room_controller
from beans.RoomRepositoryBean import room_repository

from beans.BookingControllerBean import booking_controller
from beans.BookingRepositoryBean import booking_repository

from beans.TimeSlotRepositoryBean import timeslot_repository
from beans.RoleRepositoryBean import role_repository
from beans.AmenityRepositoryBean import amenity_repository

from enums.RoleEnum import RoleEnum
from enums.AmenityEnum import AmenityEnum


from beans.UserServiceBean import user_service

organization_controller.create_organization(
    "samsung"
)

organization_controller.create_organization(
    "nokia"
)

user_controller.add_user(
    first_name="ujjwal",
    last_name="ranjan",
    email="ujjwal@gmail.com",
    organization_name="samsung",
    role_type=RoleEnum.Admin
)

user_controller.add_user(
    first_name="raj",
    last_name="kumar",
    email="kumar@gmail.com",
    organization_name="samsung",
    role_type=RoleEnum.User
)



floor_controller.add_floor(1)
floor_controller.add_floor(2)

room_controller.create_room(
    "101",
    AmenityEnum.Small,
    1
)
room_controller.create_room(
    "102",
    AmenityEnum.Large,
    1
)

room_controller.create_room(
    "201",
    AmenityEnum.Small,
    2
)
room_controller.create_room(
    "202",
    AmenityEnum.Large,
    2
)


booking_controller.book_room(
    "101",
    2,
    5,
    "ujjwal@gmail.com"
)
# user=user_service.get_user_by_email("ujjwal@gmail.com")
# print(user)
bookings=booking_controller.get_bookings_by_organization("samsung")
if bookings!=None:
    for booking in bookings:
        print(booking)

# rooms=room_controller.get_all_available_room_for_timeslot(2,5)
# # for room in rooms:
# #     print(room)
# rooms=room_controller.get_all_available_room_with_timeslots_and_amenity(2,5,AmenityEnum.Small)
# for room in rooms:
#     print(room)
# user_controller.delete_user(
#      "ujjwal@gmail.com"
# )

# for org in organization_repository.get_all_organization():
#     print(org)
#     print("\n\n")

# print(role_repository.get_role(RoleEnum.Admin))
# print("\n\n")
# print(role_repository.get_role(RoleEnum.User))
# print("\n\n")

# for user in user_repository.get_all_users():
#     print(user)
#     print("\n\n")

# for floor in floor_repository.get_all_floor():
#     print(floor)
#     print("\n\n")

# for room in room_repository.get_all_room():
#     print(room)
#     print("\n\n")

# timeslots=timeslot_repository.get_all_timeslot()
# for timeslot_hour in range(2,5):
#     print(timeslots[timeslot_hour])
#     print("\n\n")