from db import db
from models.common import CommonModel
from util.jsonencode import JsonEncodedDict

class RelationsModel(db.Model, CommonModel):
    __tablename__ = 'relations'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    birth_year = db.Column(db.Integer) #date
    is_deceased = db.Column(db.Boolean)
    gender = db.Column(db.String(255))
    relation = db.Column(db.String(255))
    notes = db.Column(db.String(500))
    is_step = db.Column(db.Boolean)
    is_adopted = db.Column(db.Boolean)



    def __init__(self, user_id, name, birth_year, is_deceased, gender, relation, notes, is_step, is_adopted):
        self.user_id =  user_id
        self.name = name
        self.birth_year = birth_year
        self.is_deceased = is_deceased
        self.gender = gender
        self.relation = relation
        self.notes =notes
        self.is_step = is_step
        self.is_adopted = is_adopted

    def json(self):
        return {
            "id": self.id,#do we need to return id and user_id?
            "name": self.name,
            "birth_year": self.birth_year,
            "is_deceased": self.is_deceased,
            "gender": self.gender,
            "relation": self.relation,
            "notes": self.notes,
            "is_step": self.is_step,
            "is_adopted": self.is_adopted
        }


    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()



