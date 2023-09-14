from beans.UserServiceBean import user_service
from beans.RoleServiceBean import role_service
from beans.OrganizationServiceBean import organization_service
from beans.UserServiceBean import user_service
from beans.BookingControllerBean import booking_controller
from enums.PermissionEnum import Permission

class UserController:

    def add_user(self,first_name,last_name,email,organization_name,role_type,user_email):
        if user_service.check_permission(user_email,Permission.WRITEUSER):
            org=organization_service.get_organization_by_name(organization_name)
            if org!=None:
                organization_id=org.get_oid()
                user_id=user_service.add_user(first_name,last_name,email,organization_id,role_type)
                role_service.add_user(user_id,role_type)
                organization_service.add_user_in_organization(organization_id,user_id,role_type)
        else:
            print("no permission for user")
            
    def delete_user(self,email,user_email):
        if user_service.check_permission(user_email,Permission.WRITEUSER):
            user=user_service.get_user_by_email(email)
            if user!=None:
                organization_service.remove_user_in_organization(user.get_organization_id(),user.get_uid(),user.get_role_enum())
                role_service.remove_user(user.get_uid(),user.get_role_enum())
                #remove bookings done by user
                booking_ids=user.get_bookings()
                for id in booking_ids:
                    booking_controller.delete_booking(id,user_email)
                user_service.delete_user(user.get_uid())
        else:
            print("no permission for user")

