class TimeSlot:
    def __init__(self, hour):
        self.start_hour = hour
        self.end_hour = hour + 1
        self.booked_rooms=set()
        self.available_rooms=set()
        self.rooms=set()

    def add_room(self,room_id):
        # if room_id not in set.union(self.booked_rooms, self.available_rooms):
        if room_id not in self.rooms:
            self.rooms.add(room_id)
            self.available_rooms.add(room_id)

    def remove_room(self,room_id):
        try:
            self.rooms.remove(room_id)
        except ValueError as error:
            print("No such room found")
        self.booked_rooms.discard(room_id)
        self.available_rooms.discard(room_id)

    def book_room(self,room_id):
        try:
            self.available_rooms.remove(room_id)
            self.booked_rooms.add(room_id)
        except ValueError as error:
            print("Room not Available")
    
    def cancel_booked_room(self,room_id):
        try:
            self.booked_rooms.remove(room_id)
            self.available_rooms.add(room_id)
        except ValueError as error:
            print("No such booking exist")
    
    def get_all_room(self):
        return self.rooms
    def get_all_available_room(self):
        return self.available_rooms
    def get_all_booked_room(self):
        return self.booked_rooms
    


