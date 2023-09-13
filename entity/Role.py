from enums.PermissionEnum import Permission

class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions
        self.users_id=set()

    def has_permission(self, permission):
        return permission in self.permissions
    
    def add_user_id(self,user_id):
        self.users_id.add(user_id)
        
    def remove_user_id(self,user_id):
        try:
            self.users_id.remove(user_id)
        except ValueError as error:
            print("No such user exist having this role")

    def get_all_user_id(self):
        return self.users_id
    def __str__(self):
        return str(self.__dict__)


