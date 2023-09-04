from Permission import Permission

class Role:
    def __init__(self, name, permissions=[]):
        self.name = name
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

# Define predefined roles
admin_role = Role("Admin", [Permission.READROOM, Permission.WRITEROOM, Permission.READUSER,Permission.WRITEUSER,Permission.READORGANIZATION,Permission.WRITEORGANIZATION])
user_role = Role("Regular User", [Permission.READROOM,Permission.READORGANIZATION])
