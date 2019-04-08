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

        if not (isinstance(data['user_id'], int) and isinstance(data['first'], str) and isinstance(data['last'], str) and isinstance(data['is_deceased'], bool) and isinstance(data['gender'], str) and isinstance(data['relation'][0], str) and isinstance(data['relation'][1], int) and isinstance(data['notes'], str) and isinstance(data['is_step'], bool) and isinstance(data['is_adopted'], bool) and isinstance(data['lives_in'], str) and isinstance(data['nickname'], str)):
            return json.dumps({"response": "ill-formed request"}), 400
        
        if data['birth_year'] and data['birth_date']:
            birth_total_str = data['birth_year'] + " " + data['birth_date']
            birth_date = datetime.strptime(birth_total_str, '%Y %m/%d')
        elif data['birth_year']:
            birth_date = datetime.strptime(data['birth_year'], '%Y')
        elif data['birth_date']:
            birth_total_str = "1000" + " " + data['birth_date']
            birth_date = datetime.strptime(birth_total_str, '%Y %m/%d')
        else:
            birth_date = None

        if data['death_year']:
            death_year = datetime.strptime(data['death_year'], '%Y')
        else:
            death_year = None

        error_message, status, response = RelationsController.make_relation(data['user_id'], data['first'], data['last'], death_year, data['is_deceased'], data['gender'], data['relation'], data['notes'], data['is_step'], data['is_adopted'], birth_date, data['lives_in'], data['nickname'])
        if error_message:
            return json.dumps({"response": error_message}), status

        return json.dumps({"response": "success!"}), 201

##Bug Here
    @classmethod
    def get_relations(cls, user_id):
        error_message, status, response = RelationsController.get_relations(user_id)
        if error_message:
            return json.dumps({"response": error_message}), status
        return json.dumps({"response": list(map(lambda x: x.json() if x else None, response))}), status #reponse



