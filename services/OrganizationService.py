from config import organization_repository,user_service
from entity.Organization import Organization
from config import BOOKING_HOUR_LIMIT
from enums.PermissionEnum import Permission
class OrganizationService:

    def add_organization(self,org_name,user_id,**kwargs):
        if user_service.check_permission(user_id,Permission.WRITEFLOOR):
            try:
                organization_repository.create_organization(
                    org_name=org_name,
                    **kwargs
                )
                print("floor successfully added")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")
        
    
    def delete_organization(self,org_name,user_id):

        if user_service.check_permission(user_id,Permission.WRITEFLOOR):
            try:
                org=organization_repository.get_organization_by_name(org_name)
                employee_ids=org.get_employee_id()
                for emp_id in employee_ids:
                    user_service.delete_user(emp_id)
                organization_repository.delete_organization_by_name(org_name)
                print("floor successfully added")
            except Exception as error:
                print(error)
        else:
            print("user with user_id: ",user_id ,"does not have permission to add floor")
        


    def add_user_in_organization(self,organization_id,user_id):
        organization=organization_repository.get_organization_by_id(organization_id)
        organization.add_employee(user_id)
    
    def remove_user_in_organization(self,org_id,user_id):
        organization=organization_repository.get_organization_by_id(org_id)
        organization.delete_employee(user_id)
    
    def get_all_organization(self):
        return organization_repository.get_all_organization_id()
    
    def can_book_room(self,org_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        booked_hours=org.get_booking_hours()
        return booked_hours+num_hours<=BOOKING_HOUR_LIMIT

    def book_room(self,org_id,booking_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        org.add_booking(booking_id)
        org.increase_booking_hour(num_hours)

    def cancel_booking(self,org_id,booking_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        org.delete_booking(booking_id)
        org.decrease_booking_hour(num_hours)

    def check_booking(self,org_id,booking_id):
        org=organization_repository.get_organization_by_id(org_id)
        org.check_booking(booking_id)