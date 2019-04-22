from db import db
from models.common import CommonModel
from util.jsonencode import JsonEncodedDict
from datetime import datetime

class RelationsModel(db.Model, CommonModel):
    __tablename__ = 'relations'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key = True)
    first = db.Column(db.String(255))
    last = db.Column(db.String(255))
    death_year = db.Column(db.DateTime)
    is_deceased = db.Column(db.Boolean)
    gender = db.Column(db.String(255))
    relation = db.Column(db.String(255))
    notes = db.Column(db.String(500))
    is_step = db.Column(db.Boolean)
    is_adopted = db.Column(db.Boolean)
    birth_date = db.Column(db.DateTime)
    lives_in = db.Column(db.String(500))
    nickname = db.Column(db.String(255))



    def __init__(self, user_id, first, last, death_year, is_deceased, gender, relation, notes, is_step, is_adopted, birth_date, lives_in, nickname):
        self.user_id =  user_id
        self.first = first
        self.last = last
        self.death_year = death_year
        self.is_deceased = is_deceased
        self.gender = gender
        self.relation = relation
        self.notes = notes
        self.is_step = is_step
        self.is_adopted = is_adopted
        self.birth_date = birth_date
        self.lives_in = lives_in 
        self.nickname = nickname

    @classmethod
    def valid_construction(cls, user_id, first, last, death_year, is_deceased, gender, relation, notes, is_step, is_adopted, birth_date, lives_in, nickname):
        if not (isinstance(user_id, int) and isinstance(first, str) and isinstance(last, str) and isinstance(is_deceased, bool) and isinstance(gender, str) and isinstance(notes, str) and isinstance(is_step, bool) and isinstance(is_adopted, bool) and isinstance(lives_in, str) and isinstance(nickname, str)):
            return None
        return cls(user_id, first, last, death_year, is_deceased, gender, relation, notes, is_step, is_adopted, birth_date, lives_in, nickname)

    
    def json(self):
        return {
            "first": self.first,
            "last": self.last,
            "relation": self.relation,
            "birth_date": self.birth_date.strftime("%m/%d/%Y") if self.birth_date else "", 
        }

    def individual_json(self):
        return {
            "id": self.id,
            "first": self.first,
            "last": self.last,
            "death_year": self.death_year.strftime("%Y") if self.death_year else "",
            "is_deceased": self.is_deceased,
            "gender": self.gender,
            "relation": self.relation,
            "notes": self.notes,
            "is_step": self.is_step,
            "is_adopted": self.is_adopted,
            "birth_date": self.birth_date.strftime("%m/%d/%Y") if self.birth_date else "", 
            "lives_in": self.lives_in, 
            "nickname": self.nickname
        }   


    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()

    @classmethod
    def find_by_relation_id(cls, relation_id):
        return cls.query.filter_by(id = relation_id).all()
