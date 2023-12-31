from entity.User import User
class UserRepository:

    def __init__(self):
        self.users_by_users_email={}
        self.users_by_users_id={}
 
    def create_user(self,**kwargs):
        user=User(**kwargs)
        self.users_by_users_email[user.get_email()]=user
        self.users_by_users_id[user.get_uid()]=user
        return user.get_uid()

    def find_by_user_id(self,user_id):
        try:
            return self.users_by_users_id[user_id]
        except:
            print("no such user")
    
    def find_by_email(self,email):
        try:
            return self.users_by_users_email[email]
        except:
            print("no such user")
    
    def delete_user_by_id(self,user_id):
        user=self.find_by_user_id(user_id)
        if user!=None:
            self.users_by_users_email.pop(user.email)
            self.users_by_users_id.pop(user_id)

    def delete_user_by_email(self,email):
        user=self.find_by_email(email)
        if user!=None:
            self.users_by_users_email.pop(email)
            self.users_by_users_id.pop(user.get_uid())
    
    def get_all_users(self):
        return self.users_by_users_email.values()


    