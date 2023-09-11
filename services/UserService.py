from entity.User import User 
from config import user_repository,organization_service,role_service

class UserService:
    
    def add_user(self,first_name,last_name,email,organization_id,role_type):
        user_id=user_repository.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            organization_id=organization_id,
            role=role_type
        )
        role_service.add_user(user_id,role_type)
        organization_service.add_user_in_organization(organization_id,user_id)

    def delete_user(self,email):
        user=user_repository.find_by_email(email)
        role_service.remove_user(user.get_uid(),user.get_role_enum())
        organization_service.remove_user_in_organization(user.get_organization_id(),user.get_uid())
        user_repository.delete_user_by_id(user.get_uid())

    def get_user(self,user_id):
        return user_repository.find_by_user_id(user_id)
    
    #update user will be written
    def get_all_users(self):
        return user_repository.get_all_users()
    
    def book_room(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        user.add_booking(booking_id)

    def cancel_booking(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        user.delete_booking(booking_id)

    def check_booking(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        user.check_booking(booking_id)

    def check_permission(self,user_id,permission_type):
        user=user_repository.find_by_user_id(user_id)
        role_type=user.get_role_enum()
        role_service.check_permission(role_type,permission_type)

