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

    def test_make_get_relation(self):
        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 0],
                                                                "notes": "this guy is cool",
                                                                "is_step": True,
                                                                "is_adopted": True,
                                                                "birth_date": "03/11",
                                                                "lives_in": "Alabama",
                                                                "nickname": "Bill"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
    
    def test_with_wrong_param(self):
        wrong_make_rel_param = self.app.post('/relation', data = json.dumps({"user_id": 1,
                                                                            "first": "Billy",
                                                                            "birth_year": "1999"}))
        self.assertEqual(wrong_make_rel_param.status_code, 400)


    def test_with_wrong_user_id(self):
        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 0],
                                                                "notes": "this guy is cool",
                                                                "is_step": True,
                                                                "is_adopted": True,
                                                                "birth_date": "03/11",
                                                                "lives_in": "Alabama",
                                                                "nickname": "Bill"
                                                                }))
        wrong_user_id = self.app.get('/relation/24')
        self.assertEqual(wrong_user_id.status_code, 400)

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": "a string",
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 0],
                                                                "notes": "this guy is cool",
                                                                "is_step": True,
                                                                "is_adopted": True,
                                                                "birth_date": "03/11",
                                                                "lives_in": "Alabama",
                                                                "nickname": "Bill"
                                                                }))
        self.assertEqual(new_relation.status_code, 400)


if __name__ == "__main__":
    unittest.main()