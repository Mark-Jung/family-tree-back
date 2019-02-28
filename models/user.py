from db import db
from models.common import CommonModel

class UserModel(db.Model, CommonModel):
   
    __tablename__='user'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    username = db.Column(db.String(500))


    def __init__(self, username):
        self.username = username

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def get_all_id(cls):
        ids = []
        for each in cls.query.all():
            ids.append(each.id)
        return ids

    @classmethod
    def id_by_username(cls, username):
        return cls.query.filter_by(username = username).first().id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
