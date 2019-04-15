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
        new_user = self.app.post('/signup', data = json.dumps({"username": "uname",}))
        self.assertEqual(new_user.status_code, 201)
        signin_user = self.app.post('/signin', data = json.dumps({"username": "uname",}))
        self.assertEqual(signin_user.status_code, 200)

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 1],
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
        new_user = self.app.post('/signup', data = json.dumps({"username": "uname",}))
        self.assertEqual(new_user.status_code, 201)
        signin_user = self.app.post('/signin', data = json.dumps({"username": "uname",}))
        self.assertEqual(signin_user.status_code, 200)
        
        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 1],
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
                                                                "relation": ["parent", 1],
                                                                "notes": "this guy is cool",
                                                                "is_step": True,
                                                                "is_adopted": True,
                                                                "birth_date": "03/11",
                                                                "lives_in": "Alabama",
                                                                "nickname": "Bill"
                                                                }))
        self.assertEqual(new_relation.status_code, 400)

    def test_relation_calculation(self):
        new_user = self.app.post('/signup', data = json.dumps({"username": "user1",}))
        self.assertEqual(new_user.status_code, 201)
        signin_user = self.app.post('/signin', data = json.dumps({"username": "user1",}))
        self.assertEqual(signin_user.status_code, 200)

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Billy",
                                                                "last": "Bob",
                                                                "birth_year": "1999",
                                                                "death_year": "2010",
                                                                "is_deceased": True,
                                                                "gender": "Male",
                                                                "relation": ["parent", 1],
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
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'father')

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Jennifer",
                                                                "last": "Bob",
                                                                "birth_year": "1960",
                                                                "death_year": "",
                                                                "is_deceased": False,
                                                                "gender": "Other",
                                                                "relation": ["parent", 2],
                                                                "notes": "this person is cool",
                                                                "is_step": False,
                                                                "is_adopted": True,
                                                                "birth_date": "10/11",
                                                                "lives_in": "Alabama",
                                                                "nickname": "Jenn"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'grandparent')


        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Josh",
                                                                "last": "Bob",
                                                                "birth_year": "1996",
                                                                "death_year": "",
                                                                "is_deceased": False,
                                                                "gender": "Other",
                                                                "relation": ["sibling", 3],
                                                                "notes": "farms",
                                                                "is_step": False,
                                                                "is_adopted": True,
                                                                "birth_date": "10/1",
                                                                "lives_in": "Oklahoma",
                                                                "nickname": "Joe"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'grandaunt/granduncle')

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Annie",
                                                                "last": "Bob",
                                                                "birth_year": "1996",
                                                                "death_year": "",
                                                                "is_deceased": False,
                                                                "gender": "Female",
                                                                "relation": ["sibling", 1],
                                                                "notes": "farms",
                                                                "is_step": False,
                                                                "is_adopted": True,
                                                                "birth_date": "10/1",
                                                                "lives_in": "New Jersey",
                                                                "nickname": "Ann"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'sister')

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Lola",
                                                                "last": "Stevenson",
                                                                "birth_year": "1980",
                                                                "death_year": "",
                                                                "is_deceased": False,
                                                                "gender": "Female",
                                                                "relation": ["child", 5],
                                                                "notes": "studies CS",
                                                                "is_step": False,
                                                                "is_adopted": True,
                                                                "birth_date": "10/1",
                                                                "lives_in": "New Jersey",
                                                                "nickname": "LOL"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'niece')

        new_relation = self.app.post('/relation', data = json.dumps({
                                                                "user_id": 1,
                                                                "first": "Bobba",
                                                                "last": "Stevenson",
                                                                "birth_year": "1981",
                                                                "death_year": "",
                                                                "is_deceased": False,
                                                                "gender": "Other",
                                                                "relation": ["partner", 6],
                                                                "notes": "studies Anthropology",
                                                                "is_step": False,
                                                                "is_adopted": True,
                                                                "birth_date": "10/1",
                                                                "lives_in": "New Jersey",
                                                                "nickname": "bubble"
                                                                }))
        self.assertEqual(new_relation.status_code, 201)
        get_relation = self.app.get('/relation/1')
        self.assertEqual(get_relation.status_code, 200)
        new_rel_id = json.loads(new_relation.data.decode('utf-8'))['response']
        res = json.loads(get_relation.data.decode('utf-8'))['response']
        self.assertEqual(res[[i for i,_ in enumerate(res) if _['id'] == new_rel_id][0]]['relation'], 'niece-in-law/nephew-in-law')

if __name__ == "__main__":
    unittest.main()