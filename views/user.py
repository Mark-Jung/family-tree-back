from flask import request
from flask.views import MethodView
from controllers.user import UserController

import json

class UserView(MethodView):
    
    @classmethod
    def make_user(cls):

        data = json.loads(request.data.decode('utf-8'))
        req_params = ['username'] 
        print("view")
        error_message, status, response = UserController.make_user(data['username'])
        if error_message:
            return json.dumps({"error_message": error_message}), status

        return json.dumps({"message": "Success!"}), 201