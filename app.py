import os

from db import db
from flask import Flask, request, redirect, Response
from flask_cors import cross_origin, CORS

from views.user import UserView
from views.relations import RelationsView
from models.relations import RelationsModel
from models.user import UserModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///localdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == '__main__':
    CORS(app)

@app.route('/')
def hello_world():
    return "running!"

@app.route('/signup', methods=['POST'])
def user():
    return UserView.make_user()

@app.route('/signin', methods=['POST'])
def signin():
    return UserView.signin()

@app.route('/relation', methods=['POST'])
def relation():
    #if request.method == 'POST':
    return RelationsView.make_relation()
    # elif request.method == 'GET':
    #     return RelationsView.get_relations()

@app.route('/relations/<string:user_id>', methods=['GET'])
def relations_by_user_id(user_id):
    return RelationsView.get_relations(user_id)

@app.route('/relation/<string:relation_id>', methods=['GET'])
def relation_by_relation_id(relation_id):
    return RelationsView.get_specific_relation(relation_id)


if __name__ == '__main__':
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()



