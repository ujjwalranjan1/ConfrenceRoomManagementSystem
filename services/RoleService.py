from entity.Role import Role
from enums import RoleEnum
from config import role_repository

class RoleService:
    def find_role_by_role_enum(self,role_enum):
        return role_repository.get_role(role_enum)