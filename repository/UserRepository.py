from entity.User import User
class UserRepository:

    def __init__(self):
        self.users_by_users_email={}
        self.users_by_users_id={}

    def create_user(self,**kwargs):
        user=User(**kwargs)
        self.users_by_users_email[user.get_email]=user
        self.users_by_users_id[user.get_uid]=user

    def find_by_user_id(self,user_id):
        return self.users_by_users_id[user_id]
    
    def find_by_email(self,email):
        return self.users_by_users_email[email]
    
    def delete_user_by_id(self,user_id):
        user=self.find_by_user_id(user_id)
        self.users_by_users_email.pop(user.email)
        self.users_by_users_id.pop(user_id)

    def delete_user_by_email(self,email):
        user=self.find_by_email(email)
        self.users_by_users_email.pop(email)
        self.users_by_users_id.pop(user.user_id)
    
    def get_all_users(self):
        return self.users_by_users_email.values()


    