from models.user import UserModel
from models.relations import RelationsModel
from datetime import datetime
#from util.logger import Logger
#from util.parser import ReqParser


class UserController():
    @classmethod
    def make_user(cls, username):
        if UserModel.find_by_username(username):
            return "User with that name already exists.", 400, None
        
        new_user_response = None
        try:
            new_user_response = UserModel.valid_construction(username)
            new_user_response.save_to_db()
        except:
            # cls.logger.exception("Error in creating new user")
            if not new_user_response:
                return "ill-formed request", 400, None
            return "Internal Server Error.", 500, None

        new_relation = None
        try:
            new_relation = RelationsModel.valid_construction(new_user_response.id, "", "", datetime.strptime("1900 01/01", '%Y %m/%d'), False, "", "", "", False, False, datetime.strptime("1900", '%Y'), "", "")
            new_relation.save_to_db()
        except:
            if not new_relation:
                return "ill-formed request", 400, None
            return "Internal Server Error.", 500, None
        
        return "", 201, new_user_response.id
    
    @classmethod
    def signin(cls, username):
        signed_user = UserModel.find_by_username(username)
        if not signed_user:
            return "ill-formed request", 400, None
        if signed_user:
            return "", 200, signed_user.id
        return "User does not exist", 400, None



            

