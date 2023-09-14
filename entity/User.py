import re
import uuid
import copy

class User:

    def __init__(self,**kwargs):
        self.uid=uuid.uuid1()
        self.bookings=set()
        try:
            self.first_name=kwargs["first_name"]
        except KeyError as error:
            print("First name is manadatory")
        
        try:
            self.last_name=kwargs["last_name"]
        except KeyError as error:
            print("Last name is manadatory")
        
        try:
            self.email=kwargs["email"]
        except KeyError as error:
            print("Email is manadatory")

        #is it manadatory?
        try:
            self.organization_id=kwargs["organization_id"]
        except KeyError as error:
            print("Email is manadatory")

        #is it manadatory?
        try:
            self.role=kwargs["role_enum"]
        except KeyError as error:
            print("Role name is manadatory")
        
    def get_first_name(self):
        return self.first_name
    def set_first_name(self,first_name:str):
        self.first_name=first_name
    
    def get_last_name(self):
        return self.last_name
    def set_last_name(self,last_name:str):
        self.last_name=last_name

    def get_email(self):
        return self.email

    def set_email(self,email:str):
        try:
            validate_email(email)
            self.email=email
        except TypeError as error:
            print("Email is not valid")
    
    def get_role_enum(self):
        return self.role
    
    def set_role(self,role_enum):
        self.role=role_enum
    
    def get_uid(self):  
        return self.uid
    
    def get_organization_id(self):
        return self.organization_id
    def set_organization_id(self,org_id):
        self.organization_id=org_id
    
    def add_booking(self,booking_id):
        self.bookings.add(booking_id)

    def get_bookings(self):
        return copy.deepcopy(self.bookings)
    
    def delete_booking(self,booking_id):
        self.bookings.discard(booking_id)
    
    def check_booking(self,booking_id):
        return booking_id in self.bookings

    def __str__(self):
        return str(self.__dict__)

        
def validate_email(email):  
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
        return True  
    return False        



    
