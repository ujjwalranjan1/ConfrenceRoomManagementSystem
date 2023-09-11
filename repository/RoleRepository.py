from entity.Role import Role
from enums.PermissionEnum import Permission
from enums.RoleEnum import RoleEnum

class RoleRepository:
    def __init__(self):
        self.role={}
        self.role[RoleEnum.Admin] = Role("Admin", [Permission.READROOM, Permission.WRITEROOM, Permission.READUSER,Permission.WRITEUSER,Permission.READORGANIZATION,Permission.WRITEORGANIZATION,Permission.READFLOOR,Permission.WRITEFLOOR])
        self.role[RoleEnum.User] = Role("Regular User", [Permission.READROOM,Permission.READORGANIZATION,Permission.READFLOOR])

    def get_role(self,role_enum):
         return self.role[role_enum]
    