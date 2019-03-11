from flask import request
from flask.views import MethodView
from controllers.user import UserController

import json

class UserView(MethodView):
    
    @classmethod
    def make_user(cls):
        data = json.loads(request.data.decode('utf-8'))
        req_params = ['username']
        if 'username' not in data:
            return json.dumps({"response": "ill-formed request"}), 400
        
        if not isinstance(data['username'], str):
            return json.dumps({"response": "ill-formed request"}), 400
        
        error_message, status, response = UserController.make_user(data['username'])
        if error_message:
            return json.dumps({"response": error_message}), status

        return json.dumps({"response": response}), 201

    @classmethod
    def signin(cls):
        data = json.loads(request.data.decode('utf-8'))
        req_params = ['username']
        if 'username' not in data:
            return json.dumps({"response": "ill-formed request"}), 400
        
        if not isinstance(data['username'], str):
            return json.dumps({"response": "ill-formed request"}), 400
        
        error_message, status, response = UserController.signin(data['username'])
        if error_message:
            return json.dumps({"response": error_message}), status

        return json.dumps({"response": response}), 200
    
if __name__ == "__main__":
    unittest.main()