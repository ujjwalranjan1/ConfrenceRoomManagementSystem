from entity.Organization import Organization
from beans.OrganizationServiceBean import organization_service
from beans.UserServiceBean import user_service
from beans.RoleServiceBean import role_service
from beans.BookingServiceBean import booking_service
from beans.BookingControllerBean import booking_controller

class OrganizationController:
    def create_organization(self,org_name,**kwargs):
        organization_service.add_organization(org_name,**kwargs)

    def delete_organization(self,org_name):
        org=organization_service.get_organization_by_name(org_name)
        if org!=None:
            employee_ids=org.get_employee_id()
            for emp_id in employee_ids:
                user=user_service.get_user(emp_id)
                if user!=None:
                    role_service.remove_user(emp_id,user.get_role_enum())
                    #delete all bookings by organization as well
                    booking_ids=user.get_bookings()
                    for id in booking_ids:
                        booking_controller.delete_booking(id)
                    user_service.delete_user(emp_id)
            organization_service.delete_organization(org_name)

        