from models.relations import RelationsModel
from models.user import UserModel


class RelationsController():
    @classmethod
    def make_relation(cls, user_id, first, last, death_year, is_deceased, gender, relation, notes, is_step, is_adopted, birth_date, lives_in, nickname):
        # if not UserModel.find_by_id(user_id):
        #     return "User with that id does not exist", 400, None
        rln = relation[0]
        related_to = relation[1]
        relation_out = "uncle" #placeholder. have to do computation for relationship
        try:
            new_relation = RelationsModel(user_id, first, last, death_year, is_deceased, gender, relation_out, notes, is_step, is_adopted, birth_date, lives_in, nickname)
            new_relation.save_to_db()
        except:
            # cls.logger.exception("Error in creating new user")
            return "Internal Server Error.", 500, None
        return "", 201, None

    @classmethod
    def get_relations(cls, user_id):

        try:
            relations = RelationsModel.find_by_user_id(user_id)
            if relations == []:
                return "No relations found for the given user id", 400, None
            return "", 200, relations
        except:
            return "Error retrieving relations for user id",500, None