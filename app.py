import os

from db import db
from flask import Flask, request, redirect, Response
from flask_cors import cross_origin, CORS

from views.user import UserView
from views.relations import RelationsView
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


#did i not save my app.py from last time?

@app.route('/relation', methods=['POST'])
def make_relation():
    return RelationsView.make_relation()

@app.route('/relation/<string:user_id>', methods=['GET'])
def get_relations(user_id):
    return RelationsView.get_relations(user_id)

if __name__ == '__main__':
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run(debug=True)


