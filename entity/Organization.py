import uuid
from User import User
from Role import admin_role,user_role

class Organization:
    def __init__(self,**kwargs):
        self.oid=uuid.uuid1()
        self.number_of_employee=0
        self.employees={
            "admin" : set(),
            "user" : set()
        }
        #employee will have key as admin ,user ,manager
        #value will be set of users
        try:
            self.name=kwargs["name"]
        except KeyError as error:
            print("Organization name is manadatory")

        #contacts is not manadatory
        if kwargs["contacts"]!=None:
            self.contacts=kwargs["contacts"]
        
        if kwargs["locations"]!=None:
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
    

    def add_employee(self,user:User):
        if user.role==admin_role:
            if user.get_uid not in self.employees["admin"]:
                self.employees["admin"].add(user.get_uid)
                self.number_of_employee=self.number_of_employee+1
            else:
                print(str(user.uid) +" already added")
        elif user.role==user_role:
            if user.get_uid not in self.employees["admin"]:
                self.employees["user"].add(user.get_uid)
                self.number_of_employee=self.number_of_employee+1
            else:
                print(str(user.uid) +" already added")
    
    def delete_employee(self,user:User):
        if user.role==admin_role:
            try:
                self.employees["admin"].remove(user.get_uid)
                self.number_of_employee=self.number_of_employee-1
            except ValueError as error:
                print("No such element found")
        elif user.role==user_role:
            try:
                self.employees["user"].remove(user.get_uid)
                self.number_of_employee=self.number_of_employee-1
            except ValueError as error:
                print("No such element found")



        
        
        
        

