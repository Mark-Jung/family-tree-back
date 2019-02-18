from flask import request
from flask.views import MethodView


import json

class CalculatorView(MethodView):
    
    @classmethod
    def addtwo(cls):

        data = json.loads(request.data.decode('utf-8'))
        req_params = ['numone', 'numtwo']
        return str(data['numone']+data['numtwo']), 200