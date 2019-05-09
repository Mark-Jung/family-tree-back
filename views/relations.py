from flask import request
from flask.views import MethodView
from controllers.relations import RelationsController

import json
from datetime import datetime

class RelationsView(MethodView):

    @classmethod
    def make_relation(cls):
        data = json.loads(request.data.decode('utf-8'))
        req_params = ['user_id', 'first', 'last', 'birth_year', 'death_year', 'is_deceased', 'gender', 'relation', 'notes', 'is_step', 'is_adopted', 'birth_date', 'lives_in', 'nickname']
        for param in req_params:
            if param not in data:
                return json.dumps({"response": "ill-formed request"}), 400

        error_message, status, response = RelationsController.make_relation(data['user_id'], data['first'], data['last'], data['death_year'], data['is_deceased'], data['gender'], data['relation'], data['notes'], data['is_step'], data['is_adopted'], data['birth_date'], data['birth_year'], data['lives_in'], data['nickname'])
        if error_message:
            return json.dumps({"response": error_message}), status

        return json.dumps({"response": response}), 201

##Bug Here
    @classmethod
    def get_relations(cls, user_id):
        error_message, status, response = RelationsController.get_relations(user_id)
        if error_message:
            return json.dumps({"response": error_message}), status
        return json.dumps({"response": list(map(lambda x: x.json() if x else None, response))}), status
     
    @classmethod
    def get_specific_relation(cls, relation_id):
        error_message, status, response = RelationsController.get_specific_relation(relation_id)
        if error_message:
            return json.dumps({"response": error_message}), status
        return json.dumps({"response": list(response.individual_json())}), status



