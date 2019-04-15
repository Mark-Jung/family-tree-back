import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
from app import app
from db import db
import json

TEST_DB = 'test.db'

class BasicTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.init_app(app)
        db.drop_all(app=app)
        db.create_all(app=app)


    # executed after each test
    def tearDown(self):
        pass

    def test_signin(self):
        new_user = self.app.post('/signup', data = json.dumps({"username": "uname",}))
        self.assertEqual(new_user.status_code, 201)
        signin_user = self.app.post('/signin', data = json.dumps({"username": "uname",}))
        self.assertEqual(signin_user.status_code, 200)
    
    def test_with_wrong_param(self):
        wrong_signup_param = self.app.post('/signup', data = json.dumps({"not_username": "a",}))
        self.assertEqual(wrong_signup_param.status_code, 400)

        new_user = self.app.post('/signup', data = json.dumps({"username": "uname",}))
        self.assertEqual(new_user.status_code, 201)
        wrong_signin_param = self.app.post('/signin', data = json.dumps({"not_username": "uname",}))
        self.assertEqual(wrong_signin_param.status_code, 400)

    def test_with_wrong_username(self):
        new_signin = self.app.post('/signup', data = json.dumps({"username": 123,}))
        self.assertEqual(new_signin.status_code, 400)

        new_user = self.app.post('/signup', data = json.dumps({"username": "uname",}))
        self.assertEqual(new_user.status_code, 201)
        wrong_username = self.app.post('/signin', data = json.dumps({"username": "aaa",}))
        self.assertEqual(wrong_username.status_code, 400)

if __name__ == "__main__":
    unittest.main()