from models.user import UserModel
#from util.logger import Logger
#from util.parser import ReqParser


class UserController():
    @classmethod
    def make_user(cls, username):
        if UserModel.find_by_username(username):
            return "User with that name already exists.", 400, None
        
        try:
            new_user = UserModel(username)
            new_user.save_to_db()
        except:
            # cls.logger.exception("Error in creating new user")
            return "Internal Server Error.", 500, None
        
        return "", 201, None
    
    @classmethod
    def signin(cls, username):
        if UserModel.find_by_username(username):
            return "", 200, None
        return "User does not exist", 400, None



            

