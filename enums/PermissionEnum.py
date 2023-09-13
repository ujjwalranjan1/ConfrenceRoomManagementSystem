from enum import Enum

class Permission(Enum):
    READROOM = "Read_Room"
    WRITEROOM = "Write_Room"
    READUSER = "Read_User"
    WRITEUSER = "Write_USER"
    READORGANIZATION = "Read_Organization"
    WRITEORGANIZATION = "Write_Organization"
    READFLOOR = "Read_Floor"
    WRITEFLOOR = "Write_floor"
    WRITEBOOKING = "Write_booking"
    READBOOKING ="Read_Booking"


