from entity.Role import Role
from entity.Permission import Permission
from entity.RoleEnum import RoleEnum

class RoleRepository:
    def __init__(self):
        self.role={}
        self.role[RoleEnum.Admin] = Role("Admin", [Permission.READROOM, Permission.WRITEROOM, Permission.READUSER,Permission.WRITEUSER,Permission.READORGANIZATION,Permission.WRITEORGANIZATION])
        self.role[RoleEnum.User] = Role("Regular User", [Permission.READROOM,Permission.READORGANIZATION])

    def add_user_id(self,user_id,role_enum:RoleEnum):
        self.role[role_enum].add_user_id(user_id)

    def remove_user_id(self,user_id,role_enum:RoleEnum):
        try:
                self.role[role_enum].remove_user_id(user_id)
        except Exception as e:
            print(e)
            
    def get_role(self,role_enum):
         return self.role[role_enum]
    