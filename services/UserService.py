from entity.User import User 
from beans.UserRepositoryBean import user_repository
from enums.PermissionEnum import Permission
from beans.RoleServiceBean import role_service

class UserService:
    
    def add_user(self,first_name,last_name,email,organization_id,role_type):
        userr_id=user_repository.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        organization_id=organization_id,
        role_enum=role_type
        )
        return userr_id
            

    def delete_user(self,user_id):
        user_repository.delete_user_by_id(user_id)
            

    def get_user(self,user_id):
        return user_repository.find_by_user_id(user_id)
    
    def get_user_by_email(self,email):
        return user_repository.find_by_email(email)
    
    #update user will be written
    def get_all_users(self):
        return user_repository.get_all_users()
    
    def book_room(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        if user!=None:
            user.add_booking(booking_id)

    def cancel_booking(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        if user!=None:
            user.delete_booking(booking_id)

    def check_booking(self,user_id,booking_id):
        user=user_repository.find_by_user_id(user_id)
        if user!=None:
            user.check_booking(booking_id)

    def check_permission(self,user_email,permission_type):
        user=user_repository.find_by_email(user_email)
        if user!=None:
            role_type=user.get_role_enum()
            role_service.check_permission(role_type,permission_type)

