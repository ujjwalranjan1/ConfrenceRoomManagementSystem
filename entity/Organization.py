import uuid
from entity.User import User
from enums.RoleEnum import RoleEnum

class Organization:
    def __init__(self,**kwargs):
        self.oid=uuid.uuid1()
        self.bookings=set()
        self.number_of_employee=0
        self.booking_hours=0
        self.employees={
            "admin" : set(),
            "user" : set()
        }
        #employee will have key as admin ,user ,manager
        #value will be set of users
        try:
            self.name=kwargs["org_name"]
        except KeyError as error:
            print("Organization name is manadatory")

        #contacts is not manadatory
        if "contacts" in kwargs:
            self.contacts=kwargs["contacts"]
        
        if "locations" in kwargs:
            self.locations=kwargs["locations"]
        
    def get_name(self):
        return self.name 
    def set_name(self,name):
        self.name=name
    
    def get_contact(self):
        return self.contacts
    
    def add_contact(self,contact):
        self.contacts.add(contact)

    def delete_contacts(self):
        self.contacts.clear()

    def update_contacts(self,old,new):
        try:
            self.contacts[self.contacts.index(old)]=new
        except KeyError as error:
            print("No such element in Contacts: "+old)

    def get_location(self):
        return self.locations
    
    def add_location(self,location):
        self.locations.add(location)

    def delete_locations(self):
        self.locations.clear()
    
    #better to create a class named location so we can edit location
        
    def get_number_of_employee(self):
        return self.number_of_employee
    
    def get_admins_id(self):
        return self.employees["admin"]
    
    def get_user_id(self):
        return self.employees["user"]

    def get_employee_id(self):
        return set.union(self.employees["admin"],self.employees["user"])
    

    def add_employee(self,user_id,role):
        if role==RoleEnum.Admin:
            if user_id not in self.employees["admin"]:
                self.employees["admin"].add(user_id)
                self.number_of_employee=self.number_of_employee+1
            else:
                print(str(user_id) +" already added")
        elif role==RoleEnum.User:
            if user_id not in self.employees["admin"]:
                self.employees["user"].add(user_id)
                self.number_of_employee=self.number_of_employee+1
            else:
                print(str(user_id) +" already added")
    
    def delete_employee(self,user_id,role):
        if role==RoleEnum.Admin:
            try:
                self.employees["admin"].remove(user_id)
                self.number_of_employee=self.number_of_employee-1
            except ValueError as error:
                print("No such element found")
        elif role==RoleEnum.User:
            try:
                self.employees["user"].remove(user_id)
                self.number_of_employee=self.number_of_employee-1
            except ValueError as error:
                print("No such element found")

    def get_oid(self):
        return self.oid
    
    def increase_booking_hour(self,num_hours):
        self.booking_hours=self.booking_hours+num_hours

    def decrease_booking_hour(self,num_hours):
        self.booking_hours=self.booking_hours-num_hours
    
    def get_booking_hours(self):
        return self.booking_hours
    
    def add_booking(self,booking_id):
        self.bookings.add(booking_id)

    def get_bookings(self):
        return self.bookings
    
    def delete_booking(self,booking_id):
        self.bookings.discard(booking_id)
    
    def check_booking(self,booking_id):
        return booking_id in self.bookings
    
    def __str__(self):
        return str(self.__dict__)

        
        
        
        

