import uuid
class Booking:
    def __init__(self,room_id,timeslots_id,user_id,organization_id):
        self.booking_id=uuid.uuid1()
        self.room_id=room_id
        self.timeslots=timeslots_id
        self.user_id=user_id
        self.organization_id=organization_id

    def get_booking_id(self):
        return self.booking_id
    def get_room_id(self):
        return self.room_id
    def get_timeslots(self):
        return self.timeslots
    def get_user_id(self):
        return self.user_id
    def get_organization_id(self):
        return self.organization_id
