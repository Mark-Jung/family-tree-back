import os

from db import db
from flask import Flask, request, redirect, Response
from flask_cors import cross_origin, CORS

from views.CalculatorView import CalculatorView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///localdata.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == '__main__':
    CORS(app)

@app.route('/')
def hello_world():
    return "running!"

@app.route('/addtwo', methods=['POST'])
def addtwo():
    return CalculatorView.addtwo()

if __name__ == '__main__':
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run()


