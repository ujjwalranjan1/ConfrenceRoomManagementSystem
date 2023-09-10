from entity.Role import Role
from enums import RoleEnum
from config import role_repository

class RoleService:

    def find_role_by_role_enum(self,role_enum):
        return role_repository.get_role(role_enum)
    
    def add_user(self,user_id,role_enum):
        role=role_repository.get_role(role_enum)
        role.add_user_id(user_id)
    
    def remove_user(self,user_id,role_enum):
        role=role_repository.get_role(role_enum)
        role.remove_user_id(user_id)