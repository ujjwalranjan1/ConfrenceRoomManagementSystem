from beans.OrganizationRepositoryBean import organization_repository
from entity.Organization import Organization
from constants import BOOKING_HOUR_LIMIT
from enums.PermissionEnum import Permission
class OrganizationService:

    def add_organization(self,org_name,**kwargs):
        organization_repository.create_organization(
            org_name=org_name,
            **kwargs
        )
        print("Organization added successfully")

    def get_organization_by_name(self,org_name):
         return organization_repository.get_organization_by_name(org_name)
           
    
    def delete_organization(self,org_name):
        organization_repository.delete_organization_by_name(org_name)


    def add_user_in_organization(self,organization_id,user_id,role):
        organization=organization_repository.get_organization_by_id(organization_id)
        if organization!=None:
         organization.add_employee(user_id,role)
    
    def remove_user_in_organization(self,org_id,user_id,role):
        organization=organization_repository.get_organization_by_id(org_id)
        if organization!=None:
         organization.delete_employee(user_id,role)
    
    def get_all_organization(self):
        return organization_repository.get_all_organization()
    
    def can_book_room(self,org_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        if org!=None:
            booked_hours=org.get_booking_hours()
            return booked_hours+num_hours<=BOOKING_HOUR_LIMIT

    def book_room(self,org_id,booking_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        if org!=None:
            org.add_booking(booking_id)
            org.increase_booking_hour(num_hours)

    def cancel_booking(self,org_id,booking_id,num_hours):
        org=organization_repository.get_organization_by_id(org_id)
        if org!=None:
            org.delete_booking(booking_id)
            org.decrease_booking_hour(num_hours)

    def check_booking(self,org_id,booking_id):
        org=organization_repository.get_organization_by_id(org_id)
        if org!=None:
         org.check_booking(booking_id)