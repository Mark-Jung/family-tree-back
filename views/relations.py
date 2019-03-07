from flask import request
from flask.views import MethodView
from controllers.relations import RelationsController

import json
from datetime import datetime

class RelationsView(MethodView):

    @classmethod
    def make_relation(cls):
        data = json.loads(request.data.decode('utf-8'))
        req_params = ['user_id', 'name', 'birth_year', 'is_deceased', 'gender', 'relation', 'notes', 'is_step',
                      'is_adopted']
        for param in req_params:
            if param not in data:
                return json.dumps({"response": "ill-formed request"}), 400

        if not (isinstance(data['user_id'], int) and isinstance(data['name'], str) and isinstance(data['birth_year'], int) and isinstance(data['is_deceased'], bool) and isinstance(data['gender'], str) and isinstance(data['relation'], str) and isinstance(data['notes'], str) and isinstance(data['is_step'], bool) and isinstance(data['is_adopted'], bool)):
            return json.dumps({"response": "ill-formed request"}), 400
        
        error_message, status, response = RelationsController.make_relation(data['user_id'], data['name'], data['birth_year'], data['is_deceased'], data['gender'], data['relation'], data['notes'], data['is_step'], data['is_adopted'])
        if error_message:
            return json.dumps({"error_message": error_message}), status

        return json.dumps({"response": data}), 201

##Bug Here
    @classmethod
    def get_relations(cls, user_id):
        error_message, status, response = RelationsController.get_relations(user_id)
        if error_message:
            return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": list(map(lambda x: x.json() if x else None, response))}), status #reponse




if __name__ == "__main__":
    unittest.main()